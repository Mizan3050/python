
# CODE FOR BISECTION SEARCH!!
# set lower limit as 0, upper limit as max (200 in this case since the range)
# iterate from lower limit to upper limit and take the 1st guess as (lower limit + upper limit)/2
# if the guess == search number, break the loop, and print the guess number
# if the guess is smaller than the search number then set lower limit as (lower limit + upper limit)/2
# if the guess is greater than search number then set upper limit as (lower limit + upper limit)/2

searchNumber  = 123
upperLimit = 250
lowerLimit = 0
guess = (lowerLimit+upperLimit)/2
i = 0
while(guess!=searchNumber):
    i = i+1
    if(guess<searchNumber):
        lowerLimit = guess
        guess = (lowerLimit+upperLimit)/2
    else:
        upperLimit = guess
        guess = (lowerLimit+upperLimit)/2
print('Your search term is', int(guess), 'and the number to iterations it took was', i)
