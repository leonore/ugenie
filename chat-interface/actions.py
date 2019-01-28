from rasa_core_sdk import Action

import elastic

class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Cost")
            response = tracker.get_slot("course") + " costs £" + str(elastic_output) + "."
        except:
            response = "Sorry, I couldn't find any course fees for " + tracker.get_slot("course") + "."
        
        dispatcher.utter_message(response)
        return 

class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Course description")
            response = "The description for " + tracker.get_slot("course") + " is: " + str(elastic_output) + "."
        except:
            response = "Sorry, I couldn't find any description for " + tracker.get_slot("course") + "."
            
        dispatcher.utter_message(response)
        return 
