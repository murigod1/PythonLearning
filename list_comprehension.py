# numbers = [0, 1, 2, 3, 4]
# # doubled_number = []

# # for number in numbers:
# #     doubled_number.append(numbers * 2)

# doubled_number = [number * 2 for number in numbers]
# print(doubled_number)

# friend_ages = [22, 31, 35, 37]
# ages_string = [f"My friend is {age} year old" for age in friend_ages]
# print(ages_string)

# names = ["Lucas", "Wendel", "Nappa", "Pastor"]
# lowerCase = [name.lower() for name in names]
# print(names)

# friend = input("What's your name: ")
# friends = ["Lucas", "Wendel", "Nappa", "Pastor"]
# friends_lower = [names.lower() for names in friends]

# if friend.lower() in friends_lower:
#     print(f'I know {friend.title()}')

# friends = ["Rolf", "ruth", "charlie", "Jen"]
# guests = ["jose", "Bod", "Rolf", "Charlie", "michael"]

# friends_lower = [f.lower() for f in friends]

# friends_frinds = [
#     name.title()
#     for name in guests
#     if name.lower() in friends_lower
# ]

# print(friends_frinds)