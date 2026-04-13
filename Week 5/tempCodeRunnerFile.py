    mid=(first+last)//2
        if(element[mid]==x):
            print("Found at : "+str(mid))
        elif(x<element[mid]):
            last=mid-1
        else:
            first=mid+1