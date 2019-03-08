from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import elastic

## DISCLAIMER: at the moment this isn't what's used for actions
# I'm not sure we will have to use it this way, as it works from templates
# and it makes more sense for me this way
# - Leo
class UtterFunctionality(Action):
    def name(self):
        return "action_utter_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "Here are some things you can ask me about:"
        buttons = [{'title': 'Short courses',
            'payload': '/ask_short_courses_functionality'},
            {'title': 'Postgraduate courses',
            'payload': '/ask_admissions_courses_functionality'},
            {'title': 'Terminology',
            'payload': '/ask_terminology_functionality'}]
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

# Sends the answer to common acronym questions
# e.g. "what does FT stand for"
class GetAcronym(Action):
    def name(self):
        return "action_get_acronym"

    def run(self, dispatcher, tracker, domain):
        response = elastic.get_description(tracker.get_slot("acronym"))
        # response format: (acronym, answer)
        dispatcher.utter_message(response[1])
        return


# Utters the description of a course or tells the description of a term used
class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        # If there is a string in the 'acronym' slot, assume the user is asking about terminology
        # Else assume the user is asking about a course
        if tracker.get_slot("acronym") != None:
            elastic_topic, elastic_desc = elastic.get_description(tracker.get_slot("acronym"))
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

# Utters the IELTS requirements to get into a course
class GetIELTSRequirements(Action):
    def name(self):
        return "action_get_ielts_requirements"

    def run(self, dispatcher, tracker, domain):
        elastic_output = elastic.get_admission_requirements(tracker.get_slot("course"), "IELTS Requirements")
        if elastic_output == "course_not_found":
            response = "Sorry, I could not find a course with that name."
        elif elastic_output:
            response = "The admission requirements are " + elastic_output
        else:
            response = "This course does not seem to have any IELTS requirement specified."

        dispatcher.utter_message(response)
        return

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

# Returns a list of up to 10 courses that match the user's choice of relevnacy
# e.g. what art courses are there / what spanish courses are there
class GetClassTypes(Action):
    def name(self):
        return "action_get_type_classes"

    def run(self, dispatcher, tracker, domain):
        # If the user is currently asking about short courses, we will only look for relevant short courses
        if tracker.get_slot("course_type") == "short":
            elastic_output, elastic_length = elastic.get_sc_type_courses(tracker.get_slot("course"))
            if elastic_output:
                response = "These are some of the short classes which I have found : " + elastic_output
            else:
                response = "Sorry, I could not find any short courses in that subject area"
            dispatcher.utter_message(response)

        # If the user is currently asking about post graduate courses, we will only look for relevant post graduate courses
        elif tracker.get_slot("course_type") == "admissions":
            elastic_output, elastic_length = elastic.get_ad_type_courses(tracker.get_slot("course"))
            if elastic_output:
                response = "These are some of the post-graduate classes which I have found : " + elastic_output
            else:
                response = "Sorry, I could not find any post-graduate courses in that subject area"
            dispatcher.utter_message(response)

        # If the user has not specified already which course type they want we ask them to clarify with the use of buttons
        elif not (tracker.get_slot("course_type")):
            response = "Did you want..."
            buttons = [{"title":"Short Courses", "payload":"/ask_set_sc_course_type"},
                        {"title":"Post Graduate", "payload":"/ask_set_ad_course_type"}]
            dispatcher.utter_button_message(response, buttons)
        else:
            response = "Sorry, I did not understand"
            dispatcher.utter_message(response)
        return

# Sets the slot for coure_type to short
class SetSCCourseType(Action):
    def name(self):
        return "action_set_sc_course_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("course_type", "short")]

# Sets the slot for coure_type to admissions
class SetADCourseType(Action):
    def name(self):
        return "action_set_ad_course_type"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("course_type", "admissions")]

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

class UtterSCFunctionality(Action):
    def name(self):
        return "action_utter_short_courses_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "You can ask me about course times, tutors, credits, fees, descriptions!"
        dispatcher.utter_message(response)
        return [SlotSet("course_type", "short")]

class UtterADFunctionality(Action):
    def name(self):
        return "action_utter_admissions_courses_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "You can ask me about fees, requirements, and a brief course description!"
        dispatcher.utter_message(response)
        return [SlotSet("course_type", "admissions")]
