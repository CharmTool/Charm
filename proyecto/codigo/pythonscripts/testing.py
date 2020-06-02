from testPhrasesGenerator import *
from os import listdir
from os.path import isfile, join
import timeit

def noMutationTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

	dirFunction = "NoMutated"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return 
def mutateUttTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


	dirFunction = "MutateChar"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return 

def mutateWithDistanceUttTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "MutateCharWithDistance"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return 

def deleteCharsTest(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "deleteChars"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)	
	return 

def traductionChained(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "traductionChained"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)

	return

def randomTraductionChained(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	dirFunction = "randomTraductionChained"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)

	return

def changeNumberToWord(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "changeNumberToWord"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)

	return

def changeWordToNumber(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "changeWordToNumber"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return

#def activeToPassive():
#	functions = [mutateUtterance, mutateUtteranceWithDistances, traductionChained, randomTraductionChained, changeNumberToWord, changeWordToNumber, 
#				activeToPassive, convertAdjectivesToSynonyms, convertAdjectivesToAntonyms, convertObjectsToSynonyms, "noMutation"]
#
#	distributionAux = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
#
#	for percentage in range(10, 41, 10):
#		for variability in range(-5, 6, 5):
#			extension = "_mutateWithDistance_{0}_{1}.utterances.txt".format(percentage, variability)
#			print(extension)
#			parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0]]
#			generateUtterances(functions, distributionAux, parameters, extension)
#	return
#
def convertAdjectivesToSynonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

	dirFunction = "convertAdjectivesToSynonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def convertAdjectivesToAntonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]

	dirFunction = "convertAdjectivesToAntonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def convertObjectsToSynonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
	dirFunction = "convertObjectsToSynonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	
	return

	return

def convertAdverbsToSynonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

	dirFunction = "convertAdverbsToSynonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def convertAdverbsToAntonyms(chatbot):
	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]

	dirFunction = "convertAdverbsToAntonyms"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 0, 0, ["de", "pl", "zh"], 3, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def mixedTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0.05, 0.05, 0.05, 0.25, 0.25, 0.05, 0.05, 0, 0.05, 0.05, 0.05, 0.05, 0.05, 0]

	dirFunction = "distributed"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return



def sturdinessTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0, 0.3, 0.3, 0, 0, 0.2, 0.2, 0, 0, 0, 0, 0, 0, 0]

	dirFunction = "sturdinessTest"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def intentTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0, 0, 0, 0.3, 0.45, 0, 0, 0, 0.05, 0.05, 0.05, 0.05, 0.05, 0]

	dirFunction = "intentTest"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def coherenceTest(chatbot):

	functions = ["mutateUtterance", "mutateUtteranceWithDistances", "deleteChars", "traductionChained", "randomTraductionChained", "changeNumberToWord", "changeWordToNumber", 
				"activeToPassive", "convertAdjectivesToSynonyms", "convertAdjectivesToAntonyms", "convertObjectsToSynonyms", "convertAdverbsToSynonyms", "convertAdverbsToAntonyms", "noMutation"]

	#We are going to give different distributions of the functions to test the chatbot.
	# Traduction 
	distributionAux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

	dirFunction = "coherenceTest"
	extension = ".utterances.txt"
	parameters = [keyboardQWERTYSpanish, 3, 0, ["de", "pl", "zh"], 2, [0], 50]
	generateUtterances(functions, chatbot, dirFunction, distributionAux, parameters, extension)
	return

def gridTest():

	#chatbots = ([f for f in listdir("../convosGen")])
	chatbots = ["Miso-Test", "viberSampleNutrition", "RoomReservation"]
	startExec = timeit.timeit()
	for chatbot in chatbots:

		statsDir = "/home/sergio/Desktop/proyecto/codigo/output/{}/mutateUtteranceStats.txt".format(chatbot)
		if exists(statsDir):
			remove(statsDir)
#		start1 = timeit.timeit()
#		mutateUttTest(chatbot)
#		end1 = timeit.timeit()
#		print("\n mutateTime for ", chatbot, ": ",(end1 - start1))
		
		statsDir = "/home/sergio/Desktop/proyecto/codigo/output/{}/mutateUtteranceWithDistancesStats.txt".format(chatbot)
		if exists(statsDir):
			remove(statsDir)
#		start2 = timeit.timeit()
##		mutateWithDistanceUttTest(chatbot)
#		end2 = timeit.timeit()
#		print("\n mutateWithDistanceTime for ", chatbot, ": ",(end2 - start2))
		
		statsDir = "/home/sergio/Desktop/proyecto/codigo/output/{}/deleteCharsStats.txt".format(chatbot)
		if exists(statsDir):
			remove(statsDir)

		sturdinessTest(chatbot)
		intentTest(chatbot)
		coherenceTest(chatbot)

#		start3 = timeit.timeit()
#		deleteCharsTest(chatbot)
#		end3 = timeit.timeit()
#		print("\n deleteCharsTest for ", chatbot, ": ",(end3 - start3))

#		start4 = timeit.timeit()
#		traductionChained(chatbot)
#		end4 = timeit.timeit()
#		print("\n traductionChained for ", chatbot, ": ",(end4 - start4))
#
#		start5 = timeit.timeit()
#		randomTraductionChained(chatbot)
#		end5 = timeit.timeit()
#		print("\n randomTraductionChained for ", chatbot, ": ",(end5 - start5))
#
#		start6 = timeit.timeit()
#		changeNumberToWord(chatbot)
#		end6 = timeit.timeit()
#		print("\n changeNumberToWord for ", chatbot, ": ",(end6 - start6))
#
#		start7 = timeit.timeit()
#		changeWordToNumber(chatbot)
#		end7 = timeit.timeit()
#		print("\n changeWordToNumber for ", chatbot, ": ",(end7 - start7))
#
#		start8 = timeit.timeit()
#		convertAdjectivesToSynonyms(chatbot)
#		end8 = timeit.timeit()
#		print("\n convertAdjectivesToSynonyms for ", chatbot, ": ",(end8 - start8))
#
#		start9 = timeit.timeit()
#		convertAdjectivesToAntonyms(chatbot)
#		end9 = timeit.timeit()
#		print("\n convertAdjectivesToAntonyms for ", chatbot, ": ",(end9 - start9))
#
#		start10 = timeit.timeit()
#		convertObjectsToSynonyms(chatbot)
#		end10 = timeit.timeit()
#		print("\n convertObjectsToSynonyms for ", chatbot, ": ",(end10 - start10))
#
#		start11 = timeit.timeit()
#		convertAdverbsToSynonyms(chatbot)
#		end11 = timeit.timeit()
#		print("\n convertAdverbsToSynonyms for ", chatbot, ": ",(end11 - start11))
#
#		start12 = timeit.timeit()
#		convertAdverbsToAntonyms(chatbot)
#		end12 = timeit.timeit()
#		print("\n convertAdverbsToAntonyms for ", chatbot, ": ",(end12 - start12))
#
#		start13 = timeit.timeit()
#		noMutationTest(chatbot)
#		end13 = timeit.timeit()
#		print("\n noMutationTest for ", chatbot, ": ",(end13 - start13))
	endExec = timeit.timeit()
	print("\n total exec time: ", chatbot, ": ",(endExec - startExec))

if __name__ == "__main__":

	gridTest()



	