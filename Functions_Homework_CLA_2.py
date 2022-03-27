#Write a Python function that takes a number as a parameter and checks if the number is prime or not. 
# A prime number (or a prime) is a 
# natural number greater than 1 and that has no positive divisors other than 1 and itself.
number=int(input('enter number ')) 
dev_numbers=[2,3,4,5,6,7,8,9] #number that will be used to check if the input number is is indeed prime
def prine_number_check(number):
    if number not in dev_numbers: 
        for i in dev_numbers:
            if number %i==0:
                print('this is not a prime number')
                break
        else:
            print('this is indeed a prime number')
    else:
        dev_numbers.pop(dev_numbers.index(number))
        print(dev_numbers)
        for i in dev_numbers:
            if number %i==0:
                print('this is not a prime number')
                break
        else:
            print('this is indeed a prime number')
prine_number_check(number)


