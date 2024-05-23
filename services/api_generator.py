# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python

import os
import json

def format_name(name:str) -> str:
    return name.replace('$', '').capitalize()

class PropertyDescription:
    """Description of a property value in the JSON schema."""
    type:str = None
    items:str = None
    description:str = None

    def user_friendly_type(self) -> str:
        return self.type if self.items is None else '{}[{}]'.format(self.type, self.items)


class ClassDescription:
    """Description of an object found in the JSON schema.
    """

    __status:str = 'idle'   # 'idle', if defined from a property but not yet from a schema, 'ready' if defined from a schema, 'ambiguous' if name defined twice.

    nested:bool = False     # if the class is described as a sub-object, embedded in the main object of the JSON schema

    name:str = None
    description:str = None
    properties: dict[str, PropertyDescription] = None

    __buffer: dict[str, PropertyDescription] = None # to avoid modifying a dict while keys are enumerated in a loop

    def __init__(self) -> None:
        self.properties = dict()
        self.__buffer = dict()
    
    def set_ambiguous(self):
        self.__status = 'ambiguous'

    def get_status(self)->str:
        return self.__status
    
    def to_dict(self) -> dict:
        return {
            'nested': self.nested,
            'name': self.name,
            'description': self.description,
            'properties': dict(zip(self.properties.keys(), [ pd.user_friendly_type() for pd in self.properties.values()]))
        }
    
    def add_buffered_property(self, key:str, value:PropertyDescription):
        self.__buffer[key] = value

    def flush_buffer(self):
        self.properties = self.properties | self.__buffer
        self.__buffer = {}


