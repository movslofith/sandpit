celebs = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]
print(celebs)
print(len(celebs))

for (nm, yr) in celebs:
    if yr < 1980:
        print(nm)

