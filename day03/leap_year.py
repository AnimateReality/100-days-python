year = int(input("Which year do you want to check?"))

if year % 4 == 0:
    print("this is a leap year")
    if year % 100 == 0:
        print("this is not a leap year because its evenly divisible by 100")
    elif year % 400 == 0:
        print("this is a leap year because it is evenly divisible by 400")
else:
    print("Not a leap year because its not divisible by 4")

# summary of rules for leap year:
# The rule is that if the year is divisible by 100 and not divisible by 400, leap year is skipped.
