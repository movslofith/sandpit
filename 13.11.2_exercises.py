def snake_lines(file):
    """ prints only lines from file containing the substring snake
    """
    infile = open(file, "r")
    list_of_lines = []
    while True:
        text = infile.readline()
        if len(text) == 0:
            break
        if "snake" in text:
            list_of_lines.append(text)
        
    for i in list_of_lines:
        j = i.replace('\n', '')
        print(j)

snake_lines("snakes_text.txt")
