print(" Welcome to the Quiz Game")
player = input("Enter the name: ")
Questions = [
    "Q1:which city is the capital of india",
    "Q2:which man is known as missile man in india",
    "Q3:which man is considered god of cricket in india",
    "Q4:who is the indian football player with feat of one of the most goals scored",
    "Q5:who is called father of nation in india"
    ]

Answers = [
    "delhi",
    "abdul kalam",
    "sachin ",
    "sunil",
    "Gandhi"
]

# print(Questions[0])
# user_name1 = input("Enter your answer: ")
# print(Questions[1])
# user_name2 = input("Enter your answer: ")
# print(Questions[2])
# user_name3 = input("Enter your answer: ")
# print(Questions[3])
# user_name4 = input("Enter your answer: ")
# print(Questions[4])
# user_name5 = input("Enter your answer: ")


# if user_name1 == Answers[0]:
#     print("correct answer")

# if user_name2 == Answers[1]:
#     print("correct answer")

# if user_name3 == Answers[2]:
#     print("correct answer")

# if user_name4 == Answers[3]:
#     print("correct answer")

# if user_name5 == Answers[4]:
#     print("correct answer")

# else:
#     print("wrong answer")

# this all is manual logic and very fundamntal program

# NOW i will try to make this code much more efficent
score = 0
for i in range(len(Questions)):


    print(Questions[i])

    user_input = input("Enter your answer:  ")

    if user_input.lower() == Answers[i].lower():
       print("correct")
       score += 1

else:
    print("wrong answer")

print("your final score is:",score)

total_questions = len(Questions)

percentage = print(score/total_questions) * 100

print("your percentage:",percentage,"%")
