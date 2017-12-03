import rules

test_rul = rules.prod_model('questions.txt', 'facts.json')
test_rul.reverse_search(["_Na"])