# Finger exercise Lecture 1

a = 1
b = 2
c = 3

total = a + b + c
print(total)

# Finger exercise Lecture 2

number = 17

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

# Finger exercise Lecture 3
N = 2
for i in range(N):
    print("Hello World!")


# Finger exercise Lecture 4

N = 27

estimated_root = 0
while (estimated_root ** 3 < N):
    estimated_root += 1

if estimated_root ** 3 == N:
    print(N)
else:
    print("error")


# Finger exercise Lecture 5

my_str = "0123456789"

print(my_str[::2])



# Finger exercise Lecture 6

N = 379

l = 0
r = 1000
steps = 0

while l < r:
    mid = (l + r) // 2
    steps += 1
    if mid < N:
        l = mid + 1
    elif mid > N:
        r = mid - 1
    else:
        print(f"Found N = {N} in {steps} steps")
        break

# Finger exercises Lecture 7

def eval_quadratic(a, b, c, x):
    """
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    Returns the value of the quadratic a×x² + b×x + c.
    """
    # Your code here
    return a*(x**2) + b*x + c

# Examples:    
print(eval_quadratic(1, 1, 1, 1)) # prints 3


def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    """
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    Prints the sum of the two evaluations. Does not return anything.
    """
    # Your code here
    return eval_quadratic(a1, b1, c1, x1) + eval_quadratic(a2, b2, c2, x2)

# Examples:    
two_quadratics(1, 1, 1, 1, 1, 1, 1, 1) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None
