numero_1= float(input("Enter the first number: "))
numero_2= float(input("Enter the second number: "))
operation=input("Type your operation (+,-,*,/): ")

if operation  == "+":
    result= numero_1 + numero_2
    print(f"The result of {numero_1} + {numero_2} is: {result}")

elif operation=="-":
    result=numero_1 - numero_2
    print(f"The result of your operation is: {result}")

elif operation=="*":
   result=numero_1 * numero_2
   print(f"The result of your operation is: {result}")


elif operation=="/":
    if numero_2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result=numero_1 / numero_2
        print(f"The result of your operation is: {result}")

else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.")

    print("Thanks for using the calculator! Goodbye!")

    exit()































































































































































