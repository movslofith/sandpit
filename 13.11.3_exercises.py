def file_line_numbering(file, numbered_file):
    """ returns numbered_file from file with lines given 4-digit leading line number
    """
    with open(file) as f:
        with open(numbered_file, 'w') as n_f:
            text = f.read().splitlines()
            for line in text:
                line_number = text.index(line)
                new_line = str(line_number).zfill(4) + " " + line
                n_f.write(new_line + '\n')
                
    print(text)

file_line_numbering("this.txt", "numbered_this.txt")