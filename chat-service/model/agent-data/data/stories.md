## user greet
* greet
 - utter_greet
 - action_utter_functionality

## user goodbye
* goodbye
 - utter_goodbye

## user thank you
* thank_you
 - action_utter_help

## user says something unexpected
* out_of_scope
 - utter_chitchat

## user asks for functionality
* help
 - action_utter_functionality

## user has been here before
* expert
 - utter_expert

## user asks to be redirect to a human
* ask_human
 - action_utter_contact

## provide help, user says yes
* thank_you
   - action_utter_help
* confirmation
   - action_utter_functionality

## provide help, user says no
* thank_you
   - action_utter_help
* denial
   - utter_goodbye

## user asks for short course functionality
* ask_short_courses_functionality
- action_utter_short_courses_functionality

## user asks for admissions functionality
* ask_admissions_courses_functionality
- action_utter_admissions_courses_functionality

## user asks for terminology functionality
* ask_terminology_functionality
- utter_terminology_functionality

## setting course type to SC
* ask_type_classes
 - action_get_type_classes
* ask_set_sc_course_type
 - action_set_sc_course_type
 - action_get_type_classes

## setting course type to AD
* ask_type_classes
 - action_get_type_classes
* ask_set_ad_course_type
 - action_set_ad_course_type
 - action_get_type_classes

## ask course type with none
* ask_type_classes
 - action_get_type_classes

## Get spanish classes
* ask_type_classes{"course": "spanish"}
   - slot{"course": "spanish"}
   - action_get_type_classes

## you're wrong! but help me again
* wrong_answer
 - action_utter_help
* confirmation
 - action_utter_functionality

## you're wrong! redirect me to a human
* wrong_answer
 - action_utter_help
* denial
 - action_utter_redirect
* denial
 - utter_sorry

## user link check, right bot suggestion
* link_check
- action_check_course
* confirmation
- action_get_sc_course_link

## user link check, wrong bot suggestion
* link_check
- action_check_course
* denial
- utter_course_denied

## user asks for funding being in the SC course context
* sc_common_question
 - action_get_sc_resource

## user asks for funding without having set a context
* sc_common_question
 - action_get_sc_resource
* confirmation
 - action_set_sc_course_type
 - action_get_sc_resource

## user asks for funding but didn't want it for short courses
* sc_common_question
 - action_get_sc_resource
* denial
 - action_utter_redirect

## user asks for course location while being in the SC course context
* location_check
 - action_get_location

## user asks for course location without having set a context
* location_check
- action_get_location
* confirmation
- action_set_sc_course_type
- action_get_location

## user asks for a course location but didn't want it for short courses
* location_check
- action_get_location
* denial
- action_utter_redirect

## user asks for credits check while being in the SC course context
* credits_check
 - action_get_credits

## user asks for course location without having set a context
* credits_check
- action_get_credits
* confirmation
- action_set_sc_course_type
- action_get_location

## user asks for a course location but didn't want it for short courses
* credits_check
- action_get_location
* denial
- action_utter_redirect

## user FT/PT check, right bot suggestion
* full_part_time_check
 - action_check_course
* confirmation
 - action_pt_ft_check

## user FT/PT check, wrong bot suggestion
* full_part_time_check
- action_check_course
* denial
- utter_course_denied

## user fee check, right bot suggestion
* fee_check
 - action_check_course
* confirmation
 - action_get_fee

## user fee check, wrong bot suggestion
* fee_check
 - action_check_course
* denial
 - utter_course_denied

## user time check, right bot suggestion
* time_check
- action_check_course
* confirmation
 - action_get_time

## user time check, wrong bot suggestion
* time_check
 - action_check_course
* denial
 - utter_course_denied

## user description check, right bot suggestion
* description_check
 - action_check_course
* denial
 - action_get_description

## user description check, wrong bot suggestion
* description_check
 - action_check_course
* denial
 - utter_course_denied

## user tutor check, right bot suggestion
* tutor_check
 - action_check_course
