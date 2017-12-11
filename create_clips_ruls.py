import re
import json
import codecs

def ind_facts(facts = [], dict_fact = dict()):
    res_list = []
    for fact in facts:
        # if (fact == 'Co(кобальт)'):
        #     print(fact)
        for key in dict_fact.keys():
            if (dict_fact[key] == fact):
                res_list.append(key)
                break
    return res_list


f = open('rules.txt',  encoding='utf-8')
oll_text_rule = f.read()
text_rule = re.split(r' -> | & |\n|,|\[|\]', oll_text_rule)

ind_fact = 0
dict_fact = dict()
set_fact = set(text_rule)

for rule in set_fact:
    if (rule != ''):
        dict_fact[str(ind_fact)] = rule
    ind_fact += 1
#
clips_ruls = ''
ind_rule = 0
dicts_rul = dict()
list_ruls = re.findall(r'.+', oll_text_rule)
for ruls in list_ruls:
    package_result = re.split(r' -> ', ruls)
    list_res  = re.split(r'\[|\]|, ', package_result[1])
    list_pack = re.split(r' & ', package_result[0])

    clips_ruls += '(defrule  rule' + str(ind_rule) + '\n'
    for pack in list_pack:
        key = ind_facts([pack], dict_fact)
        if(len(key) > 0):
            clips_ruls += '(_' + str(ind_facts([pack], dict_fact)[0]) + ')\n'
    clips_ruls += '=>'
    for res in list_res:
        key = ind_facts([res], dict_fact)
        if (len(key) > 0):
            clips_ruls += '(assert (_' + str(ind_facts([res], dict_fact)[0]) + '))\n'
    clips_ruls += ')\n'
    ind_rule += 1

print(clips_ruls)

with open('rules.clp', 'w') as outfile:
    outfile.write(clips_ruls)