#!/usr/bin/env python3 
'''This program exists to read in book text from https://cs.indstate.edu/~cs40126/authors/xyz.txt, perform some string formatting, and output to xyz.csv in https://cs.indstate.edu/~cs40126/authors/xyz.txt 

from https://cs.indstate.edu/~lmay1/courses/#/courses/cs401/knn: 

USAGE: ./author_parse.py "https://cs.indstate.edu/~cs40126/authors/a2.txt" > ~/public_html/authors/a2.csv

USAGE: ./author_parse.py "https://cs.indstate.edu/~cs40126/authors/b5.txt" > ~/public_html/authors/b5.csv
'''
import urllib.request
import re
import sys

#Handle Command Line Arguments and Read in File
#reference sources: https://www.geeksforgeeks.org/command-line-arguments-in-python/
#get cmd line arg for path to book text file
'''code origin from Professor May in CS401 Lab 2 Section 2 HTTP Requests - 
cs.indstate.edu/~lmay1/courses/#/courses/cs401/lab2'''

#check for more than 1 argument
if(len(sys.argv) > 1):
    #get arg
    argument = sys.argv[1]
    #pass in arg
    with urllib.request.urlopen(argument) as req:
        req_data = req.read().decode('utf-8')
else:
    with urllib.request.urlopen("https://cs.indstate.edu/~cs40126/authors/a1.txt") as req:
        req_data = req.read().decode('utf-8')

#Remove Punctuation using Regex
#referencing lab2 regular expressions in get_users.py for re.compile
regex_punc = re.compile(r'[!()\[\]{};:\'"\“\”\‘\’\,<>./?@#$%^&*_~]')

'''optionally add hyphenated character: —
I am opting to leave this character off of the punctuatiuon string as H.G. Wells seems to make use of this in his specific style of writing. It seems to be someone of a unique identifier.'''
#https://docs.python.org/3/library/re.html for re.sub documenation to look up params
req_data = re.sub(regex_punc, '', req_data)
#remove uppercase
req_data = req_data.lower()
#initialize list/dict to store words
word_list = []
word_count = {}
#comprehension to append to list while splitting book string on whitespace
[word_list.append(i) for i in req_data.split()]

#Get Counts of Unique Words
sum_count = 0 
##iterate through word list
for word in word_list:
    #check if word not encountered
    if word not in word_count:
        #add key and value of 1
        word_count[word] = 1
        sum_count += 1
    #otherwise increment value at key
    else:
        word_count[word] += 1
        sum_count += 1

#Sort Dictionary
##lambda function for sorted key param from 6. https://www.geeksforgeeks.org/python-sorted-function/
#sort by key values, returns a list of tuples
word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
#cast back to dictionary
word_count = dict(word_count)

##Output
print('Word,Count')
#iterate through word_count keys
for word in word_count.keys():
    #get frequency
    word_count[word] = word_count[word] / sum_count
    print(f'{word},{word_count[word]}')

print(sum_count)
