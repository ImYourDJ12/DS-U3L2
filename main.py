# Devon Taylor
# DS
# U3L2
# 10/28/24

def for_factorial(num):
  total = 0
  for i in range(num):
    total += num * i
  return total

def while_factorial(num):
  total = 0
  num2 = 1
  while num2 < num:
    total += num * num2
    num2 += 1
  return total

def recursion_factorial(num):
  if num == 0:
    return 1
  return num*recursion_factorial(num-1)

  

def main():
  num = 4
  forFact = for_factorial(num)
  whileFact = while_factorial(num)
  recurFact = recursion_factorial(num)

  print(f"Factorial: {num}\nFor: {forFact} \nWhile: {whileFact} \nRecursion: {recurFact}")

if __name__ == "__main__":
  main()