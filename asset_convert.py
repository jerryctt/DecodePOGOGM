#!/usr/bin/env python

import io
import json
from pogoprotos.networking.responses.get_asset_digest_response_pb2 import GetAssetDigestResponse
from google.protobuf.json_format import MessageToDict

def main():
    with open('ad.bin', 'rb') as gm:
        msg = GetAssetDigestResponse()
        msg.ParseFromString( gm.read() )
        dict_obj = MessageToDict(msg)
        #print json.dumps(dict_obj, sort_keys=True, indent=4)
        with io.open('ad.json', 'w', encoding='utf-8') as out:
            out.write( unicode(json.dumps(dict_obj, sort_keys=True, indent=4)) )
            
    print "END"
        
if __name__ == '__main__':
    main()    
