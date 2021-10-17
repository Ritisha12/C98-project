def swapFileData():
    file1=input("Enter file name 1:")
    file2=input("Enter file name 2:")
   # with open (file1,"r") as file1
    f1=open(file1,"r")
    data_a=f1.read()

    f2=open(file2,"r")
    data_b=f2.read()

    f1=open(file1,"w")
    f1.write(data_b)

    f2=open(file2,"w")
    f2.write(data_a)

swapFileData()
