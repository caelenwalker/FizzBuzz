#Challenge: FizzBuzz on Github
#Caelen Walker 10/12/22

for fz in range(101):
    if fz % 3 == 0:
        print("fizz")
        continue
    elif fz % 5 == 0:
        print("buzz")
        continue
    elif fz % 3 == 0 and fz % 5 == 0:
        print("fizzbuzz")
        continue
    print(fz)
    
