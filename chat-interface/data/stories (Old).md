## story_greet 
* greet 
 - utter_greet 

## story_fee_check_eu 
* fee_check
 - utter_ask_student
* fee_check{"student": "eu"}
 - slot{"student": "eu"}
 - action_get_fee
 
## story_fee_check_scottish
* fee_check
 - utter_ask_student
* fee_check{"student": "scottish"}
 - slot{"student": "scottish"}
 - action_get_fee
 
## story_fee_check_international
* fee_check
 - utter_ask_student
* fee_check{"student": "international"}
 - slot{"student": "international"}
 - action_get_fee

## story_description_check
* description_check
 - utter_description_check
 
## story_goodbye
* goodbye
 - utter_goodbye