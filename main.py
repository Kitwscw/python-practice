import random
QUESTION_FORMAT="“{}\nA:{} B:{} C:{} D: {}”"
GOOD_COMMENTS=[" good job!", f"Keep up the good work!"]
BAD_COMMENTS={"do better! " "try harder next time",}
#if you want to add a new question, just add the question to the questions list
#then add the answer to the options list
QUESTIONS=["When did the first world war start",
           "who was the first consul of france during the napoleonic wars?",
           "when was the UN formed?",
           "when did the American revolutionary war start?",
           "who gave the order to bomb Hiroshima & Nagasaki",
           "who came up with the modern concept of communism?",
           "who was the king of england famous for having 6 wives?",
           "when was ww2?",
           "What was the capiatal of the empire that ruled the Mediterranean?",
           "who is the current prime minister of new zealand"]
OPTIONS=[["1834", "1914", "1956", "1239"], 
         ["Napoleon", "Marie Antoinette", "Cambacérès", "Lebrun"],
         ["1985", "1887","1945","3500BCE"],
         ["1775","1234","1886","1764"],
         ["JFK","Abraham Lincoln","Ronald Reagan","Harry Truman"],
         ["Karl Marx","Vladimir Lenin","Joseph Stalin","Ho Chi Minh"],
         ["Charlemagne","King Henry VIII","King Henry VII"," Louis XIV"],
         ["1746-1846","1846-1852","1914-1918","1939-1945"],
         ["Constantinople","carthage","Rome","Alexandria"],
         ["Christopher luxon", "winston Peters","Rishi Sunak", "David Seymour"]]
SHORT_OPTIONS=["a","b","c","d"]
ANSWERS=[1,0,2,0,3,0,1,3,2,0]
#sets score to 0
score=0
#ask users name & saves
user = input("whats your name?")
if user=="":
        user="User"
#greet user & introduce quiz
print(f"Hello, {user} & welcome to this quiz")
print("This quiz is about world history")
replay="yes"
while replay== "yes":
    
    while True:
        try:
            tries=int( input("how many tries would you like for eack question? 1-3"))
            break
        except:
            print("that aint a number mate")
    #ask user a question
    print("Your first question is,")
    for i in range(len(QUESTIONS)):
        qtries=tries
        while qtries>0:
            qa1=input(QUESTION_FORMAT .format ( QUESTIONS[i], OPTIONS[i][0], OPTIONS[i][1], OPTIONS[i][2], OPTIONS[i][3] )).lower()
            if qa1== OPTIONS[i][ANSWERS[i]] or qa1== SHORT_OPTIONS[ANSWERS[i]].lower():
                print("Thats correct!")
                print(random.choice(GOOD_COMMENTS))
                score+=1
                break
            elif qa1=="":
                print("no clue huh?")
                qtries-=1
            elif  qa1 in OPTIONS[i] or qa1 in SHORT_OPTIONS:
                print("that isnt correct")
                qtries-=1
            else:
                print("that wasnt even an option")
                qtries-=1
    print(f"anyways thanks for playing the quiz {user}, you got {score} points")
    replay=input("do you want to play again?")
print("have a nice day!")