class ApiGenerator:

    __classes:dict[str, ClassDescription] = {}

    __input_uri:str = None

    """The keys are JSON filenames and the values are class names. Necessary when processing references.
    """
    __root_classnames:dict[str, str] = {}

    __GENERIC_PROPERTY_DESCRIPTION:PropertyDescription # used to reference untyped objects

    def __handle_array(self, items:dict, parent_property:PropertyDescription, parent_property_name:str, parent_object:ClassDescription):
        attributes = items.keys()
        if 'type' not in attributes:
            raise Exception('Missing "type" attribute in the array items definition for {}.{}'.format(parent_object.name, parent_property_name))
        if items['type'] in [ 'string', 'number', 'integer', 'boolean', 'null' ]:
            # the items are a literal type, processing ends normally
            parent_property.items = items['type']
            return        
        elif items['type'] == 'object':
            # 2 sub-cases, either anonymous nested object or class defined in schema
            if 'additionalProperties' in attributes:
                # referenced object
                reference = items['additionalProperties']
                if type(reference) != dict or '$ref' not in reference.keys():
                    raise Exception('Missing "$ref" attribute in additional properties of the array items definition for {}.{}'.format(parent_object.name, parent_property_name))
                referenced_schema = str(reference['$ref']).split('/')[-1]
                if referenced_schema not in self.__root_classnames.keys():
                    raise Exception('Unknown schema {} referenced by the array items definition for {}.{}'.format(referenced_schema, parent_object.name, parent_property_name))
                parent_property.items = ':'.join([ 'object', self.__root_classnames[referenced_schema] ])
            else:
                # anonymous nested object
                if 'properties' not in attributes:
                    print('Untyped generic object should be avoided in array items definition for {}.{}'.format(parent_object.name, parent_property_name))
                    # TODO
                print('Anonymous array-wise object: NOT IMPLEMENTED YET for {}.{}'.format(parent_object.name, parent_property_name))
                # TODO
        else:
            raise Exception('Type not handled for items of array property {}'.format(parent_property_name))

    def __handle_property(self, definition:dict, name:str, parent_object:ClassDescription):
        """Process the dictionary describing a property.
        """
        attributes = definition.keys()
        if 'type' not in attributes:
            raise Exception('Missing "type" attribute in the property definition for {}.{}'.format(parent_object.name, name))
        pass

        # initialize new property
        pd = PropertyDescription()
        pd.type = definition['type']

        if 'description' in attributes:
            pd.description = definition['description']

        # specific behavior depending on property type: literals, arrays, objects
        if pd.type in [ 'string', 'number', 'integer', 'boolean', 'null' ]:
            # the property is a literal type, processing ends normally
            pass

        elif pd.type == 'array':
            if 'items' not in attributes:
                raise Exception('Missing "items" attribute in the definition for array {}.{}'.format(parent_object.name, name))
            self.__handle_array(items=definition['items'], parent_property=pd, parent_property_name=name, parent_object=parent_object)

        elif pd.type == 'object':

            # 2 sub-cases, either anonymous nested object or class defined in schema
            if 'additionalProperties' in attributes:
                # referenced object
                reference = definition['additionalProperties']
                if type(reference) != dict or '$ref' not in reference.keys():
                    raise Exception('Missing "$ref" attribute in additional properties of the property definition for {}.{}'.format(parent_object.name, name))
                referenced_schema = str(reference['$ref']).split('/')[-1]
                if referenced_schema not in self.__root_classnames.keys():
                    raise Exception('Unknown schema {} referenced by the property definition for {}.{}'.format(referenced_schema, parent_object.name, name))
                # update property type                
                pd.type = ':'.join([ 'object', self.__root_classnames[referenced_schema] ])
            else:
                # anonymous nested object
                if 'properties' not in attributes:
                    print('Untyped generic object should be avoided in the property definition for {}.{}'.format(parent_object.name, name))
                    pd.type = 'object'
                else:
                    self.__handle_object(properties=definition['properties'], name=format_name(name=name), name_prefix=parent_object.name, description=definition['description'] if 'description' in attributes else None)
                    pd.type = ':'.join([ 'object', '_'.join([ parent_object.name, format_name(name=name) ]) ])            

        else:
            # unknown type
            raise Exception('Unknown "type" attribute in the property definition for {}.{}'.format(parent_object.name, name))

        # add property to parent class
        if name in parent_object.properties.keys():
            raise Exception('Redundant property definition for {}.{}'.format(parent_object.name, name))
        parent_object.add_buffered_property(key=name, value=pd)
        print('Added property {} to buffer of class {}'.format(name, parent_object.name))

    def __handle_object(self, properties:dict, name:str, name_prefix:str=None, description:str=None):
        """Process a class within the schema (root class or anonymous nested class or class referenced in another schema).
        """
        # create the object instance
        print('Handling object {} with properties {}.'.format(name, str(list(properties.keys()))))
        cd = ClassDescription()
        cd.nested = name_prefix is not None and len(name_prefix) > 0
        formatted_name = format_name(name=name)
        cd.name = '_'.join([ name_prefix, formatted_name ]) if cd.nested else formatted_name
        cd.description = description
        if cd.name in self.__classes.keys():
            print('Ambiguous class name found '+cd.name)
            self.__classes[cd.name].set_ambiguous()
            return

        for p in properties.keys():
            self.__handle_property(definition=properties[p], name=p, parent_object=cd)
        cd.flush_buffer()
        print('Now, class {} has properties {}'.format(cd.name, str(list(cd.properties.keys()))))


        self.__classes[cd.name] = cd

    def __handle_schema(self, schema:dict):
        """Process a full schema dictionary.
        """
        root_keys = schema.keys()
        # handle root class
        description = schema['description'] if 'description' in root_keys else None
        self.__handle_object(properties=schema['properties'], name=str(format_name(name=schema['title'])), name_prefix=None, description=description)

    def __handle_root_classname(self, filename:str):
        """Bootstrap class names and associate to containing file.
        """
        with open(os.sep.join([ self.__input_uri, filename ]), mode='r', encoding='utf-8') as fp:
            schema = json.load(fp)
            if type(schema) != dict:
                raise Exception('Unexpected JSON content type')
            root_keys = schema.keys()
            if not set([ '$schema', '$id', 'title', 'properties', 'required' ]).issubset(set(root_keys)):
                raise Exception('Missing mandatory properties, aborted')
            if schema['type'] != 'object':
                raise Exception('Currently, only root entities of type "object" are supported')
            self.__root_classnames[filename] = format_name(name=str(schema['title']))

    def __init__(self, input_uri:str) -> None:
        """The constructor should be able to deal with a local folder or with an URL. Currently, only local folder is supported.
        """
        self.__GENERIC_PROPERTY_DESCRIPTION = PropertyDescription()
        self.__GENERIC_PROPERTY_DESCRIPTION.type = 'object'
        self.__input_uri = input_uri
        if input_uri is None:
            raise Exception('Empty URI')
        elif input_uri.startswith('http:') or input_uri.startswith('https:'):
            # TODO
            raise Exception('URL is not currently supported.')
        else:
            # the URI is expected to be an existing folder
            if self.__input_uri.endswith(os.sep):
                self.__input_uri = self.__input_uri[0:len(self.__input_uri-1)]
            if not os.path.isdir(self.__input_uri):
                raise Exception('The folder does not exist')
            files = [ f for f in os.listdir(input_uri) if f.endswith('.json') ]
            if files is None or len(files) == 0:
                raise Exception('No JSON schema found')
            # pre-loop to initialize all objects with at least their class name, necessary for object references on-the-fly
            for f in files:
                self.__handle_root_classname(f)
            print('Root classes are {}'.format(str(self.__root_classnames)))
            # main loop processing schemas recursively
            for f in files:
                with open(os.sep.join([ self.__input_uri, f ]), mode='r', encoding='utf-8') as fp:
                    schema = json.load(fp)
                    print(f)
                    self.__handle_schema(schema=schema)
                    print()
            print('Final classes parsed are: {}'.format(json.dumps(dict(zip(self.__classes.keys(), [ cd.to_dict() for cd in self.__classes.values() ])), indent=4)))
