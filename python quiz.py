print("Welcome to the quick and fun physics quiz!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
print('AND do not use capitals')

question_no =  int()
playing = input('Do you want to play ? (Enter in yes to START)')
if playing == 'yes':

# ------1
    ques = input(f'\n{question_no}. In the formula s=d/t, what does s stand for? ')
    if ques == 'speed':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> speed')

# ------2
    ques = input(f'\n{question_no}. Protons, neutrons and elections all orbit the ____. ')
    
    if ques == 'nucleus':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> nucleus')

# -----3
    ques = input(f'\n{question_no}. As an ambulance drives past, you notice the pitch of its siren changing. This is caused by the ___ effect. ')
    
    if ques == 'doppler':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> doppler')

# -----4
    ques = input(f'\n{question_no}. What are sounds below 20 Hz known as? ')
    
    if ques == 'infrasound':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> infrasound')


# -----5
    ques = input(f'\n{question_no}. What does a vector quantity have that a scalar quantity lacks? ')
    
    if ques == 'direction':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> direction')

# -----6
    ques = input(f'\n{question_no}. What is the most common unit for measuring pressure? ')
    
    if ques == 'pascals':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> pascals')

# -----7
    ques = input(f'\n{question_no}. What is the property of an object that can return to its original shape after deformation? ')
    
    if ques == 'elasticity':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> elasticity')

# -----8
    ques = input(f'\n{question_no}. What type of electromagnetic radiation has the lowest frequency? ')
    
    if ques == 'radio waves':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> radio waves')

# -----9
    ques = input(f'\n{question_no}. Lubrication can be used to limit the ____ between two objects. ')
    
    if ques == 'friction':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> friction')

# -----10
    ques = input(f'\n{question_no}. The sun is mainly composed of which two elements? ')
    
    if ques == 'hydrogen and helium':
        print('correct!')
        
    else:
        print('Incorrect!')
        print(f'Correct answer is --> hydrogen and helium')

# ------11

else:
    print('Good Job you have completed the quiz!!!')
    quit()


