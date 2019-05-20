# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:45:52 2019

@author: mahsa

"""

class PalindromeSearch:
    
    def __init__(self, palindrome, index, length):
        self.palindrome=palindrome
        self.index=index
        self.length=length
    
    
    def palSearch(string): 
        length = len(string)  
        palList = list()
        
        # For every character in the string check the character before and after
        # Different cases for odd and even lengths palindromes
        for i in range(1, length):
            startOdd, maxLengthOdd = PalindromeSearch.oddSearch(string, i)             
            if maxLengthOdd > 1:
                palListItem=PalindromeSearch((string[startOdd:startOdd + maxLengthOdd]), startOdd, maxLengthOdd)
                palList.append(palListItem)   
                           
            startEven, maxLengthEven = PalindromeSearch.evenSearch(string, i)             
            if maxLengthEven > 1:
                palListItem=PalindromeSearch((string[startEven:startEven + maxLengthEven]), startEven, maxLengthEven)
                palList.append(palListItem)            
        
        palList.sort(key=lambda x: x.length, reverse=True)        
        PalindromeSearch.printResults(palList)
    
    
    
    def evenSearch(string, i):
        # Finding even length palindrome 
        # The center point between i-1 and i
        low = i - 1
        high = i 
        maxLength = 1
        length = len(string) 
        start = low
        while low >= 0 and high < length and string[low] == string[high]: 
            #if high - low + 1 > maxLength: 
            start = low 
            maxLength = high - low + 1
            low -= 1
            high += 1
            
        return start, maxLength
        
        
    def oddSearch(string, i):
        # Finding longest odd length palindrome
        # The center point is at i 
        low = i - 1
        high = i + 1
        maxLength = 1
        length = len(string) 
        start = low
        while low >= 0 and high < length and string[low] == string[high]: 
            #if high - low + 1 > maxLength: 
            start = low 
            maxLength = high - low + 1
            low -= 1
            high += 1
    
        return start, maxLength
    
    
    
    
    def printResults(palList):
        if len(palList)==0:
            print("The string doesn't have a palindrome.")
        for item in palList:
            print(item.palindrome, item.index, item.length, end='\n')
    
    
    
    
    
    

       


