import random

doors=[0]*3
goatdoor=[0]*2
swap=0#No of swap wins
dont_swap=0 #No of dont swap wins
j=0
while(j<10):
    x=random.randint(0,2)#xth door will comprise of BMW
    doors[x]="BMW"
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice "))
    door_open=random.choice(goatdoor) #open adoor that comprisesof goat
    while(door_open==choice):#door_open shouldn't be equal to choice made by the participant
        door_open=random.choice(goatdoor)
    ch= input("do u want to swap? y/n ")
    if(ch=='y'):
        if(doors[choice]=='Goat'):
            print("Player wins")
            swap+=1
        else:
            print("Player lost")
    else:
        if(doors[choice]=='Goat'):
            print("Player Lost")
        else:
            print("Player Win")
            dont_swap+=1

print (swap)
print(dont_swap)
