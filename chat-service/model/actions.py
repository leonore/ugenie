from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


import elastic

# asks the user to confirm the course
class CheckCourse(Action):
    def name(self):
        return "action_check_course"

    def run(self, dispatcher, tracker, domain):
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))
        response = "Did you want the course: " + str(elastic_title).title() + "? (yes/no)"
        dispatcher.utter_message(response)
        return

class CourseDenied(Action):
    def name(self):
        return "action_course_denied"

    def run(self, dispatcher, tracker, domain):
        response = "Sorry I did not understand, could you please rephrase the question."
        dispatcher.utter_message(response)
        return


# IN working
#  sends the answer to common acronym questions
class GetAcronym(Action):
    def name(self):
        return "action_get_acronym"

    def run(self, dispatcher, tracker, domain):
        response = elastic.get_description(tracker.get_slot("course"))
        dispatcher.utter_message(response)
        return

# utters the cost of a course
class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):

        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))
        if elastic_cat == "SC":
            elastic_output, elastic_score = elastic.get_sc_field(elastic_title, "Cost")
            response = str(elastic_title).title() + " costs £" + str(elastic_output) + "."
        elif elastic_cat == "AD":
            elastic_output = elastic.get_ad_fees(elastic_title)
            response = str(elastic_output)



        dispatcher.utter_message(response)
        return

        # # elastic_title = get_sc_title(tracker.get_slot("course"))
        # try:
        #     elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Cost")
        #     response = str(elastic_title) + " costs £" + str(elastic_output) + "."
        # except:
        #     response = "Sorry, I couldn't find any course fees for " + str(elastic_title) + "."
        #
        # dispatcher.utter_message(response)
        # return

# utters the description of a course or tells the description of a term used
class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):

        if tracker.get_slot("acronym") != None:
            elastic_topic, elastic_desc = elastic.get_description( tracker.get_slot("acronym"))
        else:
         #tracker.get_slot("course") != None:
            elastic_topic, elastic_desc = elastic.get_description(tracker.get_slot("course"))


        if elastic_topic:
            response = str(elastic_desc)
        else:
            response = "Sorry, I could not find any details for that"

        dispatcher.utter_message(response)

        # if elastic_cat == "SC":
        #     elastic_title = elastic.get
        #     elastic_output = elastic.get_sc_field(elastic_title, "Course description")
        #     response = "The description for " + str(elastic_title) + " is: " + str(elastic_output) + "."
        # elif elastic_cat == "AD":
        #     elastic_output = elastic.get_ad_description(elastic_title)
        #     response = str(elastic_output)
        # else:
        #     response = "Sorry, I couldn't find any description for that course."

        # Used to clear the acronym slot in the tracker
        return [SlotSet("acronym", None)]

# utters time related information to do with a course (e.g. start time, year)
class GetTime(Action):
    def name(self):
        return "action_get_time"

    def run(self, dispatcher, tracker, domain):
        # dispatcher.utter_message("Get Time: ")
        # dispatcher.utter_message("Get Time2: ")
        #
        # try:
        #     dispatcher.utter_message("Try: ")
        #     elastic_title = get_course_title(tracker.get_slot("course"))
        # except:
        #     dispatcher.utter_message("Except: ")
        #     response = "Sorry :("

        print("A Get Time")
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        if elastic_cat == "SC":
            elastic_output = elastic.get_sc_times(elastic_title)
            response = str(elastic_output)
        elif elastic_cat == "AD":
            elastic_output = elastic.get_ad_times(elastic_title)
            response = str(elastic_output)
        else:
            response = "Sorry, I could not find the information for times for this course"

        # try:
        #     elastic_output = elastic.get_ad_times(tracker.get_slot("course"))
        #     response = str(elastic_output)
        # except:
        #     response = "Sorry, I could not find any times for " + str(elastic_title) + "."
        #
        # dispatcher.utter_message("Time Out: ")
        # response = "Course Time : "

        dispatcher.utter_message(response)
        return

# IN WORK
# utters the tutor for a course
class GetTutor(Action):
    def name(self):
        return "action_get_tutor"

    def run(self, dispatcher, tracker, domain):

        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        if elastic_cat == "SC":
            elastic_output, elastic_score = elastic.get_sc_field(tracker.get_slot("course"), "Tutor")
            response = "The tutor for " + str(elastic_title).title() + " is: " + str(elastic_output) + "."
        elif elastic_output == "AD":
            response = "Sorry, I do not know who teaches " + str(elastic_title).title()
        else:
            response = "Sorry, I could not find the tutor for " + str(elastic_title).title()

        dispatcher.utter_message(response)
        return

# IN WORK
# utters the requirements to get into a course
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
