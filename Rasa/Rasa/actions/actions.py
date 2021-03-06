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

from inspect import Attribute
from re import L
from typing import Text, List, Any, Dict
from xml.sax.xmlreader import AttributesImpl
from matplotlib.pyplot import subplots_adjust

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

from rasa_sdk.events import SlotSet

def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        name = clean_name(slot_value)
        if len(name) == 0:
            dispatcher.utter_message(text="That must've been a typo.")
            return {"first_name": None}
        return {"first_name": name}

class ValidateAnswer(FormValidationAction):

    def number(self) -> Text:
        return "validate_number_form"
    
    def validate_number(
        self,
        slot_value: Any,
        dispacher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text,Any]:
        """Validate 'number' value."""


        num1 = tracker.get_slot(number)
        num2 = tracker.get_slot(number_1)




"""
class SeparateByAge(FormValidationAction):

    def age(self) -> Text:
        return "validate_age_form"

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        Validate `age` value.

        # If the person is under 17 = questionario 1 / else = questionario 2
        age = slot_value
        if age < 17:
            dispatcher.utter_message(text="User is 17 or under")
            return SlotSet("age", "under_17")
        else:
            return SlotSet("age", "above_17")


"""

class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        #load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("info.json")

        knowledge_base.set_representation_function_of_object(
            "pais", lambda obj: obj["country"] + " (" + obj["info"] + ")" )

        super().__init__(knowledge_base)
        

    