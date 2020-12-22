fruit = "banana"

ix = 0
while ix < len(fruit):
    letter = fruit[ix]
    print(letter)
    ix += 1

for c in fruit:
    print(c)

prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    print(p + suffix)



print(fruit[:3])
print(fruit[:])
print(fruit[0:1], fruit[3:4])