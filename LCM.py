a = 12
b = 15

# Calculate GCD
x, y = a, b
while y:
    x, y = y, x % y
gcd = x

# Calculate LCM
lcm = abs(a * b) // gcd
print(f"LCM of {a} and {b}:", lcm)
