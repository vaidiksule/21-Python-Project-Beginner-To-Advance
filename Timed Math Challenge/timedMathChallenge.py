import random as rd
import time

operators = ['+', '-', '*']

#For Difficulty
maximum_value = 2
minimum_value = 23
no_of_questions = 10

input("Press any key to start!")
start_time = time.time()
right_answers = 0

for question in range(0, no_of_questions):
    
    print("Question #" + str(question+1))
    
    LEFT = rd.randint(maximum_value, minimum_value)
    RIGHT = rd.randint(maximum_value, minimum_value)

    expression = str(LEFT) + ' ' + rd.choice(operators) + ' '  + str(RIGHT)
    answer = input(expression + ': ')

    corrent_answer = eval(expression)
    if str(corrent_answer) == answer:
        right_answers += 1


end_time = time.time()
total_time = round(end_time - start_time, 2)
print("-"* 20)
print("You got " + str(right_answers) + " correct out of " + str(no_of_questions) + "\n and you took " + str(total_time) + "seconds")