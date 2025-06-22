import random

# randomizer = random.randint(1, 10)  # we can put the range inside parentheses, or...

lowest = 1
highest = 20
randomizer = random.randint(lowest, highest)

print(randomizer)


# To print random floating point number

num = random.random()  # in the random module, we used random method
print(num)  # this will print randum number between 0 and 1
