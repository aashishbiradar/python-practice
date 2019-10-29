try:
    f = open("samplefile.txt",'w')
    f.write("File created by python!\n")
    f.write("Line two.")
    f.close()
    
    #read complete file
    f = open("samplefile.txt")
    cursor_pos = f.tell()
    print(cursor_pos)

    contents = f.read()
    print(contents)

    cursor_pos = f.tell()
    print(cursor_pos)

    f.close()

finally:
    f.close()