* confirmation
 - action_get_tutor

## user tutor check, wrong bot suggestion
* tutor_check
 - action_check_course
* denial
 - utter_course_denied

## user asks for tutor's courses
* tutor_courses_check{"tutor":"Pamela Ross"}
- action_get_tutor_courses{"tutor":"Pamela Ross"}

## user acronym check
* acronym_check
- action_get_description

## user ielts check, right bot suggestion
* requirements_check
   - action_confirm_requirement_type
* confirmation
   - action_get_ielts_requirements

## user ielts check, wrong bot suggestion, no redirect
* requirements_check
  - action_confirm_requirement_type
* denial
  - action_utter_redirect
* denial
  - utter_sorry

## user ielts check, wrong bot suggestion, redirect
* requirements_check
  - action_confirm_requirement_type
* denial
  - action_utter_redirect
* confirmation
  - action_utter_contact

## Stories that follow are mainly generated with interactive training
## two description checks
* description_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_get_description
* description_check{"course": "french stage 2"}
    - slot{"course": "french stage 2"}
    - action_get_description

## Get fees for german stage 2
* fee_check{"course": "german stage 2"}
    - slot{"course": "german stage 2"}
    - action_check_course
* confirmation
    - action_get_fee

## Get tutor for german stage 2
* tutor_check{"course": "german stage 2"}
    - slot{"course": "german stage 2"}
    - action_check_course
* confirmation
    - action_get_tutor

## Get tutor for spanish stage 4
* tutor_check{"course": "spanish stage 4"}
    - slot{"course": "spanish stage 4"}
    - action_check_course
* confirmation
    - action_get_tutor

## Full check of short course
* greet
    - utter_greet
* fee_check{"course": "the price of fancy florence"}
    - slot{"course": "the price of fancy florence"}
    - action_check_course
* confirmation
    - action_get_fee
* time_check{"course": "fancy florence"}
    - slot{"course": "fancy florence"}
    - action_check_course
* confirmation
    - action_get_time
* tutor_check{"course": "fancy florence"}
    - slot{"course": "fancy florence"}
    - action_check_course
* confirmation
    - action_get_tutor

## Check for short course description
* greet
    - utter_greet
* description_check{"course": "working with trauma"}
    - slot{"course": "working with trauma"}
    - action_get_description
    - slot{"acronym": null}

## Get short courses Ann Laird teaches
* tutor_courses_check{"tutor": "Ann Laird"}
    - slot{"tutor": "Ann Laird"}
    - action_get_tutor_courses

## Generated Course link Story
* greet
    - utter_greet
    - action_utter_functionality
* ask_short_courses_functionality
    - action_utter_short_courses_functionality
    - slot{"course_type": "short"}
* description_check{"course": "geology in the field"}
    - slot{"course": "geology in the field"}
    - action_get_description
    - slot{"acronym": null}
    - action_offer_course_link
* confirmation
    - action_get_sc_course_link


## extended functionality story
* greet
 - utter_greet
 - action_utter_functionality
* ask_short_courses_functionality
 - action_utter_short_courses_functionality
* tutor_check
 - action_get_tutor
* tutor_courses_check
 - action_get_tutor_courses
* thank_you
 - action_utter_help

## Getting location check to work
* greet
    - utter_greet
    - action_utter_functionality
* ask_short_courses_functionality
    - action_utter_short_courses_functionality
    - slot{"course_type": "short"}
* location_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_get_location

## Extended story to generate admissions graph in documentation
* description_check{"course": "academic practice"}
    - slot{"course": "academic practice"}
    - action_get_description
* location_check{"course": "academic practice"}
    - slot{"course": "academic practice"}
    - action_get_location
* denial
    - action_utter_redirect
* confirmation
    - action_utter_contact

## Asks for refund and then asks for help
* sc_common_question
 - action_get_sc_resource
* denial
 - action_utter_redirect
* confirmation
 - action_utter_contact
