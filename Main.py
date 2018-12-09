#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: Main.py
Name: Angel Villalpando
Date: 12/07/2018
Course: CS 2302 - Data Structures
Description: This program requests two words from the user and provides the minimum number of edits required
to 'transform' the first word into the second one using Dynamic Programming. 
"""

def edit_distance(str1, str2):
    matrix = []

    x = len(str1) + 1 # variables created to store length of words +1 (empty strings)
    y = len(str2) + 1

    for i in range(y): # creates the two dimensional array based on the dimensions of the provided words
        matrix.append([0] * x)

    for i in range(x): # initializes first ROW with 0, 1, 2, etc... based on string length
        matrix[0][i] = i

    for j in range(y): # initializes the first COL with 0, 1, 2, etc... based on string length
        matrix[j][0] = j

    for i in range(1, y): # nested for loop to make comparisons. Starts at 1 since we begin comparisons at index (1,1)
        for j in range(1, x):
            if str1[j-1].lower() == str2[i-1].lower(): # compares the characters of the provided word, not case sensitive
                matrix[i][j] = matrix[i-1][j-1] # if characters are the same, simply bring "diagonal" value down
            else:
                matrix[i][j] = min(
                    matrix[i - 1][j] + 1, # when characters are not the same, bring in value around current index and add 1
                    matrix[i - 1][j - 1] + 1,
                    matrix[i][j - 1] + 1
            )
    return matrix[-1][-1] # returns the last index of the 2D array, which holds the final number of edits


def userPrompt():
    word1 = input("\nPlease provide the first word: ")
    word2 = input("Please provide the second word: ")

    print("\nThe minimum number of edits required to turn the word", '"' + word1 + '"', "into", '"' + word2 + '"', "is",
          edit_distance(word1, word2), ".")

def main():

    userPrompt()

    userChoice = input("\nWould you like to compare other words? (Type yes or no): ")
    while userChoice == "yes":
        userPrompt()
        userChoice = input("\nWould you like to compare other words? (Type yes or no): ")
        if userChoice == "no":
            break

main()

