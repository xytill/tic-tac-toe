number = int(input())

print("This number is prime" if [number % x for x in range(1, number)].count(0) == 1
      else "This number is not prime")
