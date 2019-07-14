# Author: Anthony Cunningham Section A01

# CS1 Homework 5, Questions 2 & 3

# Question 2

def extractColumn(matrix, i):
    return [item[i] for item in matrix]

# Question 3

def countNumsWithDigit(upperNumber, digit): 
    return [item for item in (list(range(upperNumber)) + [upperNumber]) if digit == item]
    
        
    
        
    
    




