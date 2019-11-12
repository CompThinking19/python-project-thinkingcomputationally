# load the mortality table by importing csv
import csv
# import pandas as import pdb; pdb.set_trace()
import os
# os.getcwd()

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
##locate age and gender in mortality table in he csv file
    #if sex == male_life_expectancy and all_ages:
        #data.append(row)
    #elif sex == female_life_expectancy:
        #data.append(row)
    # return data
male_or_female = 0
if sex == "female":
    male_or_female = 1
current_life_expectancy = data[age][male_or_female]
drink = raw_input("""How often do you drink?
A) Zero - Once a Week
B) Twice Several times a Week
C) At Least Once Daily
D) Several Times a Day""" )
    if drink = "A":
        data = current_life_expectancy - 0
    elif drink = "B":
        data = current_life_expectancy - 2
    elif drink = "C":
        data = current_life_expectancy - 5
    elif drink = "D":
        data = current_life_expectancy - 10
    else "You typed an invalid answer. Please try again."

smoke = raw_input("""How often do you smoke?
A) Zero - Two Times a Week
B) Several times a Week
C) At Least Once Daily
D) Several Times a Day""" )
    if smoke = "A":
        data = current_life_expectancy - 0
    elif smoke = "B":
        data = current_life_expectancy - 2
    elif smoke = "C":
        data = current_life_expectancy - 5
    elif smoke = "D":
        data = current_life_expectancy - 10
    else "You typed an invalid answer. Please try again."

print "According to your answers, you have" current_life_expectancy "years to live."
#alternative ending
data = 2019 + current_life_expectancy
print "According to your answers, you are expected to die in " current_life_expectancy"."
