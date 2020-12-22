layout = "{0:>4}{1:>6}{2:>6}{3:>6}{4:>6}{5:>6}{6:>6}{7:>6}{8:>6}{9:>6}{10:>6}{11:>6}"

for i in range(1, 13):
    for j in range (1, 13):
        print("{0:>5}".format(i * j), end="")
    print()
    