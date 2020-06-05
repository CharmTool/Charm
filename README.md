# Charm
Charm is an open source software tool to test chatbot over Botium. 
Botium is a complete tool that helps you test your chatbots by running a set of tests which consist on recreating conversations over your chatbot to test its behaviour. Botium will output the list of tests failed and passed, with a brief description for the errors occured. 
For a better understanding of Botium, you can visit their webpage https://www.botium.ai/
Charm tries to help Botium by generating better default tests cases using the chatbot training utterances defined previously and increasing the size of the tests set by muting the input utterances (or user requests).
If you want to have a detailed explanation of the project I invite you to read the following article. *(link to the article)*

## How to use it
In this guide I am going to explain how to use Charm tool to get your convos and mutate them so you can test your chatbot freely.

### Generate convos from dialogflow

1. To generate convo files you have to download the chatbot from Dialogflow.

2. You have to add manually all the system entities that are required in any of the chatbot intents.
   * To do so, find the folder entities inside the chatbot's folder. If there is not such a folder, create it.
   * Add a file called *entityName*.json which will contain the name of the entity and another file called *entityName*_entries_en.json that will contain the values of each entry of the entity
   * Here is an example:
   
   *duration.json*
   ~~~~  
   {
      "id": "485f8456-a40c-4dbe-a678-14be959e77d4",
      "name": "duration"
   }
   ~~~~  
   
   *duration_entries_en.json*
    
   ~~~~  
   [
      {
        "value": "duration",
        "synonyms": [
        "1 hour",
        "two hours",
        "2 days",
        "24 hours"
        ]
      }
    ]
    ~~~~
3. Modify the path to the chatbots in generateDialogConvos.py main method (at the bottom of the file).
4. You can also choose how many input utterances are going to be generated per intent. It will get randomly n training utterances from the definition of the chatbot. 
5. Once you completed the steps, you can generate your convo files by executing the following command from the folder *proyecto/pythonscripts*:
```
python3 generateDialogConvos.py
```

### Mutate convos

*proyecto/pythonscripts/testPhrasesGenerator.py* includes all the functions related with mutations. Each of the input utterances will be muted by a function chosen randomly over a distribution of probabilities for each function.
Follow the next steps to create a mutation input utterances set.
1. In *proyecto/pythonscripts/testing.py*, create a function with the following variables.
1.1. Functions: array with the name of the functions you want to use.
1.2. distributionAux: an array with the distribution of probabilities for the use of any of the functions of the array we created before.
1.3. dirFunction: name of the directory in which the mutated set will be writen.
1.4. extension: extension of the files, which in this case will be ("utterances.txt")
1.5. parameters: Some mutation methods have parameters that affect to the way they mutate the phrase. Set each of the values in this array. The array has the following order: [keyboardConfig, probability, variability, languagesArray, numLanguages, indexesToRemove, Probability of changing a word for its synonym or anthonym]
2. With all this setted, call the function generateUtterances from the library testPhrasesGenerator.py and the set will be created in the directory *proyecto/pythonscripts/mutatedConvos/"chatbotName"/"TestName"*
