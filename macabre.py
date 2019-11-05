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
for item in read_the_file:
    print item

sex = raw_input("Are you male or female?")
print sex

age = raw_input("How old are you?")
print age



#if raw_input =
    #return item
#     fieldnames = []
#     age == 0
# def factors (age, gender)
#     for row in csv.reader
#         if age == 0 and gender = 0
#         return fieldname

#coding that needs to be completed:
#simplify the mortality_table (get rid of death probability)
