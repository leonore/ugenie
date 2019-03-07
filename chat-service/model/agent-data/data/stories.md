## greet
* greet
 - utter_greet

## goodbye
* goodbye
 - utter_goodbye

## give_sc_functionality
* ask_short_courses_functionality
 - utter_short_courses_functionality

## give_admissions_functionality
* ask_admissions_courses_functionality
 - utter_admissions_courses_functionality

## give_terminology_functionality
* ask_terminology_functionality
 - utter_terminology_functionality

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
  - utter_lambda

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

## Generated Story 5942406380568682275
* tutor_courses_check{"tutor": "Ruth Ezra"}
    - slot{"tutor": "Ruth Ezra"}
    - action_get_tutor_courses

## Generated Story -4738793752722995132
* tutor_courses_check{"tutor": "William Manley"}
    - slot{"tutor": "William Manley"}
    - action_get_tutor_courses

## Generated Story 693318455824008278
* tutor_courses_check{"tutor": "alison greer"}
    - slot{"tutor": "alison greer"}
    - action_get_tutor_courses

## Generated Story -3564489366415833343
* tutor_courses_check{"tutor": "Clare Crines"}
    - slot{"tutor": "Clare Crines"}
    - action_get_tutor_courses

## Generated Story -4934452183337263033
* tutor_courses_check{"tutor": "Ann Laird"}
    - slot{"tutor": "Ann Laird"}
    - action_get_tutor_courses

## Generated Story -7812749277325169161
* tutor_courses_check{"tutor": "Stephen Mather"}
    - slot{"tutor": "Stephen Mather"}
    - action_get_tutor_courses

## Generated Story -2118669979413158424
* tutor_courses_check{"tutor": "Ronnie Scott"}
    - slot{"tutor": "Ronnie Scott"}
    - action_get_tutor_courses

## Generated Story 5961721126681444915
* tutor_courses_check{"tutor": "Fiona Reid"}
    - slot{"tutor": "Fiona Reid"}
    - action_get_tutor_courses

## Short Course Type question
* ask_sc_type_classes
- action_get_sc_type_classes

## Post Graduate Course Type question
* ask_ad_type_classes
- action_get_ad_type_classes

## Generated Story -5509032080246926965
* greet
    - utter_greet
* ask_short_courses_functionality
    - utter_short_courses_functionality
* ask_sc_type_classes{"course": "writing"}
    - slot{"course": "writing"}
    - action_get_sc_type_classes

## Generated Story 1962544994882331779
* greet
    - utter_greet
* ask_short_courses_functionality
    - utter_short_courses_functionality
* ask_sc_type_classes{"course": "history"}
    - slot{"course": "history"}
    - action_get_sc_type_classes

## Generated Story -679097829603909206
* ask_sc_type_classes{"course": "spanish"}
    - slot{"course": "spanish"}
    - action_get_sc_type_classes

## Generated Story 9197496254116985007
* ask_ad_type_classes{"course": "education"}
    - slot{"course": "education"}
    - action_get_ad_type_classes

## Generated Story 4386387057852718816
* greet
    - utter_greet
* ask_admissions_courses_functionality
    - utter_admissions_courses_functionality
* ask_ad_type_classes{"course": "engineering"}
    - slot{"course": "engineering"}
    - action_get_ad_type_classes

## Generated Story -7459482735023145453
* greet
    - utter_greet
* ask_admissions_courses_functionality
    - utter_admissions_courses_functionality
* ask_ad_type_classes{"course": "physics"}
    - slot{"course": "physics"}
    - action_get_ad_type_classes

## Generated Story -7701771790884704278
* ask_ad_type_classes{"course": "russian"}
    - slot{"course": "russian"}
    - action_get_ad_type_classes

## Generated Story -3547260180970667061
* greet
    - utter_greet
* ask_short_courses_functionality
    - utter_short_courses_functionality
* ask_sc_type_classes{"course": "psychology"}
    - slot{"course": "psychology"}
    - action_get_sc_type_classes

## Generated Story 1622595172970137974
* greet
    - utter_greet
* ask_admissions_courses_functionality
    - utter_admissions_courses_functionality
* ask_ad_type_classes{"course": "sport"}
    - slot{"course": "sport"}
    - action_get_ad_type_classes

## Generated Story -2750606043582181831
* greet
    - utter_greet
* ask_short_courses_functionality
    - utter_short_courses_functionality
* ask_sc_type_classes{"course": "science"}
    - slot{"course": "science"}
    - action_get_sc_type_classes

## Generated Story -9157648934427937927
* greet
    - utter_greet
* ask_short_courses_functionality
    - utter_short_courses_functionality
* ask_sc_type_classes{"course": "music"}
    - slot{"course": "music"}
    - action_get_sc_type_classes
## Generated Story -3071205715805701429
* greet
    - utter_greet
* ask_admissions_courses_functionality
    - utter_admissions_courses_functionality
* ask_ad_type_classes{"course": "urban"}
    - slot{"course": "urban"}
    - action_get_ad_type_classes

## Generated Story 996290071412567687
* greet
    - utter_greet
* ask_admissions_courses_functionality
    - utter_admissions_courses_functionality
* ask_ad_type_classes{"course": "media"}
    - slot{"course": "media"}
    - action_get_ad_type_classes

## Generated Story -2757736751059362259
* ask_ad_type_classes{"course": "law"}
    - slot{"course": "law"}
    - action_get_ad_type_classes
