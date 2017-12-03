import rules

test_rul = rules.prod_model('questions.txt', 'rules.json')
test_rul.reverse_search(["_Na"])