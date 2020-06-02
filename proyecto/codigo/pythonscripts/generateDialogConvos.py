from os import listdir, makedirs, remove
from os.path import isfile, join, exists, dirname, abspath
import json
from itertools import combinations, product
from random import choice, sample
from re import sub
from shutil import copy
from time import sleep

"""
We are going to try to get all the convos of a chatbot in order to get botium results

In order to do that we have to generate 3 types of files:
	
	1. convo files

	2. Utterance input files

	3. Utterance output files

First, We need to get all the entities of the chatbot and store them into a dictionary

Second, we need to create a dependency dictionary with the context dependencies between all the intents.

With the dict created, we can create the convo file of each intent (First the ones that have no dependency, 
	later the ones that depend directly from the ones menctioned before and so on)

It is important to have into acc that some of the intents have required entities, if so, we will divide the convo 
into different files (one for each required entity), following the paths that the intent can have  
		P.D. if there are more than two req ent, then it will ask for the first and then the second, 
		we can respond with both entities required at the same time
We can create a list of required random items and place them in the convo so it continues the flow of the conversation.

Problem, if any systemunit is required we have to define what is systemUnits (there is probably a library for that) 
	we can set a default value for each sys.arg or try to get a random value of the library each time we need it


"""

"""
getEntities obtiene el nombre y los valores de todas las entidades de un chatbot, de esta manera, luego podemos saber 
los entities para no mutarlos en las frases
"""
def getEntities(dirPath):	

	entityDict = {}

	entInfoFiles = [join(dirPath,f) for f in listdir(dirPath) if isfile(join(dirPath, f)) and not f[-16:-5] == '_entries_en']
	entValFiles = [join(dirPath,f) for f in listdir(dirPath) if isfile(join(dirPath, f)) and f[-16:-5] == '_entries_en']

	for entInfo in entInfoFiles:
		with open(entInfo) as file:
		    entInfoDict = json.load(file)

	for entVal in entValFiles:
		with open(entVal) as file:
			entValDict = json.load(file)
			entValName = entVal.split('/')[-1]
			entityDict[entValName[:-16]] = []
			for entValAux in entValDict:
				#print(entVal['synonyms'])
				entityDict[entValName[:-16]].append(entValAux['synonyms'])
			#for entVal in entValDict:
			#	entityDict[entInfoDict['name']].append(entVal['synonyms'])   

	return entityDict
	
"""
getIntents obtiene la información de los intents de un chatbot, se pueden obtener los contextos, parámetros respuestas....
"""
def getIntents(dirPath):
	
	intentDict = {}
	intInfoFiles = [join(dirPath,f) for f in listdir(dirPath) if isfile(join(dirPath, f)) and not f[-17:-5] == '_usersays_en']

	for intInfo in intInfoFiles:
		with open(intInfo) as file:		
			intInfoDict = json.load(file)
			#print(intInfoDict['name'].replace(' ', ''))
			intentDict[intInfoDict['name']] = intInfoDict

	return intentDict

def getIntentUtterances(dirPath, intent, nTrainingUtterances):

	utts = []
	intentUtteranceFiles = [join(dirPath,f) for f in listdir(dirPath) if isfile(join(dirPath, f)) and f[:-5] == intent+'_usersays_en']

	for intUtt in intentUtteranceFiles:
		with open(intUtt) as file:		
			intUttsDict = json.load(file)
			#print(intInfoDict['name'].replace(' ', ''))
			for utt in intUttsDict: 
				uttAux = []
				aliasList = []
				#print("\n*********************\n")
				for textInstance in utt['data']:
				#	print("\n\n________________________\n", textInstance)
					if "alias" in textInstance.keys():
				#		print(textInstance['alias'])
						aliasList.append(textInstance['alias'])
					uttAux.append(textInstance['text'])
				#print(("".join(uttAux), aliasList))
				utts.append(("".join(uttAux), aliasList))

	if nTrainingUtterances < len(utts):
		return sample(utts, nTrainingUtterances)
	else:
		return utts
	
