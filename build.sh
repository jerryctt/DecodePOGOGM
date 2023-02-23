#!/binsh
rm -rf pokemongo-game-master
git clone --depth=1 https://github.com/pokemongo-dev-contrib/pokemongo-game-master.git
patch pokemongo-game-master/pom.xml < add_shade_plugin.patch
cd pokemongo-game-master
libPath=`find ./lib/*.jar -type f`
mvn install:install-file -Dfile="$libPath"
mvn package -Dmaven.test.skip=true
cd ..
jarPath=`find ./pokemongo-game-master/target/pokemongo-*.jar -type f`
cp "$jarPath" pokemongo-game-master.jar
