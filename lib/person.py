#!/usr/bin/env python3

class Person:
    # Class body goes here
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

    #Instance method definition
    pass

# Testing the Person class
if __name__ == "__main__":
    john = Person()
    john.talk()  
    john.walk()  
