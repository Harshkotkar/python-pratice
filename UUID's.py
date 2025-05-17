hfghfhimport random

# Original string
str_ = "hello"

# Generate a random number of digits (between 2 and 5)
num_digits = random.randint(2, 5)

# Generate random numbers of the chosen length
random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(num_digits)])

# Concatenate the string with the random numbers
result = str_ + random_numbers

print(result)
