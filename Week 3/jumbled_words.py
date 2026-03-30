import random
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,'Your score is : ',p1)
    print(p2n,'Your score is : ',p2)
    print('Thank You')

def play():
    p1name=input("player 1 please enter your name :")
    p2name=input("player 2 please enter your name :")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_words=choose()
        #create question
        qn=jumble(picked_words)
        print (qn)
        #player 1
        if turn%2==0 :
            print(p1name, 'Your turn')
            ans=input('What is on my mind ?')
            if ans==picked_words:
                pp1+=1
                print ('Your score is :',pp1)
            else:
                print('Better luck next time, I thought:',picked_words)
            c=input('Press 1 to continue and 0 to quit : ')
            if c=="0":
                thank(p1name,p2name,pp1,pp2)
                break
        #player 2
        else:
            print(p2name, 'Your turn')
            ans=input('What is on my mind ?')
            if ans==picked_words:
                pp2+=1
                print ('Your score is :',pp2)
            else:
                print('Better luck next time, I thought:',picked_words)
            c=input('Press 1 to continue and 0 to quit : ')
            if c=="0":
                thank(p1name,p2name,pp1,pp2)
                break
        turn+=1
play()
        