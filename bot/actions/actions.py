# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

import requests

class ActionTeste(Action):
    def name(self) -> Text:
        return "action_teste"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        try:
            dispatcher.utter_message("Mensagem enviada por uma custom action.")
        except ValueError:
            dispatcher.utter_message(ValueError)
        return []


class ActionCPF(Action):
    def name(self) -> Text:
        return "action_cpf"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        cpf = tracker.get_slot('cpf')

        try:
            dispatcher.utter_message("O seu CPF é {}?".format(cpf))
        except ValueError:
            dispatcher.utter_message(ValueError)
        return [SlotSet("cpf", cpf)]

class ActionBotsBrasil(Action):
    def name(self) -> Text:
        return "action_bots_brasil"

    def run(self, dispatcher, tracker, domain):
        req_conferencia = requests.request('GET', "https://significado.herokuapp.com/conferencia")
        req_robo = requests.request('GET', "https://significado.herokuapp.com/robo")
        req_chat = requests.request('GET', "https://significado.herokuapp.com/chat")

        msg_conferencia = req_conferencia.json()[0]["meanings"][2]
        msg_robo = req_robo.json()[0]["meanings"][0]
        msg_chat = req_chat.json()[0]["meanings"][0]

        try:
            dispatcher.utter_message("Conferência: {}\n".format(msg_conferencia))
            dispatcher.utter_message("Robô: {}\n".format(msg_robo))
            dispatcher.utter_message("Chat: {}\n".format(msg_chat))
        except ValueError:
            dispatcher.utter_message(ValueError)
        return[]