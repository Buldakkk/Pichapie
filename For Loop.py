# we use for loop to print something repeatedly without needing manual coding.

for asterisk in range(2):
    # RANDOM NOTE: to make it print starting with 1 instead of 0, use print("*", asterisk + 1)
    print("*", asterisk + 1, (asterisk + 1) * ".")

# RANDOM NOTE: There's also another way to do that
for asterisk in range(1, 6):
    print("-", asterisk, (asterisk) * ".")


for asterisk in range(1, 9, 2):
    print("+", asterisk, (asterisk) * ".")


# NESTED LOOP
for x in range(3):
    for y in range(2):
        print(f"\n({x},{y})")

# Iterable
for p in "\nBabu\n":
    print(p)

'''''
# WHILE LOOP
number = 100
while number > 0:
    print(number)
    number = number // 2
    # COMPOUND STATEMENT: number //= 2
    # this is an expression to print limited numbers, loop won't stop if don't have it.


inp = ""
while inp.lower() != "quit":
    inp = input("Enter here: ")
    print("Paste:", inp)

# SITUATION: what if the user enters an uppercase?
# ANSWER: Put [while inp.lower() != "quit":] this function to convert erthing to lower to match the lowercased "quit"


# SAME WITH WHAT'S ABOVE
command = ""
while True:
    command = input("Hephep: ")
    print("Hooray", command)

    if command == "stop":
        break
'''

# EXERCISE: PRINT 2,4,6,8 \n We have 4 even numbers

count = 0
for m in range(1, 10):
    if m % 2 == 0:
        print(m)
        count += 1

print("We have", count, "even numbers")
