def add(A, B):
    return A + B

def subtract(A, B):
    return A - B

def multiply(A, B):
    return A * B

def divide(A, B):
    if B == 0:
        return "Cannot divide by zero"
    else:
        return A / B

def main():

    print("Simple Calculator")

    while True:
        try:
            A = float(input("Enter first number: "))
            B = float(input("Enter second number: "))
            op = input("Choose operation (+, -, *, /): ")

            if op == '+':
                result = add(A, B)
            elif op == '-':
                result = subtract(A, B)
            elif op == '*':
                result = multiply(A, B)
            elif op == '/':
                result = divide(A, B)
            else:
                print("Invalid Operation, Please ReEnter")
                continue

            print(f"Result: {result}")
            
            # Ask if user wants to perform another calculation
            repeat = input("Do you want to perform Next Calculation ? (Yes/No): ")
            if repeat.lower() != 'Yes':
                break
        
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
