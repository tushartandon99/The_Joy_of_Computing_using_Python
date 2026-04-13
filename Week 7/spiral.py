def spiral(m , n ,a):
    k=0
    l=0
    '''k=index of starting row
    l=index of starting column'''

    while(k<m and l<n):
        #Printing the first row from the remaining row
        for i in range (l,n):
            print(a[k][i], end=" ")

        k+=1
        #Printing the first column from the remaining columns
        for i in range (k,m):
            print(a[i][n-1], end=" ")

        n-=1

        if(k<m):
            # printing the last row from remaining row
            for i in range(n-1,l-1,-1):
                print(a[m-1][i], end =" ")

            m-=1

        if(l<n):
            #printing the last column form remaining columns
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1


a=[]
count=1
for i in range(4):
    l=[]
    for j in range (4):
        l.append (count)
        count+=1
    a.append(l)

spiral(4,4,a)