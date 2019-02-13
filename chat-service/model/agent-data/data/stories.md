## greet
* greet
 - utter_greet

## goodbye
* goodbye
 - utter_goodbye

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

## description_check_confirm
 * description_check
 - action_check_course
 * confirmation
  - action_get_description

## description_check_deny
* description_check
 - action_check_course
* denial
 - action_course_denied

## acronym_check
* acronym_check
 - action_get_acronym

## tutor_check
* tutor_check
 - action_get_tutor

## requirements_check
* requirements_check
 - utter_confirm_requirement_type
* give_req_type
 - action_get_requirements

## Generated Story -2906752824971192833
* time_check{"course": "brain science"}
    - slot{"course": "brain science"}
    - action_check_course
* confirmation
    - action_get_time

## Generated Story 401500576632580407
* time_check{"course": "french stage"}
    - slot{"course": "french stage"}
    - action_check_course
* denial
    - action_course_denied
