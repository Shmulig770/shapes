from Rectangle import rectangle
from Circle import circle
from Square import square
from Triangle import triangle


def main():
    shape = int(input("choose your shape: \n\
                  1. rectangle.\n\
                  2. circle\n\
                  3. square\n\
                  4. triangle"))
    while True:
        if shape == 1:
            print(rectangle())
            break
        elif shape == 2:
            print(circle())
            break
        elif shape == 3:
            print(square())
            break
        elif shape == 4:
            print(triangle())
            break
        else:
            print("worn type try again")
