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

    __status:str = 'idle'   # 'idle', if defined by a property but not yet from a schema, '

    nested:bool = False     # if the class is described as a sub-object, embedded in the main object of the JSON schema

    name:str = None
    description:str = None
    properties: dict[str, PropertyDescription]


class ApiGenerator:

    __classes:list[dict] = []

    __input_uri:str = None


    def __handle_object(self, properties:list, name:str, name_prefix:str=None, description:str=None):
        # create the object instance
        cd = ClassDescription()
        cd.nested = name_prefix is not None and len(name_prefix) > 0
        cd.name = '_'.join([ name_prefix, name ]) if cd.nested else name
        cd.description = description
        for p in properties:
            pass


    def __handle_schema(self, schema:dict):
        root_keys = schema.keys()
        if not set([ '$schema', '$id', 'title', 'properties', 'required' ]).issubset(set(root_keys)):
            print('Missing mandatory properties, aborted')
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
                    self.__handle_schema(schema=schema)
