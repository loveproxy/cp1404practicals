#CP1404/CP5632 - Practical


score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 50:  # not correct, the logic should be checked. if the input is 92, two results will be output.
        print("Passable")
    if score >= 90:
        print("Excellent")
    if score < 50:
        print("Bad")

#  the correct code should be, for example, if you input 92, the program will output two results!
#     if score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Passable")
#     elif score < 50:
#         print("Bad")
