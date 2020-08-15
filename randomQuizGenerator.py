#! python3
# Create 35 different Quizzes
# Create 50 multiple-choice questions for each quiz in random order
# Provide the correct answer and three random wrong answers in random order
# Write the quizzes to 35 text files
# write the answer keys to 35 text files

from pathlib import Path
import random
import os
import string

#the Quiz Data. Keys are States and values are their capitals
capitals = {
        'Alabama': 'Montgomery',
        'Alaska': 'Juneau',
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover',
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta',
        'Hawaii': 'Honolulu',
        'Idaho': 'Boise',
        'Illinois': 'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana': 'Baton Rouge',
        'Maine': 'Augusta',
        'Maryland': 'Annapolis',
        'Massachusetts': 'Boston',
        'Michigan': 'Lansing',
        'Minnesota': 'Saint Paul',
        'Mississippi': 'Jackson',
        'Missouri': 'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada': 'Carson City',
        'New Hampshire': 'Concord',
        'New Jersey': 'Trenton',
        'New Mexico': 'Santa Fe',
        'New York': 'Albany',
        'North Carolina': 'Raleigh',
        'North Dakota': 'Bismarck',
        'Ohio': 'Columbus',
        'Oklahoma': 'Oklahoma City',
        'Oregon': 'Salem',
        'Pennsylvania': 'Harrisburg',
        'Rhode Island': 'Providence',
        'South Carolina': 'Columbia',
        'South Dakota': 'Pierre',
        'Tennessee': 'Nashville',
        'Texas': 'Austin',
        'Utah': 'Salt Lake City',
        'Vermont': 'Montpelier',
        'Virginia': 'Richmond',
        'Washington': 'Olympia',
        'West Virginia': 'Charleston',
        'Wisconsin': 'Madison',
        'Wyoming': 'Cheyenne'
}

       # TODO: Create the quiz and answer key files.
try:
    os.mkdir(Path.cwd() / 'test/', mode=0o777)
except:
    FileExistsError
    print('The Test Folder Exists')

# print("The Tests are here: " + str(Path.cwd()) + '/test/')

for i in range(35):
    quizFile = open('test/quiz-{}'.format(i), 'w')
    answerFile = open('test/answer-{}'.format(i), 'w')

    # Write out the header for the quiz.
    quizFile.write('State Capitals Quiz\nName: ____________________\n\n')

    # TODO: Shuffle the order of the states.
    for i in range(15):
            state, capital = random.choice(list(capitals.items()))

            # Write Questions and Answers to Files
            quizFile.write('Question {} -'.format(i + 1).ljust(15) + f'What is the capital of {state}?\n________________________________\n\n')
            answerFile.write("Answer {}:".format(i+1).ljust(12) + f"{capital}\n")

    quizFile.close()
    answerFile.closer()

