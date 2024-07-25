size = int(input("Enter the size of the pattern: "))


while size <= 0:
    print("Error: size must be a positive integer.")
    size = int(input("Enter the size of the pattern: "))

for row in range(size):
    for col in range(size):
        print("*", end="")
    print()  
