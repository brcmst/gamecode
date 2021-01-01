import random

pics = ["""
      +------+
      |      |
             |
             |
             |
             |
       ======= ""","""
      +------+
      |      |
      O      |
             |
             |
             |
       ======= ""","""
      +------+
      |      |
      O      |
      |      |
             |
             |
       ======= ""","""
      +------+
      |      |
      O      |
     /|      |
             |
             |
       ======= ""","""
      +------+
      |      |
      O      |
     /|\     |
             |
             |
       ======= ""","""
      +------+
      |      |
      O      |
     /|\     |
     /       |
             |
       ======= ""","""
      +------+
      |      |
      O      |
     /|\     |
     / \     |
             |
       ======= """]


while True:
    print(("-" * 30) + "\nHangman Game\n" + ("-" * 30))

    word = random.choice(["windows","python","merhaba","burcu"])
    step = 0
    letters = []

    while True:
        print(pics[step])

        for i, char in enumerate(word):
            print(char if i in letters else "-")

        answer = input("\nAnswer:")  #raw_input() ile kullanıcıdan bilgi alınır

        if answer == word:
            print("You win!!!!!!!!")
            break
        else:
            while True:
                rand = random.randint(0,len(word))
                if not rand in letters:
                    letters.append(rand)
                    break
            step +=1

        if step >= len(pics):
             print("You lose :(")
             break
    if not "y" == input("Play again(yes-no): "):
        break




