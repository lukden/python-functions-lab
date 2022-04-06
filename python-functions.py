# 1

def sum_to(num):
  sum = 0
  for n in range(1, num + 1):
    sum += n
  return sum

# 2

def largest(list):
  largest = 0
  for num in list:
    if num > largest:
      largest = num
  return largest

  # 3

def occurrences(string, substr):
  new_string = string.replace(substr, '')
  return (len(string) - len(new_string)) // len(substr)

# print(occurrences('ciaooo', 'o'))

# 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(1, 2, 5, 7))







