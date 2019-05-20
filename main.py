# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:45:52 2019

@author: mahsa

"""
import PalindromeSearch
#import PalList
def main():
    #string = "ABCBAHELLOHOWRACECARAREYOUILOVEUEVOLIIAMAIDOINGGOOD"
    string = input("Enter a string for finding all palindromes in it. \n")
    PalindromeSearch.PalindromeSearch.palSearch(string)
        
      

# Run the program
if __name__ == '__main__':
    main() 