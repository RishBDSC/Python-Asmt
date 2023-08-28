#This is a 5 question physics quiz
#Instructions to the user.
print('Welcome to the quick and fun physics quiz!')
print('NOTE: if yourspelling is incorrect then it is considered as wrong answer')
print('AND do not use capitals')

#Numbering the question
question_no = int()
#Asking the user if they want to play through entering in "yes".
playing = input('Do you want to play ? (Enter in yes to START)')
if playing == 'yes':

# Question 1-
    ques = input(f'\n{question_no}.  There are 4 states of matter in physics: gas, liquid, solid, and ____ ').lower()
# Answer
    if ques == 'speed':
        print('correct!')
        
    else:
        print('Incorrect!')
        # Displying the correct answer if the user gets the answer wrong.
        print(f'Correct answer is --> speed')
        
# Question 2
    ques = input(f'\n{question_no}. Protons, neutrons and elections all orbit the ____. ').lower()
# Answer
    if ques == 'nucleus':
        print('correct!')
        
    else:
        print('Incorrect!')
        # Displying the correct answer if the user gets the answer wrong.
        print(f'Correct answer is --> nucleus')
        
# Question 3
    ques = input(f'\n{question_no}. As an ambulance drives past, you notice the pitch of its siren changing. This is caused by the ___ effect. ').lower()
# Answer  
    if ques == 'doppler':
        print('correct!')
        
    else:
        print('Incorrect!')
        # Displying the correct answer if the user gets the answer wrong.
        print(f'Correct answer is --> doppler')
        
# Question 4
    ques = input(f'\n{question_no}. What are sounds below 20 Hz known as? ').lower()
# Answer
    if ques == 'infrasound':
        print('correct!')
        
    else:
        print('Incorrect!')
        # Displying the correct answer if the user gets the answer wrong.
        print(f'Correct answer is --> infrasound')
        
# Question 5
    ques = input(f'\n{question_no}. What does a vector quantity have that a scalar quantity lacks? ').lower()
# Answer   
    if ques == 'direction':
        print('correct!')
        
    else:
        print('Incorrect!')
        # Displying the correct answer if the user gets the answer wrong.
        print(f'Correct answer is --> direction')


# Print Statement with a good job message representing that the quiz is completed.
    print('Good Job you have completed the quiz!!!')
    quit()


