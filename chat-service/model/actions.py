from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

# data is gotten in elastic.py
# and processed into strings in actions.py
import elastic


# Offer functionality
class UtterFunctionality(Action):
    def name(self):
        return "action_utter_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "Here are some things you can ask me about..."
        buttons = [{"title": "Short courses", "payload": "/ask_short_courses_functionality"},
                   {"title": "Admissions", "payload": "/ask_admissions_courses_functionality"},
                   {"title": "Terminology", "payload": "/ask_terminology_functionality"},]

        dispatcher.utter_button_message(response, buttons)
        return


# utter short courses functionality and set the context
class UtterSCFunctionality(Action):
    def name(self):
        return "action_utter_short_courses_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "You can ask me about a course's time, location, tutors, fees, or a description!"
        dispatcher.utter_message(response)

        return [SlotSet("course_type", "short")]


# utter admissions functionality and set the context
class UtterADFunctionality(Action):
    def name(self):
        return "action_utter_admissions_courses_functionality"

    def run(self, dispatcher, tracker, domain):
        response = "You can ask me about a course's fees, English requirements, and whether it runs part-time or full-time!"
        dispatcher.utter_message(response)

        return [SlotSet("course_type", "admissions")]


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


# Offer more help
class UtterHelp(Action):
    def name(self):
        return "action_utter_help"

    def run(self, dispatcher, tracker, domain):
        response = "Is there anything else I can help you with?"
        buttons = [{"title": "Yes", "payload":"/confirmation"},
                   {"title": "No", "payload":"/denial"}]

        dispatcher.utter_button_message(response, buttons)
        return


# Offer redirection to a human
class UtterRedirect(Action):
    def name(self):
        return "action_utter_redirect"

    def run(self, dispatcher, tracker, domain):
        response = "Can I redirect you to a human who might be more helpful?"
        buttons = [{"title": "Yes", "payload":"/confirmation"},
                   {"title": "No", "payload":"/denial"}]

        dispatcher.utter_button_message(response, buttons)
        return


class UtterContact(Action):
    def name(self):
        return "action_utter_contact"

    def run(self, dispatcher, tracker, domain):
        context = tracker.get_slot("course_type")
        if context == "short":
            response = "You can contact someone about short courses at the following: shortcourses@glasgow.ac.uk"
        elif context == "admissions":
            response = "You can contact someone about PGT admissions at the following: PGAdmissions@glasgow.ac.uk"
        else:
            response = "If your query is about short courses, you can contact shortcourses@glasgow.ac.uk, and if it is about postgraduate admissions, you can contact PGAdmissions@glasgow.ac.uk"

        dispatcher.utter_message(response)
        return
        
# Asks the user to confirm the course
class CheckCourse(Action):
    def name(self):
        return "action_check_course"

    def run(self, dispatcher, tracker, domain):
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))
        response = "Did you want the course: " + str(elastic_title).title() + "?"
        buttons = [{"title":"Yes", "payload":"/confirmation"},
                    {"title":"No", "payload":"/denial"}]

        dispatcher.utter_button_message(response, buttons)
        return


# after giving a short course description, offer a short course link
# confirmation would leak to GetShortCourseLink below
class OfferCourseLink(Action):
    def name(self):
        return "action_offer_course_link"

    def run(self, dispatcher, tracker, domain):
        response = "I can try and look for the short course webpage if you would like further information?"
        buttons = [{"title":"Yes", "payload":"/confirmation"},
                   {"title":"No", "payload":"/denial"}]

        dispatcher.utter_button_message(response, buttons)
        return


class GetShortCourseLink(Action):
    def name(self):
        return "action_get_sc_course_link"

    def run(self, dispatcher, tracker, domain):
        # CheckCourse should have ran & confirmed beforehand
        # so this would be what the user confirmed
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        link = elastic.get_sc_course_link(elastic_title)
        if link:
            response = "Here's a link to the webpage for " + elastic_title + ": " + link
        else:
            response = "Sorry, this short course does not seem to have a web page. This might be because it only runs for one day."

        dispatcher.utter_message(response)
        return[SlotSet("course_type", "short")]


class GetShortCourseResource(Action):
    def name(self):
        return "action_get_sc_resource"

    def run(self, dispatcher, tracker, domain):
        context = tracker.get_slot("course_type")

        if not context or context == "admissions":
            response = "I can only provide this information for short courses. Is this what you were looking for?"
            buttons = [{"title":"Yes", "payload":"/confirmation"},
                         {"title":"No", "payload":"/denial"}]

            dispatcher.utter_button_message(response, buttons)
            return

        else:
            question = tracker.get_slot("question_topic")
            if question:
                resource = elastic.get_sc_resource_link(question)
                if resource:
                    response = "Here's a resource that might be helpful: " + resource
                else:
                    response = "I'm sorry, I couldn't find an appropriate resource for your query."
            else:
                response = "I'm sorry, I'm afraid I'm not able to understand what you mean. Could you try and rephrase your question?"

            dispatcher.utter_message(response)
            return[SlotSet("course_type", "short")]



