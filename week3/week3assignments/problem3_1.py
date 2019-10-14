def problem3_1(txtfilename):
    text_file = open(txtfilename)
    total = 0
    for line in text_file:
        print(line ,end ="")
        for c in line:
            total+=1;
    print("\n\nThere are",total,"letters in the file.")
