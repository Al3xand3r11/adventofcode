from word2number import w2n

with open('numbers.txt', 'r') as file:
    # Read each line in the file
    word = 'one'
    for line in file:
        if word in line:
            line = line.replace(word, "1")
            print(line)
        # line="".join(c for c in line if  c.isdecimal())
        # Print each line
        # if int(line) < 10:
        #    line += line
        # elif int(line) > 99:
        #    line = line[0] + line[-1]
        # num = float(line)
        # total += num
