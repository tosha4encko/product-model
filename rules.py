import json
from queue import Queue

class prod_model:
    user_rule = dict()
    all_rule  = dict()

    def __init__(self, file_rule, file_all_rule):

        js_obj = open(file_rule, "r", encoding='utf-8')
        self.user_rule = json.load((js_obj))

        js_obj1 = open(file_all_rule, "r", encoding='utf-8')
        self.all_rule = json.load((js_obj1))

    def ind_facts(self, facts=[]):
        res_list = []

        for fact in facts:
            for key in self.all_rule.keys():
                if (self.all_rule[key] == fact):
                    res_list.append(key)
                    break
        return res_list

    def direct_search(self, list_ruls = []):
        set_rule = set(self.ind_facts(list_ruls))

        for key in self.user_rule.keys():
            if (set(self.user_rule[key]) <= set_rule):
                set_rule.add(key)

        for fact in set_rule:
            print(self.all_rule[fact])
        print()

    def reverse_search(self, ellements = []):
        set_rule = set(self.ind_facts(ellements))
        list_key = self.user_rule.keys()
        for fact in set_rule:
            if (fact in list_key):
                set_rule = set_rule.union(set(self.user_rule[fact]))

        for fact in set_rule:
            print(self.all_rule[fact])
        print()



