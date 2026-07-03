#Simple quiz game
print("Welcome to this simple quiz game")
questions=("What is the capital of France?",
           "Which planet is known as the Red Planet?",
           "How many days are there in a leap year?",
           "Which animal is known as the King of the Jungle?",
           "What is the largest ocean on Earth?")

options=(("A. Berlin","B. Madrid","C. Paris","D. Rome"),
         ("A. Venus","B. Mars","C. Jupiter","D. Saturn"),
         ("A. 364","B. 365","C. 366","D. 367"),
         ("A. Tiger","B. Elephant","C. Lion","D. Leopard"),
         ("A. Atlantic Ocean","B. Indian Ocean","C. Arctic Ocean","D. Pacific Ocean"),)

answer=('C','B','C','C','D')
score=0
ans=[]
sa="l"
question_no=0
for question in questions:
    print("-----------------------")
    print(question)
    for option in options[question_no]:
        print(option)
    sa=input("Answer(A,B,C,D):").upper()
    ans.append(sa)
    if ans[question_no]==answer[question_no]:
        score+=1
    question_no += 1
print(f"your score is {score}/5")
print("your answers were:")
for a in ans:
    print(a,end=' ')
print("The correct answers are:")
for x in answer:
    print(x,end=' ')