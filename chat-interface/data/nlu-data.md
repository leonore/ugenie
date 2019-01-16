<!--- training data @ https://forum.rasa.com/t/rasa-starter-pack/704 -->
<!-- this is about analysing what the user says, so when adding intents, think:
what input do we want to be able to understand? -->

## intent:fee_check
- how much is [biology]{course}
- how much are the fees for [biology]{course}
- how much does it cost to do [biology]{course}
- how much does it cost to study [biology]{course}
- how much does [biology] cost{course}
- what's the cost to do [biology]{course}
- what's the price of [biology]{course}

## intent:description_check
- tell me about [biology]{course}
- what's the description for [science]{course}

## intent:greet  
- Hi 	
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi there
- hello is anybody there
- hello robot

## intent:goodbye
- okay see you later
- bye for now
- till next time
- I must go
- bye
- goodbye
- see you
- see you soon
- bye-bye
- bye bye good night
- good bye
- bye bye see you
- bye bye see you soon
- I said bye
- never mind bye
- now bye
- that's all goodbye
- that's it goodbye
- leave me alone
- goodbye for now
- talk to you later
- you can go now
- get lost
- alright bye
- see ya
- thanks bye bye
- okay bye
- ok bye

## synonym:biology
- bio