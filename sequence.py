Implement a program to calculate the Fibonacci sequence up to a specified number of terms:
python
Copy code
def fibonacci_sequence(n):
    sequence = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)
    for i in range(2, n):
        next_num = sequence[i-1] + sequence[i-2]
        sequence.append(next_num)
    return sequence

num_terms = int(input("Enter the number of terms: "))
fibonacci = fibonacci_sequence(num_terms)

print("Fibonacci sequence up to", num_terms, "terms:")
for num in fibonacci:
    print(num)
