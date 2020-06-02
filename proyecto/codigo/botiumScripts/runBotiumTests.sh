#!/bin/bash
#DesktopPath=/home/sergio/Escritorio #en el trabajo 
DesktopPath=/home/sergio/Desktop #en casa

testPath=${DesktopPath}/botium

OUTPUTPATH=${DesktopPath}/proyecto/codigo/output

genConvosPath=${DesktopPath}/proyecto/codigo/mutatedConvos

mkdir -p ${OUTPUTPATH}
#cat /dev/null > ${OUTPUTPATH}/totalresults/mutate_output_results.txt
#cat /dev/null > ${OUTPUTPATH}/totalresults/mutateWithDistance_output_results.txt
##
### for traduction chained
#cat /dev/null > ${OUTPUTPATH}/totalresults/traductionChained_output_results.txt
#cat /dev/null > ${OUTPUTPATH}/totalresults/randomTraductionChained_output_results.txt

# Por alguna razon falla al hacer el cat archivo > botiumarchivo

#declare -A hashmap

#hashmap["key"]="value"

#hashmap["key2"]="value2"

#echo "${hashmap["key"]}"

#for key in ${!hashmap[@]}; do echo $key; done

#for value in ${hashmap[@]}; do echo $value; done

#echo hashmap has ${#hashmap[@]} elements

chatbots=('Miso-Test' 'viberSampleNutrition' 'RoomReservation')

for chatbot in "${chatbots[@]}";
	do
	export BOTIUM_CONVOS=$testPath/${chatbot}/convos
	export BOTIUM_CONFIG=$testPath/${chatbot}/botium.json
	#------------------NoMutation-------------------------------------------------------------------

	outputAux="${OUTPUTPATH}/${chatbot}"
	mkdir -p outputAux
	mkdir -p ${outputAux}/totalresults
#	#Test Cases for noMutation

	methods=('coherenceTest' 'sturdinessTest' 'intentTest')
#	methods=('intentTest')

	for method in "${methods[@]}";
		do
		carpeta="${genConvosPath}/${chatbot}/${method}"
		echo "find ${testPath}/${chatbot}/convos/ -mindepth 1 ! -regex '^${testPath}/${chatbot}/convos/convoFiles\(/.*\)?' -delete"
		find ${testPath}/${chatbot}/convos/ -mindepth 1 ! -regex '^'${testPath}/${chatbot}/convos/convoFiles'\(/.*\)?' -delete
		echo "directorio entrada"
		echo "$carpeta"
		echo "directorio salida"
		echo "${testPath}/${chatbot}/convos"
		echo "cp -R ${carpeta} ${testPath}/${chatbot}/convos" 
		cp -R $carpeta "${testPath}/${chatbot}/convos" 

		# Tienen que estar creadas las carpetas
		mutationKind="_traductionChained"
		output="${outputAux}/${chatbot}_${method}.txt"

		if test -f "$output"; then
			echo "already tested"
		else
			botium-cli run | cat > $output
		fi

	done;
#
#	if [ "$chatbot" == "misoBot" ]; then 
#		echo "misoBot"
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/noMutation_output_results.txt
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		echo "ViberNutrition"
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/noMutation_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/noMutation_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/noMutation_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/noMutation_output_results.txt 1

	# Tests for mutation ---------------------------------------
	#---------------------------------------------------------------------------------------

