import re
import json

def ind_facts(facts = [], dict_fact = dict()):
    res_list = []
    for fact in facts:
        for key in dict_fact.keys():
            if (dict_fact[key] == fact):
                res_list.append(key)
                break
    return res_list

f = open('rules.txt',  encoding='utf-8')
oll_text_rule = f.read()
text_rule = re.split(r'-> | & |\n', oll_text_rule)

ind_fact = 0
dict_fact = dict()
set_fact = set(text_rule)

for rule in set_fact:
    if (rule != ''):
        dict_fact[str(ind_fact)] = rule
    ind_fact += 1

dicts_rul = []
list_ruls = re.findall(r'.+', oll_text_rule)
for ruls in list_ruls:
    package_result = re.split(r'-> ', ruls)
    dicts_rul.append({'&': ind_facts(re.split(r' & ', package_result[0]), dict_fact), '=' : ind_facts(re.split(r' & ', package_result[1]), dict_fact)})

with open('rulesv3.json', 'w') as outfile:
    outfile.write(json.dumps({'rules': dicts_rul}))

import codecs
with open('fuctsv3.json', 'wb') as f:
    json.dump(dict_fact, codecs.getwriter('utf-8')(f), ensure_ascii=False)