#This is a 5 questions physics quiz
import csv

#This is the list of questions with the correct answer at the end of each question.
qa = {'Which of the following speeds is faster': 'speed of light',
      'Protons, neutrons and elections all orbit the ____.': 'nucleus',
      'As an ambulance drives past, you notice the pitch of its siren changing. This is caused by the ___ effect.': 'doppler',
      'What are sounds below 20 Hz known as?': 'infrasound',
      'The sun is mainly composed of which two elements?': 'hydrogen and helium'}

#This is the answers list with 3 options of answers for each question.
options = [['speed of light', 'speed of sound', 'speed of electricity'],
           ['nucleus', 'cells', 'monochromes'],
           ['light', 'doppler', 'sound'],
           ['infrasound', 'ultrasound', 'audiblefrequency'],
           ['hydrogen and helium', 'green house gas and helium', 'helium and gas']]
#This is instructions for the user and asking for user's name.
def user_details():
    print('Hey!, Welcome to the physics quiz, this quiz contains 5 physics questions for revision on the topic of waves.')
    print('Please note to answer the question with a number from 1-3 and do not include a "." after the number.')
    name = input("Enter your name: ")
    return name
#This is a function which is using the k and v, k means outputing the question and the value is the number of the answer which is correct.
def quiz(options, qa, name):
    score = 0
    opt_num = 0
    for k, v in qa.items():
        print(k)
        print('Options: ')
        for i, option in enumerate(options[opt_num]):
            print(f'{i + 1}. {option}')
        opt_num += 1
        ans = int(input('Enter the option number for your answer: '))
        if options[opt_num - 1][ans - 1] == v:
            score += 1
            print('Correct!')
        else:
            print('Incorrect!')
        print('Score:', score)

#This print statement will disply the final score of the quiz.
    print('Your final score is', score)

#Example usage
name = user_details()
quiz(options, qa, name)
