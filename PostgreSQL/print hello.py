def new_func():
    def new_func1():
        def new_func():
            print("hello")

        new_func()

    new_func1()

# Program to add two numbers taken from user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print("The sum is:", result)