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
#     raise TypeError
#         if age =! int
print age
# life_expectancy = age, sex in the mortality_table
# create multiple choice factors
zero_once_a_week = 0
drink = raw_input("How often do you drink? Zero - Once a week, etc.... ")
# input drink

life_expectancy = life_expectancy + zero_once_a_week






#coding that needs to be completed:
#simplify the mortality_table (get rid of death probability)
