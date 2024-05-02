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
elif q1!="1914":
    print("Incorrect, the first world war started in 1914")
#end quiz
print("anyways thats the end of the quiz")
print("have a nice day!")