students = [("John", ["CompSci", "Physics"]), 
("Vusi", ["Maths", "CompSci", "Stats"]), 
("Jess", ["CompSci", "Accounting", "Economics", "Management"]), 
("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]), 
("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

counter = 0

for (name, subjects) in students:
    if "CompSci" in subjects:
        counter += 1

print("The number of students taking Computer Science is", counter)