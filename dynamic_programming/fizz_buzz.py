# Defining Starting Number Output String And Number Of Iterations to Play For
number = 1
out = ""
iterations = input("How Many Numbers To Play?: ")

# FizzBuzz Logic
while number <= int(iterations):
  if number % 3 == 0: out += "Fizz"
  if number % 5 == 0: out +="Buzz"
  if out == "": out = number
  print(out)
  number += 1
