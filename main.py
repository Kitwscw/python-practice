import random
QUESTION_FORMAT="“{}\nA:{} B:{} C:{} D: {}”"
GOOD_COMMENTS=[" good job!", f"Keep up the good work!"]
BAD_COMMENTS={f"do better! " f"try harder next time",}
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
replay="yes"
while replay== "yes":
    score=0
    #ask users name & saves
    user = input("whats your name?")
    if user=="":
        user="User"
    #greet user & introduce quiz
    print(f"Hello, {user} & welcome to this quiz")
    print("This quiz is about world history")
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
            if qa1== OPTIONS[0][ANSWERS[0]] or qa1== SHORT_OPTIONS[1].lower():
                print("Thats correct!")
                print(random.choice(GOOD_COMMENTS))
                score+=1
                break
            elif qa1=="":
                print("no clue huh?")
                qtries-=1
            elif  qa1 in OPTIONS[0] or qa1 in SHORT_OPTIONS:
                print("that isnt correct")
                print(random.choice(BAD_COMMENTS))
                qtries-=1
            else:
                print("that wasnt even an option")
                qtries-=1
    #question 2
    print("Your second question is,")
    q2tries=tries
    while q2tries>0:
        qa2=input (QUESTION_FORMAT .format(QUESTIONS[1], OPTIONS[1][0], OPTIONS[1][1], OPTIONS[1][2], OPTIONS[1][3])).lower()
        if qa2== OPTIONS[1][ANSWERS[0]] or qa2==SHORT_OPTIONS[ANSWERS[1]] .lower():
            print("Correct! the first consul was Napoleon")
            score+=1
            break
        elif qa2 in OPTIONS[1] or qa2 in SHORT_OPTIONS:
            print("that aint it mate")
            q2tries-=1
        elif qa2=="":
            print("no clue huh?")
            q2tries-=1
        else:
            print(random.choice(BAD_COMMENTS))
            q2tries-=1
    #question 3
    print("your third question is,")
    q3tries=tries
    while q3tries>0:
        qa3=input(QUESTION_FORMAT .format ( QUESTIONS[2], OPTIONS[2][0], OPTIONS[2][1],OPTIONS[2][2], OPTIONS[2][3] )).lower()
        if qa3== OPTIONS[2][ANSWERS[2]] or qa3==SHORT_OPTIONS[ANSWERS[2]]:
            print("correct! the UN was formed in 1945")
            score+=1
            break
        elif qa3=="":
            print("no clue huh?")
            q3tries-=1
        elif qa3 in OPTIONS[2] or qa3 in SHORT_OPTIONS[2] :
            print("that isnt right bro")
            q3tries-=1
        else:
            print("that wasnt even an option")
    #question 4
    print("your fourth question is,")
    q4tries=tries
    while q4tries>0:
        q4=("when did the American revolutionary war start?")
        a4=("1775")
        b4=("1234")
        c4=("1886")
        d4=("1764")
        qa4=input(QUESTION_FORMAT .format (q4, a4, b4, c4, d4,)).lower()
        if qa4== a4 or qa4== "a".lower():
            print("Correct! the american revolutionary war started in 1775")
            score+=1
            break
        elif q4=="":
            print("no clue huh?")
            q4tries-=1
        elif qa4!= a4 and qa4!= b4 and qa4 != c4 and qa4!= d4:
            print("thats not even an answer bro")
            q4tries-=1
    #question 5
    print("your fifth question is,")
    q5tries=tries
    while q5tries>0:
        q5=input("who gave the order to bomb Hiroshima & Nagasaki").lower()
        if q5=="Harry Truman".lower() or q5=="Truman".lower():
            print("Correct! Harry Truman was the one who bombed hiroshima & nagasaki")
            score+=1
            break
        elif q5=="":
            print("no clue huh?")
            q5tries-=1
    #question 6
    print("your sixth question is,")
    q6tries=tries 
    while q6tries>0:
        q6=input("who came up with the modern concept of communism?").lower()
        if q6=="karl marx".lower() or q6=="marx".lower():
            print("correct! karl marx came up with the moden concept of communism")
            score+=1
            break
        elif q6=="":
            print("no clue huh?")
        else:
            print("Incorrect! the creator of modern communism is Karl Marx")
    #question 7
    q7tries=tries
    while q7tries>0:
        print("your seventh question is,")
        q7=input("who was the king of england famous for having 6 wives?").lower()
        if (q7=="henry".lower()) and "king".lower() in q7 :
            print("Correct! King henry the 8th is the right answer")
            score+=1
            break
        elif q7=="":
            print("no clue huh?")
            q7tries-=1
        else:
            print("Incorrect! the right answer was King henry the 8th")
            q7tries-=1
    #question 8
    q8tries=tries
    while q8tries>0:
        print("your eigth question is,")
        q8=input("when was ww2?")
        if q8=="1939-1945":
            print("Correct! the 2nd world war was between 1939-1945")
            score+=1
            break
        elif q8=="":
            print("no clue huh?")
            q8tries-=1
        else:
            print("Incorrect! WWII was between 1939 & 1945")
            q8tries-=1
    #question 9
    q9tries=tries
    while q9tries>0:
        print("your ninth question is,")
        q9=input("What was the capiatal of the empire that ruled the Mediterranean?").lower()
        if q9=="Rome".lower():
            print("Correct, the capital was rome")
            score+=1
            break
        elif q9=="":
            print("no clue huh?")
            q9tries-=1
        else:
            print("Incorrect! the capital was Rome")
            q9tries-=1
    #question 10
    q10tries=tries
    while q10tries>0:
        print("your final question is,")
        q10=input("who is the current prime minister of new zealand").lower()
        if q10=="Christopher Luxon".lower() or q10=="eggman":
            print("Correct! the current pm is christopher luxon")
            score+=1
            break
        elif q10=="":
            print("no clue huh?")
            q10tries-=1
        else:
            print("Incorrect! the current PM is christopher luxon, unless it isnt")
            q10tries-=1
    print(f"anyways thanks for playing the quiz {user}, you got {score} points")
    replay=input("do you want to play again?")
print("have a nice day!")