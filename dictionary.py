
test_dict = {'codingal': 3, 'is': 2, 'for': 2, 'coding': 1}

value_to_check = 2

frequency = list(test_dict.values()).count(value_to_check)

print(f"The value {value_to_check} appears {frequency} times in the dictionary.")