def getEntitiesCombWords(entityDict):
	entityCombDict = {}
	def getCombWords(entityDictEntry):
		combinations = []
		for word in entityDictEntry:
			for synonym in word:
				nWords = len(synonym.split())

				if not nWords in combinations:
					combinations.append(nWords)
		return combinations
	for entityKey in entityDict.keys():
		entityCombDict[entityKey] = getCombWords(entityDict[entityKey])
	return entityCombDict

def writeEntityFile(directory, entityDict):
	print(directory)
	if not exists(directory):
		makedirs(directory)
	fileDir = join(directory, "entities.txt")	
	entityDictJson = json.dumps(entityDict)
	f=open(fileDir, "w+")
	f.write(entityDictJson)
	f.close()

"""
getDependancies obtiene las dependencias entre los intents, de esta manera luego podemos generar las conversaciones aplicando contexto. 

To do it we need to see if the intent we are going to check, has context and it has no parent id, if so, we need to check those intents which 
parents id is the id of the intent we are checking, and has the same contextname. If so, we can continue checking the sons of that intent and so on.

"""
def getDependencies(intentDict):

	#Recursivamente buscaremos cada contexto 
	def getDendenciesRec(intentDict, affectedContext):

		contextDependencyDict = {}

		for intentKey in intentDict.keys():
			# Si el contexto del intent coincide con el del argumento y la id del padre coincide con la pasada, dicho intent será contexto del anterior. 	
			#print("\n\n\n1.", affectedContext, intentDict[intentKey]['contexts'])
			if affectedContext in intentDict[intentKey]['contexts']:
				contextDependencyDict[intentKey] = []
				if intentDict[intentKey]['responses'][0]['affectedContexts']:
					for affectedContextsAux in intentDict[intentKey]['responses'][0]['affectedContexts']:
						#print("2.", affectedContextsAux)
						contextDependencyDict[intentKey].append(getDendenciesRec(intentDict, affectedContextsAux['name']))

		return contextDependencyDict

	dependenciesDict = {}

	for intentKey in intentDict.keys():
		if not 'parentId' in intentDict[intentKey].keys():
			# Vamos a ver si tienen contexto, si tienen contexto, miraremos para dicho intent, si alǵun otro intent le tiene de contexto
			#print("intent: ", intentKey, "contexto: ", intentDict[intentKey]['contexts'])
			dependenciesDict[intentKey] = []
			# Si existe contexto, buscaremos todos sus hijos y los colgaremos de dicho intent
			if 'affectedContexts' in intentDict[intentKey]['responses'][0].keys():
				for affectedContext in intentDict[intentKey]['responses'][0]['affectedContexts']:
					dependenciesDict[intentKey].append(getDendenciesRec(intentDict, affectedContext['name']))

	#print(intentDict)
	return dependenciesDict

def walkOverDependencies(intentDict, dependenciesDict, entityDict, entityCombDict, chatbot, nTrainingUtterances=0): #CORREGIR

	

	for intentParent in dependenciesDict.keys():
		generateConvos(intentDict, intentParent, entityDict, chatbot, nTrainingUtterances)
		if dependenciesDict[intentParent]:
			for dependency in dependenciesDict[intentParent]:
				walkOverDependencies(intentDict, dependency, entityDict, entityCombDict, chatbot, nTrainingUtterances)
		

	return
# we have to check if there is any required parameter. If so, divide the training phrases into 2 sets, 
# and treat them as two diferent convo files.

