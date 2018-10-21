#!/usr/bin/env python

import json, sys, re, os, struct, os.path, io
import glob

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
#        sys.stderr.write('%02x' % ord(key[-1]))

 #   sys.stderr.write('\n')

    size = os.path.getsize(inFile) - 37
    if size <= 0:
        sys.stderr.write("Error: %s is too short\n" % inFile)
        return False
    elif (size & 0x0F) != 0:
        # AES-128 => block of 128 bits (16 bytes)
        sys.stderr.write("Warning: unexpected size for encrypted data in %s\n" % path)

    with open(inFile, 'rb') as input:
        version = struct.unpack('B', input.read(1))[0]
        if version != 1:
            sys.stderr.write("Error: invalid version number for %s (%d)\n" % (inFile, version))
            return False

        iv = input.read(16)

        cipher = AES.new(key, AES.MODE_CBC, iv)
        raw = input.read(size)
        
        ## Add padding~
        size = len(raw)
#        print 'The size is ' + str(size)
 #       print 'The raw size is ' + str(len(raw))
        paddinglen = ((size+15)%16)+1
  #      print 'The padding size is %d'%(paddinglen)
        if paddinglen > 0 and paddinglen < 16:
            raw = raw[:-paddinglen]
   #         print 'The new raw size is ' + str(len(raw))
            
        data = cipher.decrypt(raw)


    # FIXME: sanitize bundle_name!
    with open(outFile, 'wb') as out:
        out.write(data)
    print outFile + ' Finish'
    return True   
    
def readAdFile(adFileName):    
    # Read MOVE name
    with io.open(adFileName, encoding='utf-8') as aData:
        ad = json.load( aData )['digest']
        adItems = []
        for item in ad:                    
            bundleName = item['bundleName']
            if not 'i18n' in bundleName:
                continue
            adItems.append( item )
        return adItems
        
    return None
 
def findFileBySize(path, size):
    allFiles = os.listdir( path )
    for name in allFiles:
        fullName = path + name
        statinfo = os.stat(fullName)
        if statinfo.st_size == size:
            return fullName
    return None
    
       
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('decode.py [ad_json_file_name] [bundle_directory]')
        sys.exit(0)
    adItems = readAdFile(sys.argv[1])
    
    # Find the file
    for name in adItems:
        fullName = findFileBySize( sys.argv[2], name['size'] )
        if fullName == None:
            #print 'Cannot find %s' % name['bundleName']
            continue
        decrypt_file( name['key'], fullName, name['bundleName']+'.txt' )
    #decrypt_file()    
        