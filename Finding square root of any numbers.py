# Finding square root of any number
while True:
    try:
        num = float(input("Enter the number: "))
        num_sqrt = num ** 0.5
        print(f"The Square root of {num} is {num_sqrt}")
        
        another_calculation = input("Do you want to perform one more? (yes/no): ").lower()
        if another_calculation != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
    except KeyboardInterrupt:
        print("\nProgram was terminated by user.")
        break
        