def generateConvos(intentDict, intent, entityDict, chatbot, nTrainingUtterances):

	def checkRequiredEntities(intentDict, intent):

		requiredParams = {}
		for parameter in intentDict[intent]['responses'][0]['parameters']:
			if parameter['required']:
				requiredParams[parameter['name']] = parameter
		return requiredParams

	def checkContext(intentDict, intent):
		if "parentId" in intentDict[intent].keys():
			return True
		return False 

	#print("\n", intentDict[intent]["name"])
	intentName = intentDict[intent]["name"]

	#Estas uterances están en forma de listas de listas de tuplas
	utterances = getIntentUtterances("/home/sergio/Desktop/chatbots/{}/intents".format(chatbot), intent, nTrainingUtterances)
	requiredParams = checkRequiredEntities(intentDict, intent)
	dirAux="../convosGen/{}".format(chatbot)
	if not exists(dirAux):
		makedirs(dirAux)
	#uttOutputFile= dirAux+"/"+intentName.replace(' ', '')+"_output.utterances.txt"
	splittedUtterances=[]
	i=0
	tokensRemoved = [' ', '_']

	if requiredParams:
		#Obtenemos las conversaciones parciales que nos servirán para aquellas frases que no cuenten con los parámetros requeridos.
		pconvosParams = getPConvosRequired(requiredParams, entityDict, intentName, dirAux)
		combConvos = getConvosCombinations(requiredParams)
		#print("\n*************************\n\n", combConvos)
		splittedUtterances = splitUtterances(combConvos, requiredParams, intentDict[intent], utterances, entityDict)
		#print(splittedUtterances)
		# para cada combinacion de parámetros que falten, haremos una conversación diferente en caso de que tengan utterances correspondientes. 
		# Si no hay se salta el proceso para dicha combinación

		#En caso de tener contexto, debemos asegurarnos de que el contexto contenga frases de entrenamiento, sino, este caso de prueba puede fallar

		for comb in combConvos:
			uttInputFile= dirAux+"/"+''.join(i for i in intentName if not i in tokensRemoved)+"_"+str(i)+"_input.utterances.txt"
			convoFile= dirAux+"/"+''.join(i for i in intentName if not i in tokensRemoved)+"_"+str(i)+".convo.txt"
			if splittedUtterances[str(comb)]:
				writeHeader(convoFile, intentName, str(i)) #Escribimos la cabecera del fichero
				# Vemos si existe contexto en la conversación
				if checkContext(intentDict, intent):
					#print("Tiene contexto")
					print("Caso 2 soy casen:", caseN)

					caseN = checkContextCase(intentDict, dirAux, intentDict[intent]["parentId"])
					writeInclude(convoFile, includeConvoFromContext(intentDict, intentDict[intent]["parentId"], str(caseN), chatbot))
				writeUserSentence(convoFile, intentName, str(i))
				for paramRequired in comb:
					writePConvos(convoFile, pconvosParams[paramRequired])
				writeBotResponse(convoFile, intentName)
				writeUttInputFile(uttInputFile, intentName, str(i), splittedUtterances[str(comb)])
				i += 1
				#print(comb, "\n")
				#print(pconvosParams[comb[0]], "\n")
				#print("\n",str(combConvos[0]))
			else: 
				writeNoTrainingPhrases(convoFile, intentName, str(i))
				i += 1
	else:
		i=0
	
		uttInputFile= dirAux+"/"+''.join(i for i in intentName if not i in tokensRemoved)+"_"+str(i)+"_input.utterances.txt"
		convoFile= dirAux+"/"+''.join(i for i in intentName if not i in tokensRemoved)+"_"+str(i)+".convo.txt"
		if utterances:
			writeHeader(convoFile, intentName, str(i)) #Escribimos la cabecera del fichero
			# Vemos si existe contexto en la conversación
			if checkContext(intentDict, intent):
				#print("Tiene contexto")
				caseN = checkContextCase(intentDict, dirAux, intentDict[intent]["parentId"])
				writeInclude(convoFile, includeConvoFromContext(intentDict, intentDict[intent]["parentId"], str(caseN), chatbot))
			writeUserSentence(convoFile, intentName, str(i))
			writeBotResponse(convoFile, intentName)
			writeUttInputFile(uttInputFile, intentName, str(i), utterances)
		else:
			writeNoTrainingPhrases(convoFile, intentName, str(i))
	
	uttOutputFile= dirAux+"/"+''.join(i for i in intentName if not i in tokensRemoved)+"_output.utterances.txt"

	outputUtterances = getOutputUtterances(intentDict[intent], entityCombDict)	
	writeOutputFile(uttOutputFile, intentName, outputUtterances)
	#print("________________________________________")
		#for reqParam in requiredParams:

		#	writeConvoFile(intentDict[intent]["name"], str(i))	
		#	i += 1
	# output ya con todos los requirements 
	# writeConvoFile(intentDict[intent]["name"], str(i))	

