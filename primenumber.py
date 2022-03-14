n = int(input('Enter a number: '))

# flag that will check whether a given number is prime or not
isPrime = False

# if number is zero, it is neither prime nor composite
# 2 is the only even prime number

if n==0:
    print('0 is neither prime nor composite')
elif n==2:
    print('2 is the only even prime number')
else:
    # finding square root of any number to check whether it is prime or not is good practice because
    # if we prime factorise and number in form a*b, then we will find that if a increases, then b decrease
    # so at any given point of time, a and b can attain the max value only if a and b are equal

    # a**b is always float and range doesn't work on floats, so we have to convert that value in int
    # +1 is needed with int(a**b) because otherwise the square root may be excluded
    # Ex: 49 square root is 7 and if we are not using +1, 7 will be excluded and we will get that 49 is prime, but it is not
    
    # incrementing value by 2 because if a number is not divisible by 2, it will not be divisible by any other even number
    for i in range (3,int(n**0.5)+1,2):
        if n%i == 0:
            isPrime = True
            break

if isPrime:
     print(f'{n} is not prime')
else:
    print(f'{n} is prime')
