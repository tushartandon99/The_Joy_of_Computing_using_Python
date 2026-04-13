import string
dict ={}
data=""
file=open("D:\coding\python\Joy of computing using python\Week 6\op_file.txt","w")
for i in range (len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print (dict)
with open ("D:\coding\python\Joy of computing using python\Week 6\demo.text") as f:
    while True:
        c=f.read(1)
        if not c:
            print ("end of file")
            break;
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
        print (data)
file.close()












# x="Hello World"
# print(x[0:4])
# print(len(x))
# print(x.upper())
# print(x.replace("H","J"))
# print(x)