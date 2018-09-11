#!/usr/bin/env python

import json, sys, re, os, struct, os.path

import binascii
import struct
from base64 import *
from Crypto.Cipher import AES

def decrypt_file(fileKey, inFile, outFile):
    # File structure:
    #   VERSION (1 byte)
    #   IV (16 bytes)
    #   DATA
    #   TRAILER (20 bytes)

    key_mask = '\x50\x46\x41\x69\x24\x3B\x5D\x47\x37\x52\x67\x3E\x6B\x7A\x34\x77'
    net_key = b64decode( fileKey )
    key = ''
    for i in range(0, 16):
        key += chr(ord(net_key[i]) ^ ord(key_mask[i]))
        sys.stderr.write('%02x' % ord(key[-1]))

    sys.stderr.write('\n')

    size = os.path.getsize('d') - 37
    if size <= 0:
        sys.stderr.write("Error: %s is too short\n" % path)
        return False
    elif (size & 0x0F) != 0:
        # AES-128 => block of 128 bits (16 bytes)
        sys.stderr.write("Warning: unexpected size for encrypted data in %s\n" % path)

    with open(inFile, 'rb') as input:
        version = struct.unpack('B', input.read(1))[0]
        if version != 1:
            sys.stderr.write("Error: invalid version number for %s (%d)\n" % (path, version))
            return False

        iv = input.read(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        data = cipher.decrypt(input.read(size))


    # FIXME: sanitize bundle_name!
    with open(outFile, 'wb') as out:
        out.write(data)
    
    return True   
    
def readAdFile(adFileName):    
    # Read MOVE name
    with io.open(adFileName, encoding='utf-8') as aData:
        ad = json.load( aData )
        adItems = []
        for item in ad:        
            bundleName = item['bundleName']
            if bundleName != 'i18n_moves' and bundleName != 'i18n_pokemon':
                continue
            adItems.append( item )
        return adItems
        
    return None
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('decode.py [ad_json_file_name] [bundle_directory]')
        sys.exit(0)
    adItems = readAdFile(sys.argv[1])
    
    # Find the file
    #decrypt_file()    
        