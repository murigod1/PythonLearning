friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

# long_timers = {
#     friends[i]: time_since_seen[i]
#     for i in range(len(friends))
#     if time_since_seen[i] > 5
# }

# print(long_timers)

guests = ["jose", "rolf", "lucas", "anne"]

friends_lower = set([f.lower() for f in friends])
guests_lower = set([g.lower() for g in guests])

print(friends_lower.intersection(guests_lower))