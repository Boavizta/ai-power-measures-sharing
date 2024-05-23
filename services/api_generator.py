# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python

import os
import json


class PropertyDescription:
    """Description of a property value in the JSON schema."""
    type:str = None
    items:str = None
    description:str = None


class ClassDescription:
    """Description of an object found in the JSON schema.
    """

    __status:str = 'idle'   # 'idle', if defined from a property but not yet from a schema, 'ready' if defined from a schema, 'ambiguous' if name defined twice.

    nested:bool = False     # if the class is described as a sub-object, embedded in the main object of the JSON schema

    name:str = None
    description:str = None
    properties: dict[str, PropertyDescription] = {}

    def set_ready(self):
        self.__status = 'ready'

    def set_ambiguous(self):
        self.__status = 'ambiguous'

    def get_status(self)->str:
        return self.__status


class ApiGenerator:

    __classes:dict[str, ClassDescription] = {}

    __input_uri:str = None

    __schemas_processed:list[str] = [] # list avoiding infinite loop on files previously processed

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
            return
        elif pd.type == 'array':
            pass
        elif pd.type == 'object':
            pass
        else:
            # unknown type
            raise Exception('Unknown "type" attribute in the property definition for {}.{}'.format(parent_object.name, name))
        # add property to parent class
        if name in parent_object.properties.keys():
            raise Exception('Redundant property definition for {}.{}'.format(parent_object.name, name))
        parent_object.properties[name] = pd

    def __handle_object(self, properties:dict, name:str, name_prefix:str=None, description:str=None):
        """Process a class within the schema (root class or anonymous nested class or class referenced in another schema).
        """
        # create the object instance
        cd = ClassDescription()
        cd.nested = name_prefix is not None and len(name_prefix) > 0
        cd.name = '_'.join([ name_prefix, name ]) if cd.nested else name
        cd.description = description
        if cd.name in self.__classes.keys():
            print('Ambiguous class name found '+cd.name)
            self.__classes[cd.name].set_ambiguous()
            return
        cd.set_ready()

        for p in properties.keys():
            self.__handle_property(definition=properties[p], name=p, parent_object=cd)

        self.__classes[cd.name] = cd


    def __handle_schema(self, schema:dict):
        """Process a full schema dictionary.
        """
        root_keys = schema.keys()
        if not set([ '$schema', '$id', 'title', 'properties', 'required' ]).issubset(set(root_keys)):
            raise Exception('Missing mandatory properties, aborted')
        if schema['type'] != 'object':
            raise Exception('Currently, only root entities of type "object" are supported')
        # handle root class
        description = schema['description'] if 'description' in root_keys else None
        self.__handle_object(properties=schema['properties'], name=str(schema['title']).capitalize(), name_prefix=None, description=description)
            

    def __init__(self, input_uri:str) -> None:
        """The constructor should be able to deal with a local folder or with an URL. Currently, only local folder is supported.
        """
        self.__input_uri = input_uri
        if input_uri is None:
            raise Exception('Empty URI')
        elif input_uri.startswith('http:') or input_uri.startswith('https:'):
            # TODO
            raise Exception('URL is not currently supported.')
        else:
            # The URI is expected to be an existing folder
            if self.__input_uri.endswith(os.sep):
                self.__input_uri = self.__input_uri[0:len(self.__input_uri-1)]
            if not os.path.isdir(self.__input_uri):
                raise Exception('The folder does not exist')
            files = [ f for f in os.listdir(input_uri) if f.endswith('.json')]
            if files is None or len(files) == 0:
                raise Exception('No JSON schema found')
            for f in files:
                with open(os.sep.join([ self.__input_uri, f ]), mode='r', encoding='utf-8') as fp:
                    schema = json.load(fp)
                    print(f)
                    if type(schema) != dict:
                        raise Exception('Unexpected JSON content type')
                    self.__schemas_processed.append(f)
                    self.__handle_schema(schema=schema)
