#!/usr/bin/python

## import a library
import time

## define a function
def main():

    #add some blank space on output
    print ""

    #be polite and introduce yourself
    print "Hello, my name is Max."

    ##wait a sec
    time.sleep(1)

    ## get user's name
    name = raw_input("What is your name? ")

    time.sleep(1)

    feeling = raw_input("How are you feeling today, %s? " % name )

    ## print a statement, conditional on the user's response.

    if (feeling == "good"):
        print "That's great!"

    elif (feeling == "bad"):
        print "Maybe you should get some coffee."

    else:
        print "I'm sorry, I don't understand. I'm not very intelligent."

    print ""

## call the main function
main()
