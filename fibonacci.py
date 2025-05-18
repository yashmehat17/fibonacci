# Program to display the Fibonacci sequence up to n terms

# Get number of terms from user
n_terms = int(input("How many terms? "))

# First two terms of the sequence
n1, n2 = 0, 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer.")
elif n_terms == 1:
    print("Fibonacci sequence up to 1 term:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(n1)
        nth = n1 + n2  # next term is the sum of the previous two
        n1 = n2
        n2 = nth
        count += 1
