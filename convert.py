#!/usr/bin/env python

import io
import json
from pogoprotos.networking.responses.download_item_templates_response_pb2 import DownloadItemTemplatesResponse
from google.protobuf.json_format import MessageToDict

def main():
    with open('gm.bin', 'rb') as gm:
        msg = DownloadItemTemplatesResponse()
        msg.ParseFromString( gm.read() )
        dict_obj = MessageToDict(msg)
        #print json.dumps(dict_obj, sort_keys=True, indent=4)
        with io.open('out.json', 'w', encoding='utf-8') as out:
            out.write( unicode(json.dumps(dict_obj, sort_keys=True, indent=4)) )
            
    print "END"
        
if __name__ == '__main__':
    main()    
