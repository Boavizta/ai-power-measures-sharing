# SPDX-License-Identifier: Creative Commons 4.0

 #############################################################################
# ~#~ AI Power Measure Sharing ~#~                                            #
# 'Facilitate knowledge sharing and open data in AI's power consumption'      #
# Orange/INNOV/DATA-AI, Orange Innovation Research Program 'Responsible AI'   #
 #############################################################################

#!/usr/bin/python

import os
import json

class ApiGenerator:

    __classes:list[dict] = []

    __input_uri:str = None

    def __handle_schema(self, schema:dict):
        pass

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
                    self.__handle_schema(schema=schema)
