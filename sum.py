def sum2(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

def sum3(numbers):
  total = 0
  i = 0
  print('Got here!')
  while i < len(numbers):
    print('i = ' + str(i) + ', total = ' + str(total))
    total += numbers[i]
    i += 1
  return total

print('Hello, world!')
print(sum2([1, 2, 3, 4]))
print(sum3([1, 2, 3, 4]))
