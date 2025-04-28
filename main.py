# main.py

import add
import subtract
import multiply
import divide

def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice: "))
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if choice == 1:
        print("Result:", add.add(a, b))
    elif choice == 2:
        print("Result:", subtract.subtract(a, b))
    elif choice == 3:
        print("Result:", multiply.multiply(a, b))
    elif choice == 4:
        print("Result:", divide.divide(a, b))
    else:
        print("Invalid Choice!")

if __name__ == "__main__":
    main()
