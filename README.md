# Charm
Charm  is an open source software tool to test chatbot over Botium

## How to use it
In this guide I am going to explain how to use Charm tool to get your convos and mutate them so you can test your chatbot freely.

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
5. Once you completed the steps, you can generate your convo files by executing the following command from the folder *pythonscripts*:
```
python3 generateDialogConvos.py
```
