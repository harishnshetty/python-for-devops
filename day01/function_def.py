def sum_of_num():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    sum = num1 + num2
    print (sum)

env = input("Enter your environment: ")
if env == "dev":
    print("You are in development environment")
elif env == "test":
    print("You are in test environment")
elif env == "prod":
    print("You are in production environment")
else:
    print("Invalid environment")
if env == "dev":
        sum_of_num()