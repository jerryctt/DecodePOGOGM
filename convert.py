#!/usr/bin/env python

import io
import json
import sys

from pogoprotos.networking.responses.download_item_templates_response_pb2 import DownloadItemTemplatesResponse
from google.protobuf.json_format import MessageToDict

def main(gmfile):
    with open(gmfile, 'rb') as gm:
        msg = DownloadItemTemplatesResponse()
        msg.ParseFromString( gm.read() )
        dict_obj = MessageToDict(msg)
        #print json.dumps(dict_obj, sort_keys=True, indent=4)
        with io.open( gmfile+'.json', 'w', encoding='utf-8') as out:
            out.write( unicode(json.dumps(dict_obj, sort_keys=True, indent=4)) )
            
    print "END"
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('convert.py GAME_MASTER_FLIE_BIN')
        sys.exit(0)

    main(sys.argv[1])    
