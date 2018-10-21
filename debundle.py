#!/usr/bin/env python
import os
import sys
import json
import unitypack
from unitypack.asset import Asset
from unitypack.object import ObjectPointer

def main():
    with open('patch_i18n_chinesetraditional.txt', "rb") as f:
        bundle = unitypack.load(f)

        for asset in bundle.assets:
            for id, obj in asset.objects.items():
                d = obj.read()
                if not d.get('m_Name') or (d.get('m_Name') != 'merged' and d.get('m_Name') != 'patch') or not d.get('Table'):
                    continue
                    
                table = d.get('Table')
                for item in table:
                    for entry, v in item.items():
                        print( entry )
                        print( v )
            print('\n\n\n')

if __name__ == "__main__":
	main()