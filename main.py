#sets score to 0
imp=0
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
    imp=imp+1
    q1=input("when did the first world war start?")
elif q1==""and imp==1:
    imp=imp+1
    print("did you press enter by accident or something?")
    q1 = input("When did the first world war start")
elif q1==""and imp==2:
    imp=imp+1
    print("Bro this isn't funny, just answer the question")
    q1 = input("When did the first world war start")
elif q1==""and imp==3:
    imp=imp+1
    print("Alright if you dont answer the question im gonna count to 5")
    print("& when i get to 5, i'm gonna stop the quiz")
    q1 = input("When did the first world war start")
elif q1==""and imp==4:
    imp=imp+1
    print("1")
    q1 = input("When did the first world war start")
elif q1==""and imp==5:
    imp=imp+1
    print("2")
    q1 = input("When did the first world war start")
elif q1==""and imp==6:
    imp=imp+1
    print("3")
    q1 = input("When did the first world war start")
elif q1==""and imp==7:
    imp=imp+1
    print("4")
    q1 = input("When did the first world war start")
elif q1==""and imp==8:
    imp=imp+1
    print("alright, I warned you, goodbye!")
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
if q5=="Truman" or "truman" or "Harry Truman" or "harry Truman" or "Harry truman":
    print("Correct! Harry Truman was the one who bombed hiroshima & nagasaki")
    score=score+1
elif q5=="URDDD":
    print("The correct answer is Harry Truman.")
elif q5=="":
    print("no clue huh?")

else:
    print("Incorrect! the correct answer is Harry Truman")
#end quiz
print("anyways thats the end of the quiz")
print("have a nice day!")