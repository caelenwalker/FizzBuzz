#Challenge: FizzBuzz on Github
#Caelen Walker 10/12/22

for fizzbuzz in range(1, 101):
    if (fizzbuzz % 3 == 0):
        print("fizz: " + str(fizzbuzz))
    elif (fizzbuzz % 5 == 0):
        print("buzz: " + str(fizzbuzz))
    elif (fizzbuzz % 15 == 0):
        print("fizzbuzz: " + str(fizzbuzz))
    else:
        print(fizzbuzz)
