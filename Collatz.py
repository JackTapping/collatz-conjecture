# Creating the collatz method 
def collatz(number):

    #index to keep trak of how many times the number has been chnaged
    index = 0

    # loop to run the method untill the numbe is equal to 1
    while number != 1:

        # if the number is even then divide by 2
        if number % 2 == 0:
           number = number // 2
           index  += 1
           print(str(number) + "   :   " + str(index))

        # if the number is odd then times by 3 plus 1
        else:
           number = number * 3 + 1
           index += 1
           print(str(number) + "   :   " + str(index))


# asking the user for a number 
number = int(input("Enter in a number:" ))

#calling the method for to run the collatz conjecture 
collatz(number)
