with open('numbers.txt', 'r') as file:
    # Read each line in the file
    total = 0
    for line in file:
        line="".join(c for c in line if  c.isdecimal())
        # Print each line
        if int(line) < 10:
            line += line
        num = float(line)
        total += num
    print(total)
