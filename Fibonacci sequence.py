def generate_fibonacci_sequence(n):
    # Initialize the first two terms of the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
        fibonacci_sequence.append(next_term)
    
    # Handle special cases for n = 1 and n = 2
    if n == 1:
        fibonacci_sequence = [0]
    elif n == 2:
        fibonacci_sequence = [0, 1]
    
    # Display the Fibonacci sequence
    print("Fibonacci sequence up to", n, "terms:")
    print(fibonacci_sequence)

# Example usage
try:
    num_terms = int(input("Enter the number of terms: "))
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        generate_fibonacci_sequence(num_terms)
except ValueError:
    print("Invalid input. Please enter a valid integer.")