#!/bin/sh

declare -a seds=("s/jieglaofkne/move/" 
								 "s/cljkadnpeee/pokemonType/" 
								 "s/ihlflpjllel/type1/" 
								 "s/mmmmpblkndo/type2/" 
								 "s/fpjbenmjnpo/stats/" 
								 "s/bkpaapbdbnc/baseStamina/"
          			 "s/pmbigpiicml/baseAttack/"
          			 "s/lgchfdobkck/baseDefense/"
          			 "s/gigaliikfhd/quickMoves/"
          			 "s/npjmeogkkbb/evolution/"
          			 "s/plpfkcbghme/evolutionBranch/"
          			 "s/oondagaanbp/candyCost/"
          			 "s/HKBIOBDALMG_//"
          			 "s/kapffmmbapl/cinematicMoves/"
          			 "s/lgkbfambbod/evolutionMega/"
          			 "s/lgkbfambbod/evolutionMega/"
          			 "s/bakhocpfeef/form/"
								 )

for name in "${seds[@]}"
do
    sed -i '' "$name" $1
done

