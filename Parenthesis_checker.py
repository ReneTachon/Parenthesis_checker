# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:07:04 2022

@author: rene.tachon
"""
#This script was developed following a Turing.com coding challenge. 
# The challenge is to detect incorrect praenthesis used in a string.  
# The brackets types should be opened and closed independently or opened and closed nested in another set of brackets.


test = "(g)[hh]{}"  #input to checking script. The string to test for correct parenthesis
openList =[]
for idx, i in enumerate(test): #Loop though chars in string

    # Have closing brackets been used before an opener?
    if ( i == "]"  and "[" not in openList ) or ( i == "}"  and "{" not in openList ) or ( i == ")"  and "(" not in openList ):
            print("fail - closer before opener")
            break
        
    # When brackets have been opened add them to a live list
    if i == "{" or i == "(" or i == "[":
        openList.append(i)
    else:
        #If any closers are found then they should be the last opened bracket. 
        #Remove this last opened braket from the live list. Repeat for each bracket type
        if i == "}" and openList[-1] == "{":
            del openList[-1]
        elif i == ")" and openList[-1] == "(":
            del openList[-1]
        elif i == "]" and openList[-1] == "[":
            del openList[-1]
        else:
            print("fail - closer before last opener was closed")
            break   
    
    #Check if a braket was left open and not closed when we get to the end of the list.
    if (idx == len(test) - 1) and openList != []:
        print("fail - bracket was never closed")
        break


    
        
