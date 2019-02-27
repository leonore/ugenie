from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import elastic

class UtterFunctionality(Action):
    def name(self):
        return "action_utter_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "Here are some things you can ask me about:"
        buttons = []
        buttons.append({'title': 'Short courses',
            'payload': '/ask_short_courses_functionality'},
            {'title': 'Postgraduate courses',
            'payload': '/ask_admissions_courses_functionality'},
            {'title': 'Terminology',
            'payload': '/ask_terminology_functionality'}
            )
        dispatcher.utter_button_message(response, buttons)
        return

# Asks the user to confirm the course
class CheckCourse(Action):
    def name(self):
        return "action_check_course"

    def run(self, dispatcher, tracker, domain):
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))
        response = "Did you want the course: " + str(elastic_title).title() + "? (yes/no)"
        dispatcher.utter_message(response)
        return

# Apologises if the chat-bot returns the incorrect courses
# For now it just says could you please rephrase but possible in the future it could give alternative suggestions
class CourseDenied(Action):
    def name(self):
        return "action_course_denied"

    def run(self, dispatcher, tracker, domain):
        response = "Sorry I did not understand, could you please rephrase the question."
        dispatcher.utter_message(response)
        return

## IN WORK ##
# Sends the answer to common acronym questions
# e.g. "what does FT stand for"
class GetAcronym(Action):
    def name(self):
        return "action_get_acronym"

    def run(self, dispatcher, tracker, domain):
        response = elastic.get_description(tracker.get_slot("course"))
        dispatcher.utter_message(response)
        return

# Utters the cost of a course
class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):
        # elastic_title = title of the course from the database
        # elastic_cat = course category e.g. short course / admissions courses
        # elastic_score = the score of how relevant the course was to the elastic search
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))
        if elastic_cat == "SC":
            elastic_output, elastic_score = elastic.get_sc_field(elastic_title, "Cost")
            response = str(elastic_title).title() + " costs £" + str(elastic_output) + "."
        elif elastic_cat == "AD":
            elastic_output = elastic.get_ad_fees(elastic_title)
            response = str(elastic_output)

        dispatcher.utter_message(response)
        return

# Utters the description of a course or tells the description of a term used
class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        # If there is a string in the 'acronym' slot, assume the user is asking about terminology
        # Else assume the user is asking about a course
        if tracker.get_slot("acronym") != None:
            elastic_topic, elastic_desc = elastic.get_description( tracker.get_slot("acronym"))
        else:
            elastic_topic, elastic_desc = elastic.get_description(tracker.get_slot("course"))

        if elastic_topic:
            response = str(elastic_desc)
        else:
            response = "Sorry, I could not find any details for that"

        # Used to clear the acronym slot in the tracker
        dispatcher.utter_message(response)
        return [SlotSet("acronym", None)]

# Utters time related information to do with a course
# e.g. start time, year
class GetTime(Action):
    def name(self):
        return "action_get_time"

    def run(self, dispatcher, tracker, domain):
        # elastic_title = title of the course from the database
        # elastic_cat = course category e.g. short course / admissions courses
        # elastic_score = the score of how relevant the course was to the elastic search
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        if elastic_cat == "SC":
            elastic_output = elastic.get_sc_times(elastic_title)
            response = str(elastic_output)
        elif elastic_cat == "AD":
            elastic_output = elastic.get_ad_times(elastic_title)
            response = str(elastic_output)
        else:
            response = "Sorry, I could not find the information for times for this course"

        dispatcher.utter_message(response)
        return

## IN WORK ##
# Utters the tutor for a course
class GetTutor(Action):
    def name(self):
        return "action_get_tutor"

    def run(self, dispatcher, tracker, domain):
        # elastic_title = title of the course from the database
        # elastic_cat = course category e.g. short course / admissions courses
        # elastic_score = the score of how relevant the course was to the elastic search
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        # The short-courses file tells the tutor for each class taught,
        # Although we do not know tutor information for the admissions courses so cannot return it
        if elastic_cat == "SC":
            elastic_output, elastic_score = elastic.get_sc_field(tracker.get_slot("course"), "Tutor")
            response = "The tutor for " + str(elastic_title).title() + " is: " + str(elastic_output) + "."
        elif elastic_output == "AD":
            response = "Sorry, I do not know who teaches " + str(elastic_title).title()
        else:
            response = "Sorry, I could not find the tutor for " + str(elastic_title).title()

        dispatcher.utter_message(response)
        return

## IN WORK ##
# Utters the requirements to get into a course
class GetRequirements(Action):
    def name(self):
        return "action_get_requirements"

    def run(self, dispatcher, tracker, domain):
        try:
            elastic_title = get_admission_requirements(tracker.get_slot("course"))
        except:
            response = "Sorry, I could not find any course with that name."
        elastic_output = elastic.get_admission_requirements(tracker.get_slot("course"), tracker.get_slot("requirement"))
        if elastic_output:
            response = "The admission requirements are " + elastic_output
        elif elastic_output is False:
            response = "Sorry, I did not understand the requirements you meant"
        else:
            response = "We do not have any requirements for that course"
        return response

# Utters a list of courses the tutor in question teaches
# e.g. "what classes does Sam Cook teach"
class GetTutorCourses(Action):
    def name(self):
        return "action_get_tutor_courses"

    def run(self, dispatcher, tracker, domain):
        # elastic_tutor = the name of the tutor according to the database
        # elastic_output is the list of courses they teach
        elastic_tutor, elastic_output = elastic.get_tutor_courses(tracker.get_slot("tutor"))

        if elastic_output:
            response = str(elastic_tutor) + " teaches: " + str(elastic_output)
        else:
            response = "Sorry, I could not find any courses with that tutor"

        dispatcher.utter_message(response)
        return

class GetSCClassTypes(Action):
    def name(self):
        return "action_get_sc_type_classes"

    def run(self, dispatcher, tracker, domain):
        elastic_output, elastic_length = elastic.get_sc_type_courses(tracker.get_slot("course"))

        if elastic_output:
            response = "I have found " + elastic_length + " classes: " + elastic_output
        else:
            response = "Sorry, I could not find any courses"
        dispatcher.utter_message(response)
        return

class GetADClassTypes(Action):
    def name(self):
        return "action_get__ad_type_classes"

    def run(self, dispatcher, tracker, domain):
        elastic_output, elastic_length = elastic.get_ad_type_courses(tracker.get_slot("course"))

        if elastic_output:
            response = "I have found " + elastic_length + " classes: " + elastic_output
        else:
            response = "Sorry, I could not find any courses"
        dispatcher.utter_message(response)
        return
