#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print (i)
    i -= 1
    print ("Happy New Year!")

def square_integers(int_list):
    squares = [intgr **2 for intgr in int_list]
    print(squares)
    return squares

# square_integers([1,2,3,4,5])
# square_integers([-1,-2,-3,-4,-5])

def fizzbuzz():
    num = 1
    while num <= 100:
        if num % 3 == 0 and num % 5 == 0:
            print ("FizzBuzz")
        elif num % 3 == 0:
            print ("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print (num)
        num +=1
    
fizzbuzz()

