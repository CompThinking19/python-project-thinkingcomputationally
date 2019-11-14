# load the mortality table by importing csv
import csv
# import pandas as import pdb; pdb.set_trace()
import os

print """Welcome to Macabre, your own personalized death calculator.
Today we will be calculating your life expectancy and/or probable year of death.
DISCLAIMER: RESULTS PRESENTED IN MACABRE ARE NOT DEFINITIE.
MACARBE CANNOT FACTOR FATAL OCCURENCES OR TERMINAL ILLNESSES.
USE AT YOUR OWN RISK."""

#opens mortality table
open_table = open("mortality_table.csv")
read_the_file = csv.reader(open_table)

#use string to enter age and gender
sex = raw_input("Are you male or female?")
    if raw_input == "male" or "female":
        print sex.lower()
    else:
        print "Invalid input"

age = int(raw_input("How old are you?"))
print age

#set variables for the possible values in the mortality table
data = []
for row in reader
    male_life_expectancy = float(row[1])
    female_life_expectancy = float(row[2])
    topics = [male_life_expectancy, female_life_expectancy]
    data.append(topics)

male_or_female = 0
if sex == "female":
    male_or_female = 1
current_life_expectancy = data[age][male_or_female]

#Create a while loop if an invalid answer is input

correct_answer = False
while correct_answer == False:
    drink = raw_input("""How often do you drink?
    A) Zero - Once a Week
    B) Twice Several times a Week
    C) At Least Once Daily
    D) Several Times a Day"""

    if drink == "A":
        correct_answer = True
    elif drink == "B":
        current_life_expectancy -=2
        correct_answer = True
    elif drink == "C":
        current_life_expectancy -= 5
        correct_answer = True
    elif drink == "D":
        current_life_expectancy -= 10
        correct_answer = True
    else:
        print "You typed an invalid answer. Please try again."

smoke = raw_input("""How often do you smoke?
A) Zero - Two Times a Week
B) Several times a Week
C) At Least Once Daily
D) Several Times a Day""" )
    if smoke == "A":
        correct_answer = True
    elif smoke == "B":
        current_life_expectancy -=2
        correct_answer = True
    elif smoke == "C":
        current_life_expectancy -= 5
        correct_answer = True
    elif smoke == "D":
        current_life_expectancy -= 10
        correct_answer = True
    else:
        print "You typed an invalid answer. Please try again."

print "According to your answers, you have" current_life_expectancy "years to live."
#alternative ending
data = 2019 + current_life_expectancy
print "According to your answers, you are expected to die in " current_life_expectancy"."
