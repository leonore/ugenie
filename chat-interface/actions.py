from rasa_core_sdk import Action

import elastic

class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):
        elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Cost")
        print("Elastic output: ", elastic_output)
        response = "The cost of " + tracker.get_slot("course") + " is £" + str(elastic_output)
        dispatcher.utter_message(response)
        return 

class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Course description")
        print("Elastic output: ", elastic_output)
        response = "The description for " + tracker.get_slot("course") + " is: " + str(elastic_output)
        dispatcher.utter_message(response)
        return 
