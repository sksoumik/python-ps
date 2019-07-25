seq = [1, 2, 3, 4]
# result contains odd numbers of the list 
result = filter(lambda x: x + 1, seq)
print(list(result)) # Does nothing on seq as the lambda function does not hold any condition
# Output: [1, 2, 3, 4]
# filter only works on condition, so we need to give some conditional statement with lambda
result = filter(lambda x: x % 2 == 0, seq)  # returns the elements which are only divisible by two
print(list(result)) # output: [2, 4]
