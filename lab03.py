########################################################################
##
## CS 101 Lab
## Lab 03
## Franklin Jeffries
## fmjc89@umsystem.edu
## professor's name
## October 21, 2022
##
## This program is designed to be able to correctly guess a number based off of the questions you answer.
##
########################################################################

# The game should be able to loop back and be played over and over until the user opts out
print('Welcome to the Flarsheim Guesser!\n')
print('Please think of a number between and including 1 and 100.')
#
def getRemainder(num, divisor):
    return (num - divisor * (num // divisor))
while True:
    num = int(input())
    divisor = 3
    remainder = print(getRemainder(num, divisor))
    print('What is the remainder when your number is divided by 3 ?', remainder)
    if remainder < 0:
        print('The value entered must be 0 or greater')
    elif remainder >= 3:
        print('The value entered must be less than 3')
    else:
        exit
def getRemainder(num, divisor):
    return (num - divisor * (num // divisor))
while True:
    num1 = int(input())
    divisor = 5
    remainder = print(getRemainder(num, divisor))
    print('What is the remainder when your number is divided by 5 ?', remainder)
    if remainder < 0:
        print('The value entered must be 0 or greater')
    else:
        exit
def getRemainder(num, divisor):
    return (num - divisor * (num // divisor))
while True:
    num2 = int(input())
    divisor = 7
    remainder = print(getRemainder(num, divisor))
    print('What is the remainder when your number is divided by 7 ?', remainder)
    if remainder < 0:
        print('The value entered must be 0 or greater')
    else:
        exit
def main():
    while True:
        play_again = input('Do you want to play again? Y to continue, N to quit ==>')
        if play_again == Y:
            return getRemainder()
        if play_again == N:
            break
        else:
            print('Please input Y or N')
