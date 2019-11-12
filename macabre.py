# load the mortality table by importing csv
import csv
# import pandas as import pdb; pdb.set_trace()
import os
# os.getcwd()

#opens mortality table
#declare function to store inputs
#use string to enter age and gender
#locate age and gender in mortality table in he csv file

open_table = open("mortality_table.csv")
read_the_file = csv.reader(open_table)
# for item in read_the_file:
#print item

sex = raw_input("Are you male or female?")
# inputs must be 'male', 'Male', 'female', 'Female'
# allow capatalized inputs
# raise TypeError
# if sex =! str
print sex

age = raw_input("How old are you?")
# raise TypeError if age =! int
print age
# life_expectancy = age, sex in the mortality_table
# create multiple choice factors
data = []
for row in reader
    row = [all_ages, male_life_expectancy, female_life_expectancy]
    all_ages = float(row[0])
    male life expectancy = float(row[1])
    female life expectancy = float(row[2])

    if sex = male_life_expectancy and age = all_ages
        data.append(row)
    elif sex = female_life_expectancy
        data.append(row)
    return data

drink = raw_input("How often do you drink? A) Zero - Once a week, B) Twice Several times a week C) Once daily D) Several times a day.... ")
    if drink = "A":
        data = data - 0
    elif drink = "B"
        data = data - 2
    elif drink = "C"
        data = data - 5
    elif drink = "D"
        data = data - 10
    else "You typed an invalid answer. Please try again."



#coding that needs to be completed:
#simplify the mortality_table (get rid of death probability)
