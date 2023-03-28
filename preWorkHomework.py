# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of a function.
def hello_name(user_name):
    print("hello_",user_name,sep="")

# Question 2
# Write a function that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    numList = list(range(1,101))
    for thisNum in numList:
        if(thisNum%2!=0):
            print(thisNum)

# Question 3
# Write a function to return the max number of a given list
#...am I not supposed to use a built in function? You can't want me to write an algorithm 
# to compare max ele to every other, right? I mean, I could...but max() is already optimized...
# or sort and return the first/last element depending on sort order?
def max_num_in_list(a_list):
    return(max(a_list))

# Question 4
# Write function to return if the given year is a leap year. Leap years are divisible by 4 but not by 100, unless also 
# divisible by 400. return should be true/false. 
def is_leap_year(a_year):
    print("testing year",a_year, sep=" ")
    # anything no remainder dividing by both 100 and 400 is a leap year
    if((a_year%100==0) & (a_year%400==0)):
        return(True)
    # given above, anything subsequently divisible by 4 no remainder but not by 100 is a leap year 
    elif((a_year%4==0) & (a_year%100!=0)):
        return(True)
    # given above, everything else is not a leap year
    else:
        return(False)
        
#Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. Return boolean
def is_consecutive(a_list):
    # Originally I thought I could do this by comparing the first and last elements, but this assumes some
    # qualities of the list that the question doesn't state, so I think I can't actually do that. I was trying
    # to avoid having to compare every element, but unless the question guarantees certain formatting for the 
    # list I don't think this works. I also thought, briefly, I could sort the input, but I think that's not
    # in the spirit of the question, either, so I'm going to assume they mean consecutive "as passed" to the
    # function, as opposed to the list just containing consecutive numbers but in any order.
    # The optimal is probably some recursive solution that maintains a counter and calls itself, but that's 
    # also probably beyond the scope of what's being asked.

    # I'm also going to assume that they mean the list is consecutive in the same direction consistently,
    # that is, [1,2,3,4,3,2,1] doesn't count, though these numbers are technically consecutive.

    # so, element-wise comparison it is.

    # we could receive either an ascending or a descending list. Let's just flip the list around if it's descending
    # to make life easier. 
    # Note that this reverse isn't a problem if the list doesn't end up being consecutive.
    #It would also be nice if we were passed a list with more than 1 element.
    tempList = a_list
    if(len(tempList)<2):
        print("Please submit a list of at least 2 integers")
        return(False)
    
    if(tempList[0] > tempList[1]):
        tempList.reverse()
    # now we should have an ascending list in either case...or just random numbers.
    for thisItem in range(0,len(tempList)-1):
        print(tempList[thisItem])
        if((tempList[thisItem+1]-tempList[thisItem])!=1):
            return(False)
    # if we make it to here, the list should be consecutive
    return(True)
    
# testing
#print("Testing Q1")
#hello_name("Jeff")
#print("Testing Q2")
#first_odds()
#print("Testing Q3")
#print(max_num_in_list([1,2,3,4]))
#print("Testing Q4")
#print(is_leap_year(1700))
#print(is_leap_year(2024))
#print(is_leap_year(2000))
#print(is_leap_year(27))
#print("Testing Q5")
#print(is_consecutive([1,2,3,4,5]))
#print(is_consecutive([-1,0,1,2,3,4,5]))
#print(is_consecutive([7,6,5,4,3,2,1]))
#print(is_consecutive([1,2,3,5]))