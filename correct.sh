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
          			 "s/kapffmmbapl/cinematicMoves/"
          			 "s/lgkbfambbod/evolutionMega/"
          			 "s/lgkbfambbod/evolutionMega/"
          			 "s/bakhocpfeef/form/"
          			 "s/lakkjnlnilh/templateId/"
          			 "s/mcfbihcdgcd/avatarCustomization/"
          			 "s/fefchiopepb/enabled/"
          			 "s/ofaneehdcfm/pokemon/"
          			 "s/mbjoiddjeel/power/"
          			 "s/lnedebomjpc/durationMs/"
          			 "s/laoipfmolig/energyDelta/"
          			 "s/nlblfchdopm/uniqueId/"
          			 "s/jdhnbnniigm/type1/"
          			 "s/jiljhhplbbk/type2/"
          			 "s/omknjfkkhcc/firstEvoCost/"
          			 "s/ppcjfelhblj/EvoCost/"
          			 "s/kgfmliagkid/evoUniqueId/"
          			 "s/ahmjloaldjc/evoUniqueId/"
          			 "s/HKBIOBDALMG_POKEMON_TYPE_/POKEMON_TYPE_/"
								 )

for name in "${seds[@]}"
do
    sed -i '' "$name" $1
done

