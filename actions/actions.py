# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideSolution(Action):

    def name(self) -> Text:
        return "action_provide_solution"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extracting the user's message
        user_message = tracker.latest_message.get('text', '').lower()

        # Defining a mapping of error messages to solutions
        solutions = {
            "outofmemoryerror": "Increase the heap size in your Java settings to resolve the OutOfMemoryError.",
            "memory leak": "Check your code for unused objects and ensure garbage collection is working properly.",
            "disk full": "Free up space on the disk or increase disk storage to avoid the 'Disk Full' error.",
            "timeout": "Try increasing the timeout settings in your application or server configuration."
        }

        # Determine the appropriate solution
        solution = "I'm sorry, I don't have a solution for that error at the moment."
        for error_key in solutions:
            if error_key in user_message:
                solution = solutions[error_key]
                break

        # Sending the solution back to the user
        dispatcher.utter_message(text=solution)

        return []


