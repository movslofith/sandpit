students = [("John", ["CompSci", "Physics"]), 
("Vusi", ["Maths", "CompSci", "Stats"]), 
("Jess", ["CompSci", "Accounting", "Economics", "Management"]), 
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]), 
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# print all students with a count of their courses
for (name, subjects) in students:
    print(name, "takes", len(subjects), "courses")

# count how many students are taking CompSci
counter = 0
for (name, subjects) in students:
    for s in subjects:
        if s == "CompSci":
            counter += 1

print("The number of students taking CompSci is", counter)