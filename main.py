#sets score to 0
score=0
#ask users name & save
name=input("whats your name?")
#greet user & introduce quiz
print(f"Hello, {name} & welcome to this quiz")
print("This quiz is about world history")
#ask user a question
print("Your first question is,")
q1 = input("When did the first world war start")
#check if user was correct, then tell user correct answer
if q1=="1914":
    print("Correct! the first world war started in 1914")
    score=score+1
elif q1=="URDDD":
    print("The correct answer is 1914.")
elif q1=="":
    print("no clue huh?")
    q1=input("when did the first world war start?")

else:
    print("Incorrect, the first world war started in 1914")
#question 2
print("Your second question is,")
q2=input("who was the first consul of france during the napoleonic wars?")
if q2=="napoleon":
    print("Correct! the first consul was Napoleon")
    score=score+1
elif q2=="URDDD":
    print("The correct answer is Napoleon.")
elif q2=="":
    print("no clue huh?")
    imp=imp+1
    q2=input("who was the first consul of france during the napoleonic wars?")
else:
    print("Incorrect! the first consul was Napoleon")
#question 3
print("your third question is,")
q3=input("when was the UN formed?")
if q3=="1945":
    print("correct! the UN was formed in 1945")
    score=score+1
elif q3=="URDDD":
    print("The correct answer is 1945.")
elif q3=="":
    print("no clue huh?")
else:
    print("Incorrect! the un was formed in 1945")
#question 4
print("your fourth question is,")
q4=input("when did the American revolutionary war start?")
if q4=="1775":
    print("Correct! the american revolutionary war started in 1775")
    score=score+1
elif q4=="URDDD":
    print("The correct answer is 1945.")
elif q4=="":
    print("no clue huh?")
else:
    print("Incorrect! the american revolutionart war started in 1775")
#question 5
print("your fifth question is,")
q5=input("who gave the order to bomb Hiroshima & Nagasaki")
if q5=="Truman" or q5 == "truman" or q5 == "Harry Truman" or q5 == "harry Truman" or q5 == "Harry truman":
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
q6=input("who came up with the modern concept of communism?")
if q6=="Karl marx" or q6== "Marx" or q6== "marx":
    print("correct! karl marx came up with the moden concept of communism")
    score=score+1
elif q6=="":
    print("no clue huh?")
else:
    print("Incorrect! the creator of modern communism is Karl Marx")
#question 7
print("your seventh question is,")
q7=input("who was the king of england famous for having 6 wives?")
if (q7=="henry"or q7== "Henry") and "king" or q7== "king" in q7 :
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
q10=input("who is the current prime minister of new zealand")
if q10=="Christopher Luxon" or q10=="eggman":
    print("Correct! the current pm is christopher luxon")
    score=score+1
elif q10=="":
    print("no clue huh?")
else:
    print("Incorrect! the current PM is christopher luxon, unless it isnt")
print(f"anyways thats the end of the quiz, you got {score} points")
print("have a nice day!")