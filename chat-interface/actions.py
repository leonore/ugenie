from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class CheckCourseFees(Action):
    def name(self):
        # type: () -> Text
        return "check_course_fees"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]

        course = tracker.get_slot('course')

        # THIS IS JUST AN EXAMPLE QUERY, REPLACE CODE WHEN NEW DB READY
        q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
        result = db.query(q)

        return [SlotSet("matches", result if result is not None else [])]
