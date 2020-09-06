"""
Write a function which can take any number of integers as input and will return the sum

E.g.

Function "ReturnType" Sum("InputType" inputs)
{
}

catch:
We live in a world where we only have string, char, 32 bit integer, array

Note:
Do not use any framework functions 
"""

def pad(a, b):
    isNegativeA, isNegativeB = False, False
    if a[0] == "-":
        isNegativeA = True
        a = a[1:]
    if b[0] == "-":
        isNegativeB = True
        b = b[1:]

    isSwap = False
    if len(a) < len(b):
        a, b = b, a #swap
        isNegativeA, isNegativeB = isNegativeB, isNegativeA
        isSwap = True

    pad = ""
    for i in range(len(a)-len(b)):
        pad += "0"
    b = pad + b

    if isNegativeA:
        a = "-" + a
    else:
        a = "+" + a
    if isNegativeB:
        b = "-" + b
    else:
        b = "+" + b
    if isSwap:
        return (b, a)
    return (a, b)

def add(a, b, isNegative):
  increment = 0
  result = ""
  for i in range(len(a)-1, 0, -1):
      temp = int(a[i]) + int(b[i]) + increment
      increment = 0
      if temp > 9:
          increment = 1
          temp = temp % 10
      result += str(temp)
  if increment > 0:
      result += str(increment)

  result = result[::-1]
  if isNegative:
      result = "-"+result

  return result

def sub(a1, b1):
    res = ""
    borrow = 0

    a, b = a1[1:], b1[1:]

    isSwap, isNegative = False, True
    if a < b:
        isSwap = True
        a, b = b, a
        isNegative = False

    for i in range(len(a)-1, -1, -1):
        c, d = int(a[i]), int(b[i])
        borrowLater = False
        if c < d:
            c = c+10
            borrowLater = True
        res += str(c-d-borrow)
        if borrowLater == True:
            borrow = 1
        else:
            borrow = 0

    if isNegative:
        res = "-" + res[::-1]
    else:
        res = res[::-1]
    return res

def operate(a, b):
  a, b = pad(a, b)

  if a[0] != b[0]: #different symbol
    return sub(a, b)
  return add(a, b, a[0] == "-")

def sum(arr):
  total = 0
  for a in arr:
    total = operate(total, a)

  return total

print(operate(str(-1), str(-1))) #2
print(operate(str(-1), str(-14))) #-15
print(operate(str(-53), str(27))) #-26
print(operate(str(-43), str(1))) #-42
print(operate(str(-1), str(43)))
print(operate(str(1), str(999))) #1000
print(operate(str(1), str(2)))
print(operate(str(12), str(12)))
print(operate(str(12), str(19))) #31
print(operate(str(123), str(999)))
