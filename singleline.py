def single_line(txtfile):  ##textfile format: "hackinit.txt"
    file = open(txtfile,"r") 
    string = file.read()
    file.close()
    filelist = list(string)
    for i in range(len(filelist)):
        if filelist[i] == "\n":
            filelist[i] = " "
    newstring = "".join(filelist)


    f2 = open("newtextfile.txt", "w")##create a new file
    f2.write(newstring)
    f2.close()
