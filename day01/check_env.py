env = input("Enter your environment: ")

if env == "dev":
    print("You are in development environment")
elif env == "test":
    print("You are in test environment")
elif env == "prod":
    print("You are in production environment")
else:
    print("Invalid environment")