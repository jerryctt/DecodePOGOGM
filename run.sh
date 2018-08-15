#!/bin/bash
echo Clone POGO Proto
git clone https://github.com/Furtif/POGOProtos.git protos > /dev/null 2>&1
cd protos
echo Compile protobuf file for python
python compile.py python > /dev/null 2>&1
cd ..
VAR="$PWD"
rm -rf $VAR/pogoprotos
mv $VAR/protos/out/pogoprotos $VAR/pogoprotos
rm -rf protos
# Begin to convert file
export PYTHONPATH=.
cp pogoprotos/networking/responses/__init__.py pogoprotos/
cp pogoprotos/networking/responses/__init__.py pogoprotos/networking/

# Convert Game Master file
if [ -f "gm.bin" ]
then
echo Convert gm.bin to out.json
python convert.py
else
echo Cannot file gm.bin to convert
fi

# Convert Asset Digest file
if [ -f "ad.bin" ]
then
echo Convert ad.bin to ad.json
python asset_convert.py
else
echo Cannot file ad.bin to convert
fi