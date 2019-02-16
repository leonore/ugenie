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

## description_check
 * description_check
  - action_get_description

## acronym_check
* acronym_check
 - action_get_description

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

## Generated Story -8439416083735920226
* description_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_get_description
* description_check{"course": "brain sciences"}
    - slot{"course": "brain sciences"}
    - action_get_description

## Generated Story -7533391507131635900
* description_check{"acronym": "ft"}
    - slot{"acronym": "ft"}
    - action_get_description
    - slot{"acronym": null}
* description_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_get_description
    - slot{"acronym": null}
* description_check{"course": "brain sciences"}
    - slot{"course": "brain sciences"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story -38991934262801992
* description_check{"acronym": "ATAS"}
    - slot{"acronym": "ATAS"}
    - action_get_description
    - slot{"acronym": null}
* description_check{"course": "opera afternoons 1"}
    - slot{"course": "opera afternoons 1"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story 4143942832046725484
* description_check{"acronym": "ATAS"}
    - slot{"acronym": "ATAS"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story -80120238664483409
* time_check{"course": "brain science"}
    - slot{"course": "brain science"}
    - action_check_course
* confirmation
    - action_get_time
## Generated Story -8446625055458395372
* fee_check{"course": "german stage 2"}
    - slot{"course": "german stage 2"}
    - action_check_course
* confirmation
    - action_get_fee

## Generated Story -1947807233046006126
* time_check{"course": "french stage 1"}
    - slot{"course": "french stage 1"}
    - action_check_course
* confirmation
    - action_get_time

## Generated Story 6367092150298876504
* tutor_check{"course": "german stage 2"}
    - slot{"course": "german stage 2"}
    - action_check_course
* confirmation
    - action_get_tutor

## Generated Story -8976798553218325342
* tutor_check{"course": "spanish stage 4"}
    - slot{"course": "spanish stage 4"}
    - action_check_course
* confirmation
    - action_get_tutor

## Generated Story 531403387340956866
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

## Generated Story 5678576394477347802
* greet
    - utter_greet
* description_check{"acronym": "IELTS"}
    - slot{"acronym": "IELTS"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story 7504242019204737608
* description_check{"acronym": "PT"}
    - slot{"acronym": "PT"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story -6739786421983660791
* greet
    - utter_greet
* description_check{"course": "working with trauma"}
    - slot{"course": "working with trauma"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story -241338351404499824
* description_check{"course": "opera afternoons"}
    - slot{"course": "opera afternoons"}
    - action_get_description
    - slot{"acronym": null}

## Generated Story -48418464369663666
* description_check{"acronym": "plan code"}
    - slot{"acronym": "plan code"}
    - action_get_description
    - slot{"acronym": null}
