#from rasa_core.actions.action import Action

from rasa_core_sdk import Action

class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):
        print("Checking Fees...")
        return "Checking Fees..."

class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        print("Checking Description...")
        return "Checking Description..."
