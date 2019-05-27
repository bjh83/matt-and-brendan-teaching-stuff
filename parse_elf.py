f = file('elfdump.txt')

for line in f:
  if 'SECTION' in line:
    print(line)

print('Hello\nworld!')
