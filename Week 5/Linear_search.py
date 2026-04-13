def linear_search(n,x):
    element=[]
    for i in range (1,n):
        element.append(i)
    flag =0
    count =0
    for i in element:
        count+=1
        if(i==x):
            print("Found at : "+str(i))
            flag=1
            break;

    if(flag ==0):
        print("Not Found")

    print (count)

linear_search(1001,57)