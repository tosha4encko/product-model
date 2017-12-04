import rules
import json


test_rul = rules.prod_model('rules.json', 'facts.json')
#test_rul.direct_searcj(['13', '34', '51'])
test_rul.reverse_search(['_Na'])



