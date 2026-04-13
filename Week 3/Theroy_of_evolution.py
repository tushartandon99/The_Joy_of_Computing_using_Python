with open("D:\coding\python\Joy of computing using python\Week 3\file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()