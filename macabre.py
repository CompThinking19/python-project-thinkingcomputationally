# load the mortality table by importing csv
import csv
import os

print
"""
Welcome to Macabre, your own personalized death calculator.
Today we will be calculating your life expectancy.
DISCLAIMER: RESULTS PRESENTED IN MACABRE ARE NOT DEFINITIE.
MACARBE CANNOT FACTOR FATAL OCCURENCES OR TERMINAL ILLNESSES.
USE AT YOUR OWN RISK.
"""

#opens mortality table in csv
open_table = open("mortality_table.csv")
read_the_file = csv.reader(open_table)

#use string to enter age and gender
sex = raw_input("Are you male or female?")
if raw_input == "male" or "female":
    print sex.lower
else:
    print "Invalid input"

age = int(raw_input("How old are you?"))
print age

#set variables for the possible values in the mortality table for male and female life expectancies
#data holds this information
data = []
for row in reader:
    male_life_expectancy = float(row[1])
    female_life_expectancy = float(row[2])
    topics = [male_life_expectancy, female_life_expectancy]
    data.append(topics)

#male is assigned to variables in column 0, female is assigned to variables in column 1
male_or_female = 0
if sex == "female":
    male_or_female = 1
current_life_expectancy = data[age][male_or_female]

#Create a while loop if an invalid answer is input for health questions
#selected answer subtracts years from life expectancy
correct_answer = False
while correct_answer == False:
    drink = raw_input(
    """
    How many standard alcoholic drinks do you have per week?
    A) 0 - 7
    B) 8 - 14
    C) 14 - 25
    D) 25 +
    """
    )

    if drink == "A":
        correct_answer = True
    elif drink == "B":
        current_life_expectancy -=0.5
        correct_answer = True
    elif drink == "C":
        current_life_expectancy -=2
        correct_answer = True
    elif drink == "D":
        current_life_expectancy -=5
        correct_answer = True
    else:
        print "You typed an invalid answer. Please try again."

smoke = raw_input(
"""
How many cigarettes do you smoke per day?
A) 0
B) less than 5
C) 5 - 20
D) 20 +
"""
)
if smoke == "A":
        correct_answer = True
elif smoke == "B":
        current_life_expectancy -=5
        correct_answer = True
elif smoke == "C":
        current_life_expectancy -=9
        correct_answer = True
elif smoke == "D":
        current_life_expectancy -=13
        correct_answer = True
else:
    print "You typed an invalid answer. Please try again."

#input final life expectancy (int) into the string
stuff_in_string = "According to your answers, you have %d to live." % (current_life_expectancy)
print stuff_in_string
