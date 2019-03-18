def sum_array(array):
    #Declare and initialize the sum as 0. If no array is passed the sum will remain zero
    array_sum=0
    #Use a for loop to loop over each item in the array to sum them up
    for i in array:
        array_sum += i
    #Return sum of all items in array
    return array_sum

def fibonacci(n):
    if n <= 0:
        return 0
    if n <= 1:
        return 1 # Return n if n is less or equal to one:
    else:
        #Return the nth term in a fibonacci sequence if n is greater than one
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n <= 1:
        return 1 # Return n if n is equal to one:
    else:
        #Return n! if n is not equal to one
        return n * factorial(n-1)

def reverse(word):
    '''
    By using [start:stop:step] and not indicating the start and stop values the
    function starts printing the list items from the end:
    '''
    reversed_word=word[::-1]

    #Return the reversed list
    return reversed_word
