import rules
import json


test_rul = rules.prod_model('rules_v4.json', 'fuctsv3.json')

test_rul.reverse_search(['Черные металлы'])
#test_rul.direct_search(['Металлы', 'Большая плотность', 'Высокая температура плавления'])



