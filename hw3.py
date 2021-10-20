#!/usr/bin/python
# problems = search is still case sensitive, searches are only for one place in sequence 

sequence= input("Please enter a sequence:  ")
valid_nucleotides = "ACGTactgNn"
sequence = sequence.replace(" ", "")

for i in sequence:
    if i in valid_nucleotides:
            count = 1
    else:
            count=0
if count==1:
    print("This is a valid DNA sequence.") 
    pass
    
else:
    print("This is an invalid DNA sequence")
    quit ('exit')

sequencesearch= input ("please enter the search terms: ")

if sequencesearch in sequence:
        print( sequencesearch, "is found in position")
        print (sequence.find(sequencesearch))    
        pass
else: 
        print ("not found")
        quit ('exit')
