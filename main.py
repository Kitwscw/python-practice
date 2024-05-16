QUESTION_FORMAT="“{}\nA:{} B:{} C:{} D: {}”"
#sets score to 0 & deactivates devmode
replay="yes"
while replay== "yes":
    score=0
    devmode=False
    #ask users name & saves
    name=input("whats your name?".lower)
    #greet user & introduce quiz
    print(f"Hello, {name} & welcome to this quiz")
    print("This quiz is about world history")
    #ask user a question
    print("Your first question is,")
    q1 = "When did the first world war start"
    a= "1832"
    b= "1914"
    c= "1926"
    d= "1980"
    qa1=input(QUESTION_FORMAT .format ( q1, a, b, c, d )).lower()
    #check if user was correct, then tell user correct answer
    if qa1== b or qa1== "b".lower:
        print("Correct! the first world war started in 1914")
        score=score+1
    elif qa1=="":
        print("no clue huh?")
        q1=input(QUESTION_FORMAT .format ( q1, a, b, c, d )).lower()
    elif  qa1!=a and qa1!=b and qa1!=c and qa1!=d:
        print("Bro that wasn't even an option")
    else:
        print("Incorrect, the first world war started in 1914")
    #question 2
    print("Your second question is,")
    q2=input("who was the first consul of france during the napoleonic wars?".lower)
    if q2=="napoleon".lower:
        print("Correct! the first consul was Napoleon")
        score=score+1
    elif q2=="URDDD":
        print("The correct answer is Napoleon.")
    elif q2=="":
        print("no clue huh?")
        imp=imp+1
        q2=input("who was the first consul of france during the napoleonic wars?".lower)
    else:
        print("Incorrect! the first consul was Napoleon")
    #question 3
    print("your third question is,")
    q3=("when was the UN formed?")
    a3=("1937")
    b3=("1956")
    c3=("1936")
    d3=("1945")
    qa3=input(QUESTION_FORMAT .format ( q3, a3, b3, c3, d3 )).lower()
    if qa3== d3 or qa3== "d":
        print("correct! the UN was formed in 1945")
        score=score+1
    elif qa3!=a3 and qa3!=b3 and qa3!=c3 and qa3!=d3:
        print("bro that wasnt even an answer")
    elif qa3=="":
        print("no clue huh?")
    else:
        print("Incorrect! the un was formed in 1945")
    #question 4
    print("your fourth question is,")
    q4=("when did the American revolutionary war start?")
    a4=1775
    b4=1234
    c4=1886
    d4=1764
    qa4=input(QUESTION_FORMAT .format (q4, a4, b4, c4, d4,)).lower()
    if qa4== a4 or qa4== "a".lower:
        print("Correct! the american revolutionary war started in 1775")
        score=score+1
    elif qa4!= a4 and qa4!= b4 and qa4 != c4 and qa4!= d4:
        print("thats not even an answer bro")
    elif q4=="":
        print("no clue huh?")
    else:
        print("Incorrect! the american revolutionart war started in 1775")
    #question 5
    print("your fifth question is,")
    q5=input("who gave the order to bomb Hiroshima & Nagasaki".lower)
    if q5=="Harry Truman".lower or q5=="Truman".lower:
        print("Correct! Harry Truman was the one who bombed hiroshima & nagasaki")
        score=score+1
    elif q5=="URDDD":
        print("The correct answer is Harry Truman.")
    elif q5=="":
        print("no clue huh?")
    else:
        print("Incorrect! the correct answer is Harry Truman")
    #question 6
    print("your sixth question is,")
    q6=input("who came up with the modern concept of communism?".lower)
    if q6=="karl marx".lower or q6=="marx".lower:
        print("correct! karl marx came up with the moden concept of communism")
        score=score+1
    elif q6=="":
        print("no clue huh?")
    else:
        print("Incorrect! the creator of modern communism is Karl Marx")
    #question 7
    print("your seventh question is,")
    q7=input("who was the king of england famous for having 6 wives?".lower)
    if (q7=="henry".lower) and "king".lower in q7 :
        print("Correct! King henry the 8th is the right answer")
        score=score+1
    elif q7=="":
        print("no clue huh?")
    else:
        print("Incorrect! the right answer was King henry the 8th")
    #question 8
    print("your eigth question is,")
    q8=input("when was ww2?")
    if q8=="1939-1945":
        print("Correct! the 2nd world war was between 1939-1945")
        score=score+1
    elif q8=="":
        print("no clue huh?")
    else:
        print("Incorrect! WWII was between 1939 & 1945")
    #question 9
    print("your ninth question is,")
    q9=input("What was the capiatal of the empire that ruled the Mediterranean?")
    if q9=="Rome" or q9== "rome":
        print("Correct, the capital was rome")
        score=score+1
    elif q9=="":
        print("no clue huh?")
    else:
        print("Incorrect! the capital was Rome")
    #question 10
    print("your final question is,")
    q10=input("who is the current prime minister of new zealand".lower)
    if q10=="Christopher Luxon".lower or q10=="eggman":
        print("Correct! the current pm is christopher luxon")
        score=score+1
    elif q10=="":
        print("no clue huh?")
    else:
        print("Incorrect! the current PM is christopher luxon, unless it isnt")
    print(f"anyways thanks for playing the quiz {name}, you got {score} points")
    replay=input("do you want to play again?")
print("have a nice day!")