def splitUtterances(combConvos, requiredParams, intentEntry, utterances, entityDict):

	# Esta función será verdadera en caso de que los parámetros de utt sean aquellos que
	# están en requiredParams pero no en comb

	def checkUttInCombination(comb, utt, requiredParams):

		# En este bucle comprobamos que ningún parámetro de comb esté incluido en utt[1]
		for combParam in comb:
			if combParam in utt[1]:
				return False

		# En este bucle comprobamos que todos los parámetros (salvo los de comb) de requiredParams
		# están incluidos en utt[1]
		for combParam in comb:
			requiredParams.remove(combParam)
		for reqParam in requiredParams:
			if not reqParam in utt[1]:
				return False
		return True

	combinationsUtts = {}
	#print(combConvos)
	combConvos.append([])
	# Para cada combinación, se incluyen las utterances que correspondan.
	# Las combinaciones contienen los parámetros requeridos que se van a autocompletar, 
	# Luego para ser incluida la frase tiene que tener dichos parámetros y no los que faltan.

	for comb in combConvos:
		uttsComb = []
		#print("\n-----------", comb)
		for utt in utterances:
			if checkUttInCombination(comb, utt, list(requiredParams.keys())):
				#print(utt)
				uttsComb.append(utt)
				#uttAux.remove(utt)
		combinationsUtts[str(comb)] = uttsComb
	#print(combinationsUtts)

	return combinationsUtts

def includeConvoFromContext(intentDict, parentId, i, chatbot):

	tokensRemoved = [' ', '_']
	print("HOLA soi i",i)
	for intent in intentDict.keys():
		#print(intentDict[intent]['id'])
		#print(parentId)
		#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		if intentDict[intent]['id'] == parentId:
			file = "/home/sergio/Desktop/proyecto/codigo/convosGen/{}".format(chatbot)+"/" +''.join(i for i in intent if not i in tokensRemoved)+"_"+i+".convo.txt"
			print(file)
			f=open(file, "r")
			if f.mode == 'r':
				content=f.readlines()
			pconvo = content[1:]
			#pconvo = "\nINCLUDE " + intent.replace(' ', '')+"_"+i + "\n"
	return pconvo 

def checkContextCase(intentDict, dirAux, parentId):
	i = 0
	for intent in intentDict.keys():
		if intentDict[intent]['id'] == parentId:
			parentIntentName = intent
	print(parentIntentName)
	parentIntentConvos = [join(dirAux,f) for f in listdir(dirAux) if isfile(join(dirAux, f)) and f[:-12] == parentIntentName and f[-10:] == ".convo.txt"]
	parentIntentConvos.sort()
	for convoDir in parentIntentConvos:

		f=open(convoDir, "r")
		if f.mode == 'r':
			content=f.readlines()
		#If there is no convo in this file, we skip this one
		if content[0] == 'There are no training phrases for this case, please complete your training set':
			i+=1
		#Else, we return the numberr oof the case
		else:
			return i
	#if not utterances
	return -1
#	for case in splittedUtterances.keys():
#		
#		if splittedUtterances[case]:
#
#			print("Caso 000000")
#			print(i)
#			return i
#		print("\n\n\n\n\n\n\n\n", i)
#		i += 1
#	return -1

