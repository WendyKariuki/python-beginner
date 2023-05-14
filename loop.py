secretnumber = 777

print( """
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("Guess a number:" ))

while number != secretnumber:
    print("Haha! You're stuck in my loop!")
    number = int(input("Guess a number:"))
print("well done")