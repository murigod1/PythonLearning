friend = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Enter your name:")

if user_name in friend:
    print("Hello, Friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I don't know you.")