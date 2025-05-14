def prime_checker(number):
  for numbers in range(2, number):
    if number % numbers == 0:
      print("It's not a prime number.")
      break
  else:
    print("It's a prime number.")
    
n = int(input())
prime_checker(number=n)