from data import useful_data
from question_model import Question
from quiz_brain import QuizBrain


questions_list=[]
for data in useful_data:
    questions_list.append(Question(data["question"],data["correct_answer"]))
#creates all the "Question" objects ^
pontuation=0
for index,question in enumerate(questions_list):
    user_answer=input(f"{index+1} Question :'{question.getQuestion()}' is (True\False) ? \n Answer : ").lower()
    if user_answer==question.getAnswer().lower():
       pontuation+=1
       print("\nThats Correct !!!! :D \n")
    else:
        print("\nSorry thats wasnt the Answer ;-; \n")
    print(f"Pontuation {pontuation} of {index+1}\n")
#shows to user all the questions and checks the answer ^
print(f"""\t ---End of the Game ---
You got {pontuation} of {len(questions_list)}""")