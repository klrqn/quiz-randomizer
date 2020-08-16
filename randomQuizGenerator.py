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
for quizNum in range(35):
    quizFile = open(f'Capitals Quiz {quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'Capitals Quiz Answers {quizNum + 1}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\n:Period:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write Questions and Answers to Files
        answerKeyFile.write(f"{questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
