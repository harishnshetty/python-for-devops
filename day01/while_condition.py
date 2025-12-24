# while condition
choice = input("Do you want to continue? (y/n)")

while choice == "y":
    num = int(input("Enter a table number:"))
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)
    choice = input("Do you want to continue? (y/n)")
else:
    print("Thank you")