# Calculate Average Temperature
# num_days = int(input("How may day's temperature? "))
# total = 0
# for i in range(1, num_days + 1):
#     nextDay = int(input("Day " + str(i) + "'s high temp: "))
#     total = total + nextDay
# average = total / num_days
# print(average)

# Using list to determine which days exceed the average temperature
num_days = int(input("How may day's temperature? "))
total = 0
temp = []
for i in range(num_days):
    nextDay = int(input("Day " + str(i) + "'s high temp: "))
    temp.append(nextDay)
    total = total + temp[i]

average = total / num_days
print(average)

above = 0
for i in temp:
    if i > average:
        above += 1
print(above)
