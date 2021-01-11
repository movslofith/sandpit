def file_line_unnumbering(file, numbered_file):
    """ returns file from numbered_file with 4-digit leading number removed
    """
    with open(file, 'w') as f:
        with open(numbered_file) as n_f:
            text = n_f.read().splitlines()
            for line in text:
                new_line = line[5:]
                f.write(new_line + '\n')
                
    print(text)

file_line_unnumbering("unnumbered_this.txt", "numbered_this.txt")