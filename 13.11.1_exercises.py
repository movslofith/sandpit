def reverse_file_by_lines(oldfile, newfile):
    """returns newfile which contains all the lines from oldfile with the order of lines reversed
    """
    infile = open(oldfile, "r")
    outfile = open(newfile, "w")
    list_of_lines = []
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if "\n" not in text:
            text = text + '\n'
        list_of_lines.append(text)

    list_of_lines.reverse()

    for i in list_of_lines:
        outfile.write(i)


    infile.close()
    outfile.close()

reverse_file_by_lines("this.txt", "reversethis.txt")

#print(count_file_lines("this.txt"))
