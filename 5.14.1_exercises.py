n = int(input("Pick a number between 0 and 6: "))

def day_number(x):
    """Function to return the days of the week according to numbering 0 to 6"""
    if x < 0 or x > 6:
        print("Sorry we need a number between 0 and 6")
        return

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[x]

print("The day you have selected is", day_number(n))
