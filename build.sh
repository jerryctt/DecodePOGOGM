#!/binsh
rm -rf pokemongo-game-master
git clone https://github.com/pokemongo-dev-contrib/pokemongo-game-master.git
cd pokemongo-game-master
libPath=`find ./lib/*.jar -type f`
mvn install:install-file -Dfile="$libPath"
mvn package
