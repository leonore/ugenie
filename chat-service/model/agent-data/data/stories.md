## greet
* greet
 - utter_greet
 - utter_functionality

## goodbye
* goodbye
 - utter_goodbye

## you're wrong! but help me again
* wrong_answer
 - utter_help
* confirmation
 - utter_functionality

## you're wrong! redirect me to a human
* wrong_answer
 - utter_help
* denial
 - utter_redirect
* denial
 - utter_sorry

## thank you
* thank_you
 - utter_help

## extended functionality story
* greet
 - utter_greet
 - utter_functionality
* ask_short_courses_functionality
 - action_utter_short_courses_functionality
* tutor_check
 - action_get_tutor
* tutor_courses_check
 - action_get_tutor_courses
* thank_you
 - utter_help
 - utter_functionality

## give_sc_functionality
* help
 - utter_functionality

## give_sc_functionality
* ask_short_courses_functionality
 - action_utter_short_courses_functionality

## give_admissions_functionality
* ask_admissions_courses_functionality
 - action_utter_admissions_courses_functionality

## give_terminology_functionality
* ask_terminology_functionality
 - utter_terminology_functionality

## link_check_confirm
* link_check
- action_check_course
* confirmation
- action_get_sc_course_link

## link_check_deny
* link_check
- action_check_course
* denial
- action_course_denied

## fee_check_confirm
* fee_check
 - action_check_course
* confirmation
 - action_get_fee

## fee_check_deny
* fee_check
 - action_check_course
* denial
 - action_course_denied

## time_check_confirm
* time_check
- action_check_course
* confirmation
 - action_get_time

## time_check_deny
* time_check
 - action_check_course
* denial
 - action_course_denied

## description_check
 * description_check
  - action_get_description

## acronym_check
* acronym_check
 - action_get_acronym

## tutor_check_confirm
* tutor_check
 - action_check_course
* confirmation
 - action_get_tutor

## tutor_check_deny
* tutor_check
 - action_check_course
* denial
 - action_course_denied

## ielts_requirements_check_yes
* requirements_check{"course": "Advanced Nursing Science"}
   - slot{"course": "Advanced Nursing Science"}
   - utter_confirm_requirement_type
* confirmation
   - action_get_ielts_requirements

## ielts_requirements_check_no
* requirements_check{"course":"American studies"}
  - slot{"course":"American studies"}
  - utter_confirm_requirement_type
* denial
  - utter_redirect
* denial
  - utter_sorry

## ielts_requirements_check_no_redirect
* requirements_check{"course":"mechatronics"}
  - slot{"course":"mechatronics"}
  - utter_confirm_requirement_type
* denial
  - utter_redirect
* confirmation
  - utter_contact

## tutor_courses_check
* tutor_courses_check{"tutor":"Pamela Ross"}
 - action_get_tutor_courses{"tutor":"Pamela Ross"}

## acronym_check_ATAS
* acronym_check{"acronym":"ATAS"}
 - slot{"acronym": "ATAS"}
 - action_get_acronym

## acronym_check_mario
* acronym_check{"acronym":"MaRio"}
 - slot{"acronym": "Mario"}
 - action_get_acronym

## acronym_check_PT
* acronym_check{"acronym":"PT"}
 - slot{"acronym": "PT"}
 - action_get_acronym

## ask course type with none
- ask_type_classes
* action_get_type_classes

## setting course type to SC
* ask_set_sc_course_type
 - action_set_sc_course_type
 - action_get_type_classes

## setting course type to AD
* ask_set_ad_course_type
 - action_set_ad_course_type
 - action_get_type_classes

## Get brain science time
* time_check{"course": "brain science"}
    - slot{"course": "brain science"}
    - action_check_course
* confirmation
    - action_get_time

## Wrong course offered
* time_check{"course": "french stage"}
    - slot{"course": "french stage"}
    - action_check_course
* denial
    - action_course_denied

## two description checks
* description_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_get_description
* description_check{"course": "brain sciences"}
    - slot{"course": "brain sciences"}
    - action_get_description

## Get time for brain science
* time_check{"course": "brain science"}
    - slot{"course": "brain science"}
    - action_check_course
* confirmation
    - action_get_time

## Get fees for german stage 2
* fee_check{"course": "german stage 2"}
    - slot{"course": "german stage 2"}
    - action_check_course
* confirmation
    - action_get_fee

## Get times for french stage 1
* time_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_check_course
* confirmation
    - action_get_time

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

## Acronym check
* greet
    - utter_greet
* acronym_check{"acronym": "IELTS"}
    - slot{"acronym": "IELTS"}
    - action_get_acronym

## Check for short course description
* greet
    - utter_greet
* description_check{"course": "working with trauma"}
    - slot{"course": "working with trauma"}
    - action_get_description
    - slot{"acronym": null}

## Check for short course description
* description_check{"course": "opera afternoons"}
    - slot{"course": "opera afternoons"}
    - action_get_description
    - slot{"acronym": null}

## Check acronym description
* acronym_check{"acronym": "plan code"}
    - slot{"acronym": "plan code"}
    - action_get_acronym

## ## Get short courses Ruth Ezra teaches
* tutor_courses_check{"tutor": "Ruth Ezra"}
    - slot{"tutor": "Ruth Ezra"}
    - action_get_tutor_courses

## ## Get short courses William Manley teaches
* tutor_courses_check{"tutor": "William Manley"}
    - slot{"tutor": "William Manley"}
    - action_get_tutor_courses

## Get short courses Alison Greer teaches
* tutor_courses_check{"tutor": "alison greer"}
    - slot{"tutor": "alison greer"}
    - action_get_tutor_courses

## Get short courses Clare Crines teaches
* tutor_courses_check{"tutor": "Clare Crines"}
    - slot{"tutor": "Clare Crines"}
    - action_get_tutor_courses

## Get short courses Ann Laird teaches
* tutor_courses_check{"tutor": "Ann Laird"}
    - slot{"tutor": "Ann Laird"}
    - action_get_tutor_courses

## Get short courses Stephen Mather teaches
* tutor_courses_check{"tutor": "Stephen Mather"}
    - slot{"tutor": "Stephen Mather"}
    - action_get_tutor_courses

## Get short courses Ronnie Scott teaches
* tutor_courses_check{"tutor": "Ronnie Scott"}
    - slot{"tutor": "Ronnie Scott"}
    - action_get_tutor_courses

## Get short courses Fiona Reid teaches
* tutor_courses_check{"tutor": "Fiona Reid"}
    - slot{"tutor": "Fiona Reid"}
    - action_get_tutor_courses

## Get spanish classes
* ask_type_classes{"course": "spanish"}
    - slot{"course": "spanish"}
    - action_get_type_classes

## Generated Course link Story
* greet
    - utter_greet
    - utter_functionality
* ask_short_courses_functionality
    - action_utter_short_courses_functionality
    - slot{"course_type": "short"}
* description_check{"course": "geology in the field"}
    - slot{"course": "geology in the field"}
    - action_get_description
    - slot{"acronym": null}
    - utter_offer_course_link
* confirmation
    - action_get_sc_course_link

## provide help, user says yes
* thank_you
    - utter_help
* confirmation
    - utter_functionality

## provide help, user says no
* thank_you
    - utter_help
* denial
    - utter_goodbye

## Getting greet + functionality to work
* greet
    - utter_greet
    - utter_functionality
* ask_admissions_courses_functionality
    - action_utter_admissions_courses_functionality
    - slot{"course_type": "admissions"}
