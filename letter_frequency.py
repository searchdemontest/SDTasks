# Write a program that takes a string input from the user, calculates how many times each letter in the string occurs and then prints this out to the screen.
# case should be ignored
# the code to get the string input has already been provided
# the final output should be sorted alphabetically
# ignore characters not in the alphabet

#A sample output is of the following:

# $ python letter_counts.py "ThiS is String with Upper and lower case Letters."
# a  2
# c  1
# d  1
# e  5
# g  1
# h  2
# i  4
# l  2
# n  2
# o  1
# p  2
# r  4
# s  5
# t  5
# u  1
# w  2
# $

def count_letter_frequency(string):
    frequency = {} #dictionary to hold mapping between each letter and frequency

    
    #enter your code here#
    for x in string:
        if frequency.has_key(x):
            frequency[x] = frequency[x] + 1
        else:
            frequency[x] = 1


    return frequency

string = raw_input('Enter sentence: ')
frequencyDict = count_letter_frequency(string)

#carry out the printing here, and dont forget to print in alphabetical order as seen above
