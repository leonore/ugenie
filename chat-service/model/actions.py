from rasa_core_sdk import Action

from actions import elastic

# IN working
#  sends the answer to common acronym questions
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

# utters the cost of a course
class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):

        elastic_title, elastic_cat = elastic.get_course_title(tracker.get_slot("course"))
        if elastic_cat == "SC":
            elastic_output = elastic.get_sc_field(elastic_title, "Cost")
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

# utters the description of a course
class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Get Fee:")

        elastic_title, elastic_cat = elastic.get_course_title(tracker.get_slot("course"))
        if elastic_cat == "SC":
            elastic_output = elastic.get_sc_field(elastic_title, "Course description")
            response = "The description for " + str(elastic_title) + " is: " + str(elastic_output) + "."
        elif elastic_cat == "AD":
            elastic_output = elastic.get_ad_description(elastic_title)
            response = str(elastic_output)
        else:
            response = "Sorry, I couldn't find any description for that course."

        dispatcher.utter_message(response)
        return

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
        elastic_title, elastic_cat = elastic.get_course_title(tracker.get_slot("course"))

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
        try:
            elastic_title = get_sc_title(tracker.get_slot("course"))
        except:
            response = "Sorry, I could not find any course called " + str(tracker.get_slot("course")) + "."

        try:
            elastic_output = elastic.get_sc_field(tracker.get_slot("course"), "Tutor")
            response = "The tutor for " + str(elastic_title) + " is: " + str(elastic_output) + "."
        except:
            response = "Sorry, I could not find the tutor for " + str(elastic_title) + "."

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