def getPConvosRequired(requiredParams, entityDict, intentName, dirAux):

	def getParamValue(reqParam, entityDict):

		#print(reqParam)
		if reqParam in entityDict:
			paramValue = choice(choice(entityDict[reqParam]))
			if paramValue[0] == "@":
				paramValue = getParamValue(paramValue[1:], entityDict)
		else:
			paramValue = "!REQUIRED_PARAMETER"

		return paramValue 

	pconvosParams = {}
	tokensRemoved = [' ', '_']
	intentNamecleared = ''.join(i for i in intentName if not i in tokensRemoved)
	for reqParam in requiredParams.keys():
		
		paramValue = getParamValue(reqParam, entityDict)
		
		reqParamHeader = intentNamecleared + reqParam
		writeReqParamPrompts(dirAux, reqParamHeader, requiredParams[reqParam]["prompts"])

		pconvosParams[reqParam] = "\n#bot\n"+reqParamHeader+"\nINTENT "+intentName+"\n\n#me\n"+paramValue+"\n"
		requiredParams[reqParam]["prompts"][0]["value"]

	return pconvosParams

def writeReqParamPrompts(dirAux, reqParamHeader, prompts):
	 
	tokensRemoved = [' ', '_']
	
	header=reqParamHeader+"\n"

	reqParamFilename=join(dirAux, reqParamHeader)
	reqParamFilename=reqParamFilename + ".utterances.txt"

	f=open(reqParamFilename, "w+")
	f.write(header)
	for prompt in prompts:
		f.write(prompt["value"]+"\n")

def getConvosCombinations(requiredParams):

	combConvos = []
	
	for L in range(0, len(requiredParams)+1):
	    for subset in combinations(requiredParams, L):
	        combConvos.append([x for x in subset if x != ","])
	return [x for x in combConvos if x != []]

"""
[[['$size0']], [['$snack0'], ['$snack0', '$snack1'], ['$snack0', '$snack1', '$snack2']], [['$deliverypickup0', '$deliverypickup1'], ['$deliverypickup0']]]

Las combinaciones posibles son:


"""

def getOutputVariablesCombinations(variablesCombinations):

	combOutputVariables = []
	
	for L in range(0, len(variablesCombinations)+1):
	    for subset in combinations(variablesCombinations, L):
	        combOutputVariables.append([x for x in subset if x != ","])
	return [x for x in combOutputVariables if x != []]


# 1. Comprobamos cuantas combinaciones de numero de palabras tiene como máximo la entidad a ver
# 2. Tenemos que hacer tantas frases como combinaciones posible haya 
#    entidad $drink (coffee, hot chocolate)
#	 ejemplo de respuesta: do you want $drink? tenemos que separar en: do you want $drink1? do you want $drink1 $drink2?

def getOutputUtterances(intentDictEntry, entityCombDict):

	def checkWordIsVar(word):
		if word[0] == '$':
			return True
		return False

	def checkVariables(word):
		
		if word[0] == '$':
			lenEntry = [len(key) for key in entityCombDict.keys() if key in word[0:]] # this works if entities names are only letters of the dictionary
			if len(lenEntry) == 1:
				combs = entityCombDict[word[1:lenEntry[0]+1]]
				#print(word[1:lenEntry[0]+1], "\n", combs)	
				
				combWords = []
				for comb in combs:
					words = []
					for i in range(0, comb):
						words.append('$'+sub('[\W_]+', '', word)+str(i))
					combWords.append(words)
				#print(combWords)
				return combWords
			else:
				#print(entityCombDict)
				print("hay diversas entradas que comparten la misma cadena para: ", word)
				return []
		else:
			return []

	# first we have to check all the combinations posibles


	outputUtterances = []
	for msg in intentDictEntry["responses"][0]["messages"]:
		if msg["type"] == 0:
			if isinstance(msg["speech"], list):
				for msgText in msg["speech"]:
					variablesCombinations = []
					msgText = msgText.split()
					for i, word in enumerate(msgText):
						listCombs = checkVariables(word)
						#print(listCombs)
						if listCombs:
							variablesCombinations.append(listCombs)

					# Now we have to make all possible combinations 
					#print("\n_____________________________________________________\n", variablesCombinations, "\n\n")


					variablesCombinations = list(product(*variablesCombinations))
					#if variablesCombinations:
					#	variablesCombinations = getOutputVariablesCombinations(variablesCombinations)
					if variablesCombinations:
						for varComb in variablesCombinations:
							nVar=0
							#
							(varComb)
							for i, word in enumerate(msgText):
								if checkWordIsVar(word):
									#
									(word, varComb[nVar])
									msgText[i] = ' '.join(varComb[nVar]) 
									nVar += 1
							outputUtterances.append(' '.join(msgText))

			else:
				outputUtterances.append(msg["speech"])

	return outputUtterances

