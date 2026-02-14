
# Ethan E. Lopez
# 002425516
# etlopez@chapman.edu
# CPSC 230 - Section 2
# Program Assignment 3

def complement(dna): # defines function complement(dna)
    c = '' # creates a new string at value c
    dna = dna.upper() # capitalizes all letters in dna
    for letter in dna: # creates for loop for every letter
        if letter == 'A': # adds T in c if letter is A
            c += 'T'
        elif letter == 'G': # adds C in c if letter is G
            c += 'C'
        elif letter == 'T': # adds A in c if letter is T
            c += 'A'
        elif letter == 'C': # adds G in c if letter is G
            c += 'G'
    return c # returns final dna sequence complement

def rev_complement(dna): # defines function rev_complement(dna)
    dna = dna[::-1] # reverses original input
    dna = complement(dna) # uses complement function to translate 
    return dna # returns final reverse dna sequence complement

dna = input('Please enter dna sequence: ') # grabs input from user for dna sequencing

print(complement(dna)) # prints result of complement function
print(rev_complement(dna)) # prints result of rev_complement function
    
