from rasa_core_sdk import Action

import elastic

class GetAcronym(Action):
    def name(self):
        return "action_get_acronym"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_acronym, elastic_output = elastic.get_acronym_answer("question")
            response = str(elastic_output)
        except:
            response = "Sorry, I couldn't find any answer for " + str(elastic_acronym) + "."

        dispatcher.utter_message(response)
        return

class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_title, elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Cost")
            response = str(elastic_title) + " costs £" + str(elastic_output) + "."
        except:
            response = "Sorry, I couldn't find any course fees for " + str(elastic_title) + "."

        dispatcher.utter_message(response)
        return

class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_title, elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Course description")
            response = "The description for " + str(elastic_title) + " is: " + str(elastic_output) + "."
        except:
            response = "Sorry, I couldn't find any description for " + str(elastic_title) + "."

        dispatcher.utter_message(response)
        return

class GetTime(Action):
    def name(self):
        return "action_get_time"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_title, elastic_output = elastic.get_sc_times(tracker.get_slot("course"))
            response = str(elastic_output)
        except:
            response = "Sorry, I could not find any times for " + str(elastic_title) + "."

        dispatcher.utter_message(response)
        return

class GetTutor(Action):
    def name(self):
        return "action_get_tutor"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_title, elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Tutor")
            response = "The tutor for " + str(elastic_title) + " is: " + str(elastic_output) + "."
        except:
            response = "Sorry, I could not find the tutor for " + str(elastic_title) + "."

        dispatcher.utter_message(response)
        return
