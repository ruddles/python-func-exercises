# Write a map call that takes in the numbers 1-5 and doubles them

doubles = map(lambda x: x*2, range(1, 6))
print(list(doubles))  # expect [2, 4, 6, 8, 10]
