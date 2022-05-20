# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#

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
from tokenize import Number
from typing import Text, List, Any, Dict
from xml.sax.xmlreader import AttributesImpl

from rasa_sdk import Tracker, FormValidationAction, ValidationAction
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
        

class ValidateAnswer(ValidationAction):

    def number(self) -> Text:
        return "validate_number_form"
    
    def validate_number(
        self,
        slot_value: Any,
        dispacher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Number,Any]:
        """Validate 'number' value."""


        ptsdnumbers = {}

        ptsdnumbers['num1'] = tracker.get_slot("number")
        ptsdnumbers['num2'] = tracker.get_slot("number_1")
        ptsdnumbers['num3'] = tracker.get_slot("number_2")
        ptsdnumbers['num4'] = tracker.get_slot("number_3")
        ptsdnumbers['num5'] = tracker.get_slot("number_4")
        ptsdnumbers['num6'] = tracker.get_slot("number_5")
        ptsdnumbers['num7'] = tracker.get_slot("number_6")
        ptsdnumbers['num8'] = tracker.get_slot("number_7")
        ptsdnumbers['num9'] = tracker.get_slot("number_8")
        ptsdnumbers['num10'] = tracker.get_slot("number_9")
        ptsdnumbers['num11'] = tracker.get_slot("number_10")
        ptsdnumbers['num12'] = tracker.get_slot("number_11")
        ptsdnumbers['num13'] = tracker.get_slot("number_12")
        ptsdnumbers['num14'] = tracker.get_slot("number_13")
        ptsdnumbers['num15'] = tracker.get_slot("number_14")
        ptsdnumbers['num16'] = tracker.get_slot("number_15")
        ptsdnumbers['num17'] = tracker.get_slot("number_16")
        ptsdnumbers['num18'] = tracker.get_slot("number_17")
        ptsdnumbers['num19'] = tracker.get_slot("number_18")
        ptsdnumbers['num20'] = tracker.get_slot("number_19")

       
        Total = sum(ptsdnumbers)

        print(Total)

        return {"total": Total}



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
        

    