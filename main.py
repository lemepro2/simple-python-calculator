
while True:
    a = input("Enter first number (or 'exit'): ").strip()
    if a.lower() == "exit":
        break

    try:
        num1 = int(a)  
    except ValueError:
        print("Please enter a valid number")
        continue

    b = input("Enter second number: ").strip()
    try:
        num2 = int(b)  
    except ValueError:
        print("Please enter a valid number")
        continue

    print("Choose an operation\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")

    operation = input("Enter operation : ")

    match operation :
        case "+":  
            print(f"Result is {num1+num2}")
        case "-": 
            print(f"Result is {num1-num2}")
        case "*": 
            print(f"Result is {num1*num2}")
        case "/": 
            if b != 0:
                print(f"Result is {num1/num2}")
            else :
                print("Error : Division by Zero")    
        case _:
            print("Invalid input detected")