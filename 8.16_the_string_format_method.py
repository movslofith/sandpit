s1 = "His name is {0}!".format("Arthur")
print(s1)

name = "Alice"
age = 10
s2 = "I an {1:^20} and I am {0} years old.".format(age, name) # <, ^, > controls if the field is aligned left, center or right, field width is determined by the number after the :, alignment must proceed field width
print(s2)

n1 = 4
n2 = 5
s3 = "2**10 = {0:x} and {1} * {2} = {3:.1f}".format(2**10, n1, n2, n1*n2) # ':x' converts to hexadecimal, ':f' to float, ':.2f' a float to 2 decimal places
print(s3)

n1 = "Paris"
n2 = "Whitney"
n3 = "Hilton"

print("Pi to three decimal places is {0:.3f}".format(3.14159))
print("|||{0:<15}|||{1:^15}|||{2:>15}|||Born in {3}|||".format(n1, n2, n3, 1981))
print("The decimal value {0} converts to hex value {0:x}".format(123456))

# the real utility of string formating - illustrated by printing a table

print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i,"\t",i**2,"\t",i**3,"\t",i**5,"\t",i**10,"\t",i**20)

layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(layout.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(layout.format(i, i**2, i**3, i**5, i**10, i**20))