# Return standard location answer, as we don't have any specific data for it
class GetCourseLocation(Action):
    def name(self):
        return "action_get_location"

    def run(self, dispatcher, tracker, domain):
        context = tracker.get_slot("course_type")

        if not context or context == "admissions":
            response = "I can only provide this information for short courses. Is this what you were looking for?"
            buttons = [{"title":"Yes", "payload":"/confirmation"},
                         {"title":"No", "payload":"/denial"}]
            dispatcher.utter_button_message(response, buttons)
            return

        else:
            response =  "The building will be confirmed by email three days before the start date, and the room number will be listed at reception before the class!"
            dispatcher.utter_message(response)
            return[SlotSet("course_type", "short")]


# Utters the description of a course or tells the description of a term used
# This action is not granular because of the ambiguity of "what is" statements
class GetDescription(Action):
    def name(self):
        return "action_get_description"

    def run(self, dispatcher, tracker, domain):

        course = tracker.get_slot("course")
        acronym = tracker.get_slot("acronym")

        if acronym:
            elastic_cat, elastic_title, elastic_desc = elastic.get_description(acronym)
        elif course:
            elastic_cat, elastic_title, elastic_desc = elastic.get_description(course)
        else:
            response = "Sorry, I can't seem to pick up what you're asking about"
            dispatcher.utter_message(response)
            return

        if elastic_cat in ["SC", "acronym"]:
            # string formatting isn't needed because the description is provided in the data
            response = elastic_desc
        elif elastic_cat == "AD":
            # string formatting is needed for a custom description
            response = "{} is a {} course".format(elastic_title, elastic_desc)
        else:
            response = "Sorry, I could not find any details for that."

        dispatcher.utter_message(response)
        return[SlotSet("acronym", None)]


# checks when a PGT course runs, or returns appropriate message
class PTorFTCheck(Action):
    def name(self):
        return "action_pt_ft_check"

    def run(self, dispatcher, tracker, domain):
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))
        if elastic_cat == "AD":
            pt_ft_answer, pt_ft_variables = elastic.check_pt_ft_course(elastic_title)
        else:
            response = "Sorry, I can only check for part-time/full-time for PGT courses."

        if pt_ft_answer == "not_running":
            response = "Sorry, it does not seem this course is running this year"
        elif pt_ft_answer == "running":
            response = pt_ft_variables[0] + " runs " + ', '.join(pt_ft_variables[1])

        dispatcher.utter_message(response)
        return


# Utters time related information to do with a course e.g. start time, year
class GetTime(Action):
    def name(self):
        return "action_get_time"

    def run(self, dispatcher, tracker, domain):
        # elastic_cat = course category e.g. short course / admissions courses
        # elastic_score = course relevancy score
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        if elastic_cat == "SC":
            # instances_variables
            # 0      1      2      3      4      5
            # title, sdate, edate, stime, etime, duration
            instance_variables = elastic.get_sc_times(elastic_title)

            # If the course begins in January, then it will specify,
            response = "I have found " + str(len(instance_variables)) + " instance(s) of that course: \n"
            i = 1
            for time_variables in instance_variables:
                if time_variables[5] is not 1:
                    response += "Instance " + str(i) + " of %s starts on %s and ends on %s, and runs from %s to %s \n" % (time_variables[0], time_variables[1], time_variables[2], time_variables[3], time_variables[4])
                else:
                    response += "Instance " + str(i) + " of %s runs from %s to %s on %s \n" % (time_variables[0], time_variables[3], time_variables[4], time_variables[1])
                i += 1

        elif elastic_cat == "AD":
            # time_variables
            # 0      1     2
            # title, term, january_start
            time_variables = elastic.get_ad_times(elastic_title)

            # If the course begins in January, then it will specify,
            # Otherwise it will not mention the start month as we do not have more information
            if time_variables[2]:
                answer = "%s starts in %s and begins in January." % (time_variables[0], time_variables[1])
            else:
                answer = "%s starts in %s" % (time_variables[0], time_variables[1])
            response = str(answer)
        else:
            response = "Sorry, I could not find information on times for this course"

        dispatcher.utter_message(response)
        return


# Utters the tutor for a course
class GetTutor(Action):
    def name(self):
        return "action_get_tutor"

    def run(self, dispatcher, tracker, domain):
        # elastic_cat = course category e.g. short course / admissions courses
        # elastic_score = course relevancy score
        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        # we don't have teaching information about PGT
        if elastic_cat == "SC":
            tutor_number, tutor_list = elastic.getMultiTutors(tracker.get_slot("course"))
            if tutor_number == 1:
                response = "The tutor for " + str(elastic_title).title() + " is: " + str(tutor_list) + "."
            elif tutor_number > 1:
                response = "There are " + str(tutor_number) + " different tutors for " + str(elastic_title).title() + ":"
                response += str(tutor_list)
            else:
                response = "Sorry, I could not find any tutors for " + str(elastic_title)

        elif elastic_output == "AD":
            response = "Sorry, I do not know who teaches " + str(elastic_title).title()

        else:
            response = "Sorry, I could not find the tutor for " + str(elastic_title).title()

        dispatcher.utter_message(response)
        return


class ConfirmRequirementType(Action):
    def name(self):
        return "action_confirm_requirement_type"

    def run(self, dispatcher, tracker, domain):
        # at the moment we only have usable PGT data + IELTS requirements, hence this answer
        response = "Currently, I can only provide immediate information on English IELTS requirements for PGT courses. Is this what you're looking for?"
        buttons = [{"title":"Yes", "payload":"/confirmation"},
                   {"title":"No", "payload":"/denial"}]

        dispatcher.utter_button_message(response, buttons)
        return


# Utters the IELTS requirements to get into a course
# The user would have been informed this is IELTS + for admissions
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
        # the user confirmed it's an admissions course so I assume this is the context they're interested in
        return [SlotSet("course_type", "admissions")]


# Utters a list of courses the tutor in question teaches
# e.g. "what classes does Sam Cook teach"
class GetTutorCourses(Action):
    def name(self):
        return "action_get_tutor_courses"

    def run(self, dispatcher, tracker, domain):
        # elastic_output is the list of courses a tutor teaches
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
        context = tracker.get_slot("course_type")

        if context == "short":
            elastic_output, elastic_length = elastic.get_type_courses(tracker.get_slot("course"), context)

            if elastic_output:
                month_text = ""
                weekday_text = ""

                if tracker.get_slot("month"):
                    elastic_output = elastic.filterForMonths(tracker.get_slot("month"), elastic_output)
                    month_text = " in " + tracker.get_slot("month").title()
                if tracker.get_slot("weekday"):
                    elastic_output = elastic.filterForWeekday(tracker.get_slot("weekday"), elastic_output)
                    weekday_text = " on " + tracker.get_slot("weekday").title()
                if elastic_output:
                    elastic_output = elastic.return_list(elastic_output)
                    response = "These are some of the short classes which I have found " + weekday_text + month_text + ": " + elastic_output

                else:
                    response = "Sorry, I could not find any courses with those specifications"

            else:
                response = "Sorry, I could not find any short courses in that subject area"

            dispatcher.utter_message(response)
            return[SlotSet("month", None), SlotSet("weekday", None)]

        # If the user is currently asking about post graduate courses, we will only look for relevant post graduate courses
        elif context == "admissions":
            elastic_output, elastic_length = elastic.get_type_courses(tracker.get_slot("course"), context)

            if elastic_output:
                if tracker.get_slot("month"):
                    response = "Post-Graduate courses either start at the begining of Semester 1 or Semester 2"
                elif tracker.get_slot("weekday"):
                    response = "Sorry, I do not know what days post-graduate courses are on"
                else:
                    response = "These are some of the post-graduate classes which I have found : " + elastic.return_list(elastic_output)

            else:
                response = "Sorry, I could not find any post-graduate courses in that subject area"

            dispatcher.utter_message(response)
            return[SlotSet("month", None), SlotSet("weekday", None)]

        # If the user has not specified already which course type they want we ask them to clarify with the use of buttons
        elif not context:
            response = "Did you want..."
            buttons = [{"title":"Short Courses", "payload":"/ask_set_sc_course_type"},
                        {"title":"Post Graduate", "payload":"/ask_set_ad_course_type"}]
            dispatcher.utter_button_message(response, buttons)

        else:
            response = "Sorry, I did not understand"
            dispatcher.utter_message(response)

        return


# Utters the cost of a course
class GetFees(Action):
    def name(self):
        return "action_get_fee"

    def run(self, dispatcher, tracker, domain):
        # elastic_cat = course category e.g. short course / admissions courses
        # elastic_score = course relevancy score

        elastic_title, elastic_cat, elastic_score = elastic.get_course_title(tracker.get_slot("course"))

        if elastic_cat == "SC":
            elastic_output, elastic_score = elastic.get_sc_field(elastic_title, "Cost")
            response = str(elastic_title).title() + " costs £" + str(elastic_output) + "."
        elif elastic_cat == "AD":
            # fee_variables
            # 0       1         2
            # course, home_fee, int_fee
            fee_variables = elastic.get_ad_fees(elastic_title)
            response = "%s costs £%s if you are from Scotland or the EU, %s costs £%s if you are from elsewhere in the UK or abroad." % (fee_variables[0], fee_variables[1], fee_variables[0], fee_variables[1])

        dispatcher.utter_message(response)
        return
