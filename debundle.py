#!/usr/bin/env python
import os
import sys
import json
import unitypack
from unitypack.asset import Asset
from unitypack.object import ObjectPointer

def main():
    with open(sys.argv[1], "rb") as f:
        bundle = unitypack.load(f)

        for asset in bundle.assets:
            for id, obj in asset.objects.items():
                d = obj.read()
                if not d.get('m_Name') or (d.get('m_Name') != 'merged' and d.get('m_Name') != 'patch') or not d.get('Table'):
                    continue
                    
                table = d.get('Table')
                
       #         print( json.dumps( table, ensure_ascii=False, sort_keys=True, indent=4 ) )
                with io.open( sys.argv[1]+'.json', 'w', encoding='utf8') as fw:
                    fw.write( unicode(json.dumps(allitem, ensure_ascii=False, sort_keys=True, indent=4)) )

#                for item in table:
 #                   print( json.dumps( item ) )
            print('\n\n\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('debundle.py bundle_file_name')
        sys.exit(0)
    main()