start_day = int(input("What was the number of the day you left on? "))
number_of_sleeps = int(input("How many sleeps passed since then? "))

new_day = (start_day + number_of_sleeps) % 6 # determine the number of the day after the sleeps

def day_number(x):
    """Function to return the days of the week according to numbering 0 to 6"""
    if x < 0 or x > 6:
        print("Sorry we need a number between 0 and 6")
        return

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[x]

print("The day you started on was a", day_number(start_day))
print("The current day is a", day_number(new_day))
