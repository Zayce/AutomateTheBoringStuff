def collatz():
    try:
        number = input("Please enter an integer: ")
        number = int(number)
        print(int(number))
        while number != 1: # Stops when number = 1
            if number % 2 == 0: # Evem
                number = number / 2
                print(int(number))
            elif number % 2 == 1: # ODD
                number = (3*number) + 1
                print(int(number))
            else:
                print("Error")
                break
    except:
        collatz()
collatz()

