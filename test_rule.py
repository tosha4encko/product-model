import rules

test_rul = rules.prod_model('questions.txt', 'rules.json')
test_rul.start_search_many_rull(['22', "13", "33"])
