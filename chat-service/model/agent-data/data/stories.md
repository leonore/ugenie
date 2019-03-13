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
 - utter_out_of_scope

## user asks for functionality
* help
 - action_utter_functionality

## user has been here before
* expert
 - utter_expert

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
* ask_set_sc_course_type
 - action_set_sc_course_type
 - action_get_type_classes

## setting course type to AD
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
- action_course_denied

## user asks for course location while being in the SC course context
* ask_set_sc_course_type
 - action_set_sc_course_type
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

## user FT/PT check, right bot suggestion
* full_part_time_check
 - action_check_course
* confirmation
 - action_pt_ft_check

## user FT/PT check, wrong bot suggestion
* full_part_time_check
- action_check_course
* denial
- action_course_denied

## user fee check, right bot suggestion
* fee_check
 - action_check_course
* confirmation
 - action_get_fee

## user fee check, wrong bot suggestion
* fee_check
 - action_check_course
* denial
 - action_course_denied

## user time check, right bot suggestion
* time_check
- action_check_course
* confirmation
 - action_get_time

## user time check, wrong bot suggestion
* time_check
 - action_check_course
* denial
 - action_course_denied

## user description check, right bot suggestion
* description_check
 - action_check_course
* denial
 - action_get_description

## user description check, wrong bot suggestion
* description_check
 - action_check_course
* denial
 - action_course_denied

## user tutor check, right bot suggestion
* tutor_check
 - action_check_course
* confirmation
 - action_get_tutor

## user tutor check, wrong bot suggestion
* tutor_check
 - action_check_course
* denial
 - action_course_denied

## user asks for tutor's courses
* tutor_courses_check{"tutor":"Pamela Ross"}
- action_get_tutor_courses{"tutor":"Pamela Ross"}

## user acronym check
* acronym_check
- action_get_acronym

## acronym check for ATAS
* acronym_check{"acronym":"ATAS"}
 - slot{"acronym": "ATAS"}
 - action_get_acronym

## acronym check for mario
* acronym_check{"acronym":"MaRio"}
 - slot{"acronym": "Mario"}
 - action_get_acronym

## acronym check for PT
* acronym_check{"acronym":"PT"}
 - slot{"acronym": "PT"}
 - action_get_acronym

## acronym check for Plan Code
* acronym_check{"acronym": "plan code"}
   - slot{"acronym": "plan code"}
   - action_get_acronym

## extended acronym check for IELTS
* greet
   - utter_greet
* acronym_check{"acronym": "IELTS"}
   - slot{"acronym": "IELTS"}
   - action_get_acronym

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
  - utter_contact

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

## Check for short course description
* description_check{"course": "opera afternoons"}
    - slot{"course": "opera afternoons"}
    - action_get_description
    - slot{"acronym": null}

## Get short courses Ruth Ezra teaches
* tutor_courses_check{"tutor": "Ruth Ezra"}
    - slot{"tutor": "Ruth Ezra"}
    - action_get_tutor_courses

## Get short courses William Manley teaches
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
 - action_utter_functionality

## Getting greet + functionality to work
* greet
    - utter_greet
    - action_utter_functionality
* ask_admissions_courses_functionality
    - action_utter_admissions_courses_functionality
    - slot{"course_type": "admissions"}

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
