import rules
import json


test_rul = rules.prod_model('rules.json', 'facts.json')
test_rul.reverse_search(['_Na'])