#	for per in `seq 5 10 26`; 
#		do
#			for var in `seq -5 5 6`; 
#				do
#					((i=i+1))
#					#Test Cases for mutate
#					for intentName in "${convosIntents[@]}";
#						do
#						archivo="${genConvosPath}/${chatbot}/${intentName}_mutate_${per}_${var}.utterances.txt"
#						cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#					done;
#					output="${outputAux}/mutate_output_${per}_${var}.txt"
#					if test -f "$output"; then
#						echo "already tested"
#					else
#						botium-cli run | cat > $output
#					fi
#
#					if [ "$chatbot" == "misoBot" ]; then 
#						awk 'NR >= 38&& NR<=39 {print $1;}' $output >> ${outputAux}/totalresults/mutate_output_results.txt
#						awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/mutate_output_${per}_${var}_results.txt						
#					elif [ "$chatbot" == "ViberNutrition" ]; then
#						awk 'NR >= 53&& NR<=54 {print $1;}' $output >> ${outputAux}/totalresults/mutate_output_results.txt
#						awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/mutate_output_${per}_${var}_results.txt
#					elif [ "$chatbot" == "veterinary" ]; then
#						awk 'NR >= 49&& NR<=50 {print $1;}' $output >> ${outputAux}/totalresults/mutate_output_results.txt
#						awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/mutate_output_${per}_${var}_results.txt						
#					elif [ "$chatbot" == "attendance" ]; then
#						awk 'NR >= 22&& NR<=23 {print $1;}' $output >> ${outputAux}/totalresults/mutate_output_results.txt
#						awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/mutate_output_${per}_${var}_results.txt							
#					fi
#					python3 plotGraphs.py ${outputAux}/totalresults/mutate_output_${per}_${var}_results.txt $i
#	        done;
#	done;     		
#	# IMPARES, PASSED TESTS
#	awk 'NR%2==1 {total += $1}END{ print total }' ${outputAux}/totalresults/mutate_output_results.txt > ${outputAux}/totalresults/mutate_output_Totalresults.txt
#	# PARES, FAILED TESTS 
#	awk 'NR%2==0 {total += $1}END{ print total }' ${outputAux}/totalresults/mutate_output_results.txt >> ${outputAux}/totalresults/mutate_output_Totalresults.txt
#
#	python3 plotGraphs.py ${outputAux}/totalresults/mutate_output_Totalresults.txt $i
#
##	#------------------------------------------------------------
##	#------------------------- mutateWithDistance----------------
#
#	i=0
#	for per in `seq 5 10 26`; 
#		do
#			for var in `seq -5 5 6`; 
#				do
#					((i=i+1))
#	        		#Test Cases for mutateWithDistance
#	        		for intentName in "${convosIntents[@]}";
#						do
#						archivo="${genConvosPath}/${chatbot}/${intentName}_mutateWithDistance_${per}_${var}.utterances.txt"
#						cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#					done;
#					output="${outputAux}/mutateWithDistance_output_${per}_${var}.txt"
#					if test -f "$output"; then
#						echo "already tested"
#					else
#						botium-cli run | cat > $output
#					fi
#					if [ "$chatbot" == "misoBot" ]; then 
#						awk 'NR >= 38&& NR<=39 {print $1;}' $output >> ${outputAux}/totalresults/mutateWithDistance_output_results.txt
#						awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/mutateWithDistance_output_${per}_${var}_results.txt						
#					elif [ "$chatbot" == "ViberNutrition" ]; then
#						awk 'NR >= 53&& NR<=54 {print $1;}' $output >> ${outputAux}/totalresults/mutateWithDistance_output_results.txt
#						awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/mutateWithDistance_output_${per}_${var}_results.txt
#					elif [ "$chatbot" == "veterinary" ]; then
#						awk 'NR >= 49&& NR<=50 {print $1;}' $output >> ${outputAux}/totalresults/mutateWithDistance_output_results.txt
#						awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/mutateWithDistance_output_${per}_${var}_results.txt 
#					elif [ "$chatbot" == "attendance" ]; then
#						awk 'NR >= 22&& NR<=23 {print $1;}' $output >> ${outputAux}/totalresults/mutateWithDistance_output_results.txt
#						awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/mutateWithDistance_output_${per}_${var}_results.txt 
#					fi
#		
#					python3 plotGraphs.py ${outputAux}/totalresults/mutateWithDistance_output_${per}_${var}_results.txt $i
#	
#        	done;
#	done;
#	# IMPARES, PASSED TESTS
#	awk 'NR%2==1 {total += $1}END{ print total }' ${outputAux}/totalresults/mutateWithDistance_output_results.txt > ${outputAux}/totalresults/mutateWithDistance_output_Totalresults.txt
#	# PARES, FAILED TESTS 
#	awk 'NR%2==0 {total += $1}END{ print total }' ${outputAux}/totalresults/mutateWithDistance_output_results.txt >> ${outputAux}/totalresults/mutateWithDistance_output_Totalresults.txt
#
#	python3 plotGraphs.py ${outputAux}/totalresults/mutateWithDistance_output_Totalresults.txt $i
#
#	#------------------------------------------------------------
#	#------------------------- deleteChars----------------
#
#	i=0
#	for per in `seq 5 10 26`; 
#		do
#			for var in `seq -5 5 6`; 
#				do
#					((i=i+1))
#	        		#Test Cases for mutateWithDistance
#	        		for intentName in "${convosIntents[@]}";
#						do
#						archivo="${genConvosPath}/${chatbot}/${intentName}_deleteChars_${per}_${var}.utterances.txt"
#						cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#					done;
#					output="${outputAux}/deleteChars_output_${per}_${var}.txt"
#					if test -f "$output"; then
#						echo "already tested"
#					else
#						botium-cli run | cat > $output
#					fi
#					if [ "$chatbot" == "misoBot" ]; then 
#						awk 'NR >= 38&& NR<=39 {print $1;}' $output >> ${outputAux}/totalresults/deleteChars_output_results.txt
#						awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/deleteChars_output_${per}_${var}_results.txt					
#					elif [ "$chatbot" == "ViberNutrition" ]; then
#						awk 'NR >= 53&& NR<=54 {print $1;}' $output >> ${outputAux}/totalresults/deleteChars_output_results.txt
#						awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/deleteChars_output_${per}_${var}_results.txt
#					elif [ "$chatbot" == "veterinary" ]; then
#						awk 'NR >= 49&& NR<=50 {print $1;}' $output >> ${outputAux}/totalresults/deleteChars_output_results.txt
#						awk 'NR >= 49&& NR<=50 {print $1;}'	$output > ${outputAux}/totalresults/deleteChars_output_${per}_${var}_results.txt		
#					elif [ "$chatbot" == "attendance" ]; then
#						awk 'NR >= 22&& NR<=23 {print $1;}' $output >> ${outputAux}/totalresults/deleteChars_output_results.txt
#						awk 'NR >= 22&& NR<=23 {print $1;}'	$output > ${outputAux}/totalresults/deleteChars_output_${per}_${var}_results.txt	
#					fi
#					
#					python3 plotGraphs.py ${outputAux}/totalresults/deleteChars_output_${per}_${var}_results.txt $i
#	
#        	done;
#	done;
#	# IMPARES, PASSED TESTS
#	awk 'NR%2==1 {total += $1}END{ print total }' ${outputAux}/totalresults/deleteChars_output_results.txt > ${outputAux}/totalresults/deleteChars_output_Totalresults.txt
#	# PARES, FAILED TESTS 
#	awk 'NR%2==0 {total += $1}END{ print total }' ${outputAux}/totalresults/deleteChars_output_results.txt >> ${outputAux}/totalresults/deleteChars_output_Totalresults.txt
#
#	python3 plotGraphs.py ${outputAux}/totalresults/deleteChars_output_Totalresults.txt $i
#
#	#----------------------------------------------------------------------
#	#----------------------traductionChained--------------------------
#
#	#Test Cases for traductionChained
#	for intentName in "${convosIntents[@]}";
#		do
#		archivo="${genConvosPath}/${chatbot}/${intentName}_traductionChained.utterances.txt"
#		cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#	done;
#	output="${outputAux}/traductionChained_output.txt"
#	if test -f "$output"; then
#		echo "already tested"
#	else
#		botium-cli run | cat > $output
#	fi
#	if [ "$chatbot" == "misoBot" ]; then 
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/traductionChained_output_results.txt					
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/traductionChained_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/traductionChained_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/traductionChained_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/traductionChained_output_results.txt 1
#	
#	
#	#---------------------------------------------------------------------------
#	#----------------Test Cases for randomTraductionChained---------------------
#
#	i=0
#	for nLan in `seq 2 1 4`; 
#		do
#			for intentName in "${convosIntents[@]}";
#				do
#				archivo="${genConvosPath}/${chatbot}/${intentName}_randomTraductionChained_${nLan}.utterances.txt"
#				cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#			done;
#			output="${outputAux}/randomTraductionChained_output_${nLan}.txt"
#			if test -f "$output"; then
#				echo "already tested"
#			else
#				botium-cli run | cat > $output
#			fi
#			if [ "$chatbot" == "misoBot" ]; then 
#				awk 'NR >= 38&& NR<=39 {print $1;}' $output >> ${outputAux}/totalresults/randomTraductionChained_output_results.txt				
#				awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/randomTraductionChained_output_${nLan}_results.txt					
#			elif [ "$chatbot" == "ViberNutrition" ]; then
#				awk 'NR >= 53&& NR<=54 {print $1;}' $output >> ${outputAux}/totalresults/randomTraductionChained_output_results.txt
#				awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/randomTraductionChained_output_${nLan}_results.txt
#			elif [ "$chatbot" == "veterinary" ]; then
#				awk 'NR >= 49&& NR<=50 {print $1;}' $output >> ${outputAux}/totalresults/randomTraductionChained_output_results.txt
#				awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/randomTraductionChained_output_${nLan}_results.txt
#			elif [ "$chatbot" == "attendance" ]; then
#				awk 'NR >= 22&& NR<=23 {print $1;}' $output >> ${outputAux}/totalresults/randomTraductionChained_output_results.txt
#				awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/randomTraductionChained_output_${nLan}_results.txt
#			fi
#
#			python3 plotGraphs.py ${outputAux}/totalresults/randomTraductionChained_output_${nLan}_results.txt $i
#	
#		done;
#	# IMPARES, PASSED TESTS
#	awk 'NR%2==1 {total += $1}END{ print total }' ${outputAux}/totalresults/randomTraductionChained_output_results.txt > ${outputAuxoutputAux}/totalresults/randomTraductionChained_output_Totalresults.txt
#	# PARES, FAILED TESTS 
#	awk 'NR%2==0 {total += $1}END{ print total }' ${outputAux}/totalresults/randomTraductionChained_output_results.txt >> ${outputAuxoutputAux}/totalresults/randomTraductionChained_output_Totalresults.txt
#
#	python3 plotGraphs.py ${outputAuxoutputAux}/totalresults/randomTraductionChained_output_Totalresults.txt $i
#
#	#----------------------changeNumberToWord--------------------------
#
#	#Test Cases for changeNumberToWord
#	for intentName in "${convosIntents[@]}";
#		do
#			archivo="${genConvosPath}/${chatbot}/${intentName}_changeNumberToWord.utterances.txt"
#			cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#	done;
#	output="${outputAux}/changeNumberToWord_output.txt"
#	if test -f "$output"; then
#		echo "already tested"
#	else
#		botium-cli run | cat > $output
#	fi
#	if [ "$chatbot" == "misoBot" ]; then 
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/changeNumberToWord_output_results.txt					
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/changeNumberToWord_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/changeNumberToWord_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/changeNumberToWord_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/changeNumberToWord_output_results.txt 1
#	
#
#	#---------------------------------------------------------------------------
#	#----------------------changeWordToNumber--------------------------
#
#	#Test Cases for traductionChained
#	for intentName in "${convosIntents[@]}";
#		do
#			archivo="${genConvosPath}/${chatbot}/${intentName}_changeWordToNumber.utterances.txt"
#			cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#	done;
#	output="${outputAux}/changeWordToNumber_output.txt"
#	if test -f "$output"; then
#		echo "already tested"
#	else
#		botium-cli run | cat > $output
#	fi
#	if [ "$chatbot" == "misoBot" ]; then 
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/changeWordToNumber_output_results.txt					
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/changeWordToNumber_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/changeWordToNumber_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/changeWordToNumber_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/changeWordToNumber_output_results.txt 1
#	
#
#	#---------------------------------------------------------------------------
#	#----------------------convertAdjectivesToSynonyms--------------------------
#
#	#Test Cases for traductionChained
#	for intentName in "${convosIntents[@]}";
#		do
#			archivo="${genConvosPath}/${chatbot}/${intentName}_convertAdjectivesToSynonyms.utterances.txt"
#			cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#	done;
#	output="${outputAux}/convertAdjectivesToSynonyms_output.txt"
#	if test -f "$output"; then
#		echo "already tested"
#	else
#		botium-cli run | cat > $output
#	fi
#	if [ "$chatbot" == "misoBot" ]; then 
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToSynonyms_output_results.txt					
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToSynonyms_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToSynonyms_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToSynonyms_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/convertAdjectivesToSynonyms_output_results.txt 1
#
#	#---------------------------------------------------------------------------
#	#----------------------convertAdjectivesToAntonyms--------------------------
#
#	#Test Cases for traductionChained
#	for intentName in "${convosIntents[@]}";
#		do
#			archivo="${genConvosPath}/${chatbot}/${intentName}_convertAdjectivesToAntonyms.utterances.txt"
#			cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#	done;
#	output="${outputAux}/convertAdjectivesToAntonyms_output.txt"
#	if test -f "$output"; then
#		echo "already tested"
#	else
#		botium-cli run | cat > $output
#	fi
#	if [ "$chatbot" == "misoBot" ]; then 
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToAntonyms_output_results.txt					
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToAntonyms_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToAntonyms_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/convertAdjectivesToAntonyms_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/convertAdjectivesToAntonyms_output_results.txt 1
#	
#	#--------------------------------------------------------------------------------
#	
#	#----------------------convertObjectsToSynonyms--------------------------
#
#	#Test Cases for traductionChained
#	for intentName in "${convosIntents[@]}";
#		do
#			archivo="${genConvosPath}/${chatbot}/${intentName}_convertObjectsToSynonyms.utterances.txt"
#			cat $archivo > "${testPath}/${chatbot}/convos/${intentName}.utterances.txt" 
#	done;
#	output="${outputAux}/convertObjectsToSynonyms_output.txt"
#	if test -f "$output"; then
#		echo "already tested"
#	else
#		botium-cli run | cat > $output
#	fi
#	if [ "$chatbot" == "misoBot" ]; then 
#		awk 'NR >= 38&& NR<=39 {print $1;}' $output > ${outputAux}/totalresults/convertObjectsToSynonyms_output_results.txt					
#	elif [ "$chatbot" == "ViberNutrition" ]; then
#		awk 'NR >= 53&& NR<=54 {print $1;}' $output > ${outputAux}/totalresults/convertObjectsToSynonyms_output_results.txt
#	elif [ "$chatbot" == "veterinary" ]; then
#		awk 'NR >= 49&& NR<=50 {print $1;}' $output > ${outputAux}/totalresults/convertObjectsToSynonyms_output_results.txt
#	elif [ "$chatbot" == "attendance" ]; then
#		awk 'NR >= 22&& NR<=23 {print $1;}' $output > ${outputAux}/totalresults/convertObjectsToSynonyms_output_results.txt
#	fi
#	python3 plotGraphs.py ${outputAux}/totalresults/convertObjectsToSynonyms_output_results.txt 1
#
#	#--------------------------------------------------------------------------------
done;