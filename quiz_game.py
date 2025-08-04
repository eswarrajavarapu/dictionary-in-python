questions = {'The ability of one class to acquire methods and attributes of another class is called:':'A',
             'which of the following is a type of inheritance?':'C',
             'what type of inheritance has multiple subclasses  to a single superclass?': 'C',
             'what is the depth of multi level inheritance in python?': 'C',
             'what does MRO stand for?': 'B',}
options = {1:['A. Inheritance', 'B. Abstraction', 'C. Polymorphism', 'D. Objects'],
           2:['A. Single', 'B. Double', 'C. Multiple', 'D. Both A and C'],
           3:['A. Multiple Inheritance', 'B. Multilevel Inheritance', 'C. Hierarchical Inheritance', 'D. None of these'],
           4:['A. Two level', 'B. Three level', 'C. Any level', 'D. None of these'],
           5:['A. Method Recursive Object', 'B. Method Resolution Order', 'C. Main Resolution Order', 'D.Method Resolution Object']}
def options_loop(key_option):




    print(f'{options[key_option][0]}\n{options[key_option][1]}\n{options[key_option][2]}\n{options[key_option][3]}')





print('Welcome to my quiz game')
end_of_quiz = False
while not end_of_quiz:
    value = 1
    score  = 0

    for i in questions:
        print(i)
        options_loop(value)
        answer = input("Enter your answer: (A/B/C/D): ")
        if answer == questions[i]:
            score+=1

            print('Correct answer!')
            print(f'your score is {score}/{value}')

            if value == len(questions):
                end_of_quiz = True

        elif answer!= questions[i]:
            print('Incorrect answer!')
            print(f'your score is {score}/{value}')
        value += 1







