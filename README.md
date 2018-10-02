# Decode POGO GameMaster/AssetDigest

This utility cloud convert binary game master file and asset digest file of PokemonGO to readable json file. The protobuf is from `https://github.com/Furtif/POGOProtos.git`. 

You just simple run  

`sh ./run.sh`

This utility will decode gm.bin to out.json and ad.bin to ad.json in default. 

# Decode UnityFS file from encrypted folder
`python decode.py ad.json ./bundles/`

# Decode UnityFS file to plain resource file
`unityextract --all i18n_moves.txt`. 


**Remember: The version of python is 3.6.6**
