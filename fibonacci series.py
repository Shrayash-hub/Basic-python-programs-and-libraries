#fibonacci series
def fibonacci(n):
    sequence = [0,1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
terms = 10
print(f"The first {terms} terms of the fibonacci sequence are: {fibonacci(terms)}")
