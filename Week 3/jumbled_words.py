import random

# choose word
def choose():
    words = ["apple", "banana", "grapes", "mango", "orange"]
    return random.choice(words)

# jumble word
def jumble(word):
    return "".join(random.sample(word, len(word)))

# final result
def thank(p1, p2, s1, s2):
    print("\nFinal Scores:")
    print(p1, ":", s1)
    print(p2, ":", s2)

def play():
    p1name = input("Player 1 please enter your name: ")
    p2name = input("Player 2 please enter your name: ")

    pp1 = 0
    pp2 = 0
    turn = 0

    while True:
        picked_words = choose()
        qn = jumble(picked_words)
        print("\nJumbled word:", qn)

        if turn % 2 == 0:
            print(p1name, "Your turn")
            ans = input("What is on my mind? ")

            if ans == picked_words:
                pp1 += 1
                print("Correct! Score:", pp1)
            else:
                print("Wrong! I thought:", picked_words)

        else:
            print(p2name, "Your turn")
            ans = input("What is on my mind? ")

            if ans == picked_words:
                pp2 += 1
                print("Correct! Score:", pp2)
            else:
                print("Wrong! I thought:", picked_words)

        c = input("Press 1 to continue and 0 to quit: ")

        if c == "0":   # 👈 string compare
            thank(p1name, p2name, pp1, pp2)
            break

        turn += 1   # 👈 important

play()