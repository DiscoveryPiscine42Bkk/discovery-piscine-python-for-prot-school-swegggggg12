number = int(input("Enter a number to generate ist muitiplication table:"))
print(f"Mltiplication table for {number}:")
for i in range(1, 11):
    print(f"{number}* {i} = {number * i}")