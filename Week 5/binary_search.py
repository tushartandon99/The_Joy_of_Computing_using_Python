def binary_search(n,x):
    element=[]
    for i in range (1,n):
        element.append(i)
    flag=0
    count=0
    first =0
    last=n-1
    while(first<=last):
        count+=1
        mid=(first+last)//2
        if(element[mid]==x):
            print("Found at : "+str(mid))
            print("In iterations = "+str(count))
            flag=1
            break;
        elif(x<element[mid]):
            last=mid-1
        else:
            first=mid+1

    if(flag ==0):
        print("Not Found")

binary_search(1001,57)
