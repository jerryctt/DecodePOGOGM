#!/bin/sh
fileName=$1
java -cp pokemongo-game-master.jar com.pokebattler.gamemaster.GenerateJSON $fileName "${fileName}.json"