def writeNoTrainingPhrases(convoFile, intentName, i):
	f=open(convoFile, "w+")
	f.write("There are no training phrases for this case, please complete your training set")

def writeHeader(convoFile, intentName, i):
	 
	tokensRemoved = [' ', '_']
	
	header=''.join(i for i in intentName if not i in tokensRemoved)+"_"+i+"\n"
	f=open(convoFile, "w+")
	f.write(header)

def writeInclude(convoFile, include):
	f=open(convoFile, "a")
	for line in include:
		f.write(line)

def writeUserSentence(convoFile, intentName, i):
	tokensRemoved = [' ', '_']
	convo="\n#me\n"+''.join(i for i in intentName if not i in tokensRemoved)+"_"+i+"_input\n"
	f=open(convoFile, "a")
	f.write(convo)

def writePConvos(convoFile, pcomb):
	f = open(convoFile, "a")
	f.write(pcomb)


def writeBotResponse(convoFile, intentName):
	tokensRemoved = [' ', '_']
	convo="\n#bot\n"+''.join(i for i in intentName if not i in tokensRemoved)+"_output\nINTENT "+intentName+"\n"
	f=open(convoFile, "a")
	f.write(convo)

def writeUttInputFile(uttFile, intentName, i, splittedUtterances):
	tokensRemoved = [' ', '_']
	header=''.join(i for i in intentName if not i in tokensRemoved)+"_"+i+"_input\n"
	f=open(uttFile, "w+")
	f.write(header)
	for utt in splittedUtterances:
		f.write(utt[0]+"\n")


def writeConvoFile(convoFile, intentName, i, header=False):

	tokensRemoved = [' ', '_']
	convo="\n#me\n"+''.join(i for i in intentName if not i in tokensRemoved)+"_"+i+"_input\n\n#bot\n"+''.join(i for i in intentName if not i in tokensRemoved)+"_output\n"
	f=open(convoFile, "a")
	f.write(convo)

def writeOutputFile(outputFile, intentName, outputUtterances):

	tokensRemoved = [' ', '_']
	header=''.join(i for i in intentName if not i in tokensRemoved)+"_output\n"
	f=open(outputFile, "w+")
	f.write(header)
	for utt in outputUtterances:

		f.write(utt+"\n")


def printDependencies(dependenciesDict):

	def printDependenciesRec(dependenciesDict, i):
		for dependency in dependenciesDict.keys():
			if i==0:
				print("i=0: ", dependency)
			elif i==1:
				print("\n\ti=1: ", dependency)
			elif i==2:
				print("\n\t\ti=2: ", dependency)
			elif i==3:
				print("\n\t\t\ti=3: ", dependency)
			else:
				print("\n\t\t\t\ti>3: ", dependency)
			for dependenciesDictAux in dependenciesDict[dependency]:
				printDependenciesRec(dependenciesDictAux, i+1)

	for dependency in dependenciesDict.keys():
		print("i=0: ", dependency)
		for dependenciesDictAux in dependenciesDict[dependency]:
			printDependenciesRec(dependenciesDictAux, 1)
		print("\n_____________________________________________________\n")

		

