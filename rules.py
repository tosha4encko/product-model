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

    def start_search(self):
        init_set = self.I;
        for k in self.rule.keys():
            print(k)
            a = int(input())
            if (a == 1):
                init_set -= (init_set - set(self.rule[k]))
            if (a == 0):
                init_set -= set(self.rule[k])
        print(init_set)

    def start_search_other_file(self):
        init_question = 'Это простой эллемент?'
        print(init_question)
        a = (input())

        while (type(init_question) != type([])):
            if (a=='+'):
                init_question = self.user_rule[init_question][0]
            else:
                if (a=='-'):
                    init_question = self.user_rule[init_question][1]
                else:
                    init_question = ['Null']

            print(init_question)

            a = input()

    def start_search_many_rull(self, list_rule = []) :
        queue_rule  = Queue()
        result_set = set()

        for rule in list_rule:
            queue_rule.put(rule)

        while (queue_rule.qsize() != 0):
            next_rule = self.user_rule[queue_rule.get()]
            for rule in next_rule:
                if (type(rule) == type([])):
                    result_set = result_set.union(set(rule))

                if (type(rule) == type('')):
                    queue_rule.put(rule)

        print(result_set)