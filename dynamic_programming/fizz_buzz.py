number = 1
out = ""
iterations = 100

while number <= int(iterations):
  if number % 3 == 0: out += "Fizz"
  if number % 5 == 0: out +="Buzz"
  if out == "": out = number
  print(out)
  number += 1
