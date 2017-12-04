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

    def direct_searcj(self, list_rule = []) :
        queue_rule  = Queue()
        result_set = set()

        for rule in list_rule:
            queue_rule.put(rule)

        while (queue_rule.qsize() != 0):
            next_rule = self.user_rule[queue_rule.get()]
            for rule in next_rule:
                if (rule[0] == '_'):
                    result_set = result_set.union([rule])
                else:
                    queue_rule.put(rule)
        print(result_set)

    def reverse_search(self, ellements = []):
        queue_ell = Queue()
        result_set = set()

        for ell in ellements:
            queue_ell.put(ell)

        while (queue_ell.qsize() != 0):
            ell = queue_ell.get()
            for key in self.user_rule.keys():
                if (self.user_rule[key].count(ell) != 0):
                    print(self.all_rule[key])
                    result_set.add(key)
                    queue_ell.put((key))



