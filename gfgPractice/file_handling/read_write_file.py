with open("read.txt" , "r") as input:

    with open("write.txt" , "w") as output:
        
        for lines in input:
            output.write(lines)
