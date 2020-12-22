def grade(m):
    if 75 <= m <= 100:
        return "First"
    elif 70 <= m < 75:
        return "Upper Second"
    elif 60 <= m < 70:
        return "Second"
    elif 50 <= m < 60:
        return "Third"
    elif 45 <= m < 50:
        return "F1 Supp"
    elif 40 <= m < 45:
        return "F2"
    elif 0 <= m < 40:
        return "F3"
    else:
        print("You can't have gotten that score")

#mark = int(input("What mark did you get? "))

#print("Your grade was a", grade(mark))

mark_list = [3, 56, 78, 35, 74, 23, 53, 72, 94, 23, 45, 67, 39, 76]

for i in range(len(mark_list)):
    print("Your mark was", mark_list[i], "Your grade was a", grade(mark_list[i]))

