#Challenge: FizzBuzz on Github
#Caelen Walker 10/12/22

for fz in range(1, 101):
    if fz % 3 == 0:
        print("fizz: " + str(fz))
    elif fz % 5 == 0:
        print("buzz: " + str(fz))
    elif fz % 3 == 0 and fz % 5 == 0:
        print("fizzbuzz: " + str(fz))
    else:
        print(fz)
