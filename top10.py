guesses=[]
TOP10_ANSWERS=["minecraft",
               "gta5",
               "gtav",
               "grand theft auto 5",
                "grand theft auto v",
                "tetris",
                "wii sports",
                "wiisports",
                "pubg",
                "mario kart 8",
                "red dead redemtion 2",
                "super mario bros",
                "overwatch",
                "human fall flat"]
#-----FUNCTIONS-----
def intro():
    print("Hello!")
    nam = input("What's your name?")
    print("nice to meet you {}! & welcome to this quiz".format(nam) )
def getlives():
    while True:
        lives=input("how many tries would you like? 1-10")
        try:
            lives=int(lives)
            if lives >0 and lives<10:
                return lives
        except:
            print("that isn't a number")
def correct(answer, list):
    if answer in list:
        return True
    else:
        return False
#-----MAIN CODE-----

score=0
intro()
lives=getlives()
while lives>0:
    ans=input("What are the top 10 most sold games?").lower()
    if correct(ans, TOP10_ANSWERS):
        if correct(ans, guesses):
            print("you've already guessed that")
        else:
            print("")
    else:
        print("incorrect!")
        lives-=1
print("Game over, you're out of lives. Your score was{}".format(score))