def separateConvosByIntents(dependenciesDict, convosDir, removeFiles):
	tokensRemoved = [' ', '_']

	def separateConvosByIntentsRec(dependenciesDict, intentDir, intentFiles):
		tokensRemoved = [' ', '_']

		for dependency in dependenciesDict.keys():
			newIntentDir=convosDir+"/"+''.join(i for i in dependency if not i in tokensRemoved)
			if not exists(newIntentDir):
				makedirs(newIntentDir)
			for f in intentFiles:
				copy(f, newIntentDir)
			removeFiles = [join(newIntentDir,f) for f in listdir(newIntentDir) if isfile(join(newIntentDir, f)) and f[-9:] == "convo.txt"]
			for f in removeFiles:
				remove(f)
 #			# 4. Copy all the input and output files into the intent Dir
			intentFiles = [join(convosDir,f) for f in listdir(convosDir) if isfile(join(convosDir, f)) and ''.join(i for i in dependency if not i in tokensRemoved)+"_" in f]
 #			#print(intentFiles, "\n")
			for f in intentFiles:
				copy(f, newIntentDir)
 #			# 5. keep running through the tree of dependencies
 			# Get all the files in the directory and pass them 
			intentFiles = [join(newIntentDir,f) for f in listdir(newIntentDir) if isfile(join(newIntentDir, f))]

			for dependenciesDictAux in dependenciesDict[dependency]:
				separateConvosByIntentsRec(dependenciesDictAux, newIntentDir, intentFiles)

	for dependency in dependenciesDict.keys():
		# 1. MAKE A DIRECTORY INSIDE WITH THE NAME OF THE INTENT
		intentDir = convosDir+"/"+''.join(i for i in dependency if not i in tokensRemoved)
		if not exists(intentDir):
			makedirs(intentDir)

		# 2. We copy the convos, inputs, and outputs starting with the same name to it
		intentFiles = [join(convosDir,f) for f in listdir(convosDir) if isfile(join(convosDir, f)) and ''.join(i for i in dependency if not i in tokensRemoved)+"_" in f]
		#print("\n________________________________________________________________\n\n", intentFiles)
		for f in intentFiles:
			copy(f, intentDir)
		# 3. We call the recursive with the kids of the root
		for dependenciesDictAux in dependenciesDict[dependency]:
			separateConvosByIntentsRec(dependenciesDictAux, intentDir, intentFiles)

	if removeFiles:
		intentFiles = [join(convosDir,f) for f in listdir(convosDir) if isfile(join(convosDir, f)) and f[-3:] == "txt"]
		for f in intentFiles:
			remove(f)


if __name__ == "__main__":

	chatbots = ["Miso-Test", "RoomReservation", "viberSampleNutrition"]
	nTrainingUtterances = [ 1000, 10, 1000 ]
	i=0

	for chatbot in chatbots:

		if chatbot == "Coffee-Shop":
			separateConvosByIntentsFlag = 0
		else:
			separateConvosByIntentsFlag = 0

		entityDir = "/home/sergio/Desktop/chatbots/{}/entities".format(chatbot)
		if exists(entityDir): 

			entityDict = getEntities(entityDir)
#			for key in entityDict.keys():
#				print(key, entityDict[key], "\n\n")
		else:
			entityDict = {}
			#getEntities("/home/sergio/Escritorio/chatbots/viberSampleNutrition/entities") fin de cuarentena
		#writeEntityFile("/home/sergio/Desktop/proyecto/codigo/convosGen/{}/entities".format(chatbot), entityDict)
		entityCombDict = getEntitiesCombWords(entityDict)
		#print(entityCombDict)

		intentDict = getIntents("/home/sergio/Desktop/chatbots/{}/intents".format(chatbot)) 
		#getIntents("/home/sergio/Escritorio/chatbots/viberSampleNutrition/intents") fin de cuarentena
		#for intent in intentDict.keys():
		#	print("\n\n\n\n", intentDict[intent])
		dependenciesDict = getDependencies(intentDict)

		printDependencies(dependenciesDict)

		walkOverDependencies(intentDict, dependenciesDict, entityDict, entityCombDict, chatbot, nTrainingUtterances[i])
		i += 1

		if separateConvosByIntentsFlag == 1:
			separateConvosByIntents(dependenciesDict, "/home/sergio/Desktop/proyecto/codigo/convosGen/{}".format(chatbot), True)
	