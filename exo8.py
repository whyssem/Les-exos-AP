nombre = int(input("Entrez un nombre: "))

if nombre % 3 == 0 and nombre % 5 == 0:
    print("FizzBuzz")
elif nombre % 3 == 0:
    print("Fizz")
elif nombre % 5 == 0:
    print("Buzz")

