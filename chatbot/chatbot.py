#!/usr/bin/python

## import a library
import time

## define a function
def main():

    #add some blank space on output
    printEmptyLine()

    #be polite and introduce yourself
    print ("Hello, my name is Max.")

    x=1
    ##wait a sec
    time.sleep(x)

    ## get user's name
    name = input("What is your name? ")

    time.sleep(1)

    feeling = input("How are you feeling today, %s? " % name )

    ## print a statement, conditional on the user's response.

    if (feeling == "good"):
        print ("That's great!")

    elif ( feeling == "bad"):
        print ("Maybe you should get some coffee.")

    else:
        print ("I'm sorry, I don't understand. I'm not very intelligent.")

    printEmptyLine()

def printEmptyLine():
    print ("")


## call the main function
main()
