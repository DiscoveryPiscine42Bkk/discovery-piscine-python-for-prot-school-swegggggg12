number = 1
while number <= 10:
    print(f"Table de {number}:", end="")
    i = 1 
    while i <= 10:
        print(number * i, end= " ")
        i += 1 
    print()
    number += 1