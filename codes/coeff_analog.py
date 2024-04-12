from sympy import symbols, simplify, I, poly

# Constants
B = 0.1066
Omega_0 = 0.5945

# Define symbolic variables
s, y = symbols('s y')

# Define the original transfer function
H_s_L = 0.3125 / (s**4 + 1.1068 * s**3 + 1.6125 * s**2 + 0.9140 * s + 0.3366)

# Define the domain transformation function g(x)
k = (y**2 + Omega_0**2) / (B * y)

# Substitute g_inverse(y) into the original function f(x)
H_s = H_s_L.subs(s, k)

# Substitute the value of y
y_value = 0.6502 * I
H_s_y = H_s.subs(y, y_value)

# Simplify the expression
H_s_y_simplified = simplify(H_s_y)

# Simplify the expression
H_s = simplify(H_s / abs(complex(H_s_y_simplified)))

# Convert the symbolic expression to polynomial form
numerator, denominator = H_s.as_numer_denom()

# Extract the coefficients
numerator_coeffs = poly(numerator, y).all_coeffs()
denominator_coeffs = poly(denominator, y).all_coeffs()

# Get the leading coefficient of the denominator
leading_denom_coeff = denominator_coeffs[0]

# Divide each coefficient by the leading coefficient of the denominator
numerator_coeffs = [coeff / leading_denom_coeff for coeff in numerator_coeffs]
denominator_coeffs = [coeff / leading_denom_coeff for coeff in denominator_coeffs]

print("Numerator coefficients:", numerator_coeffs)
print("Denominator coefficients:", denominator_coeffs)

# Store the coefficients in a file
with open('coefficients_analog.txt', 'w') as file:
    file.write("Numerator coefficients: " + str(numerator_coeffs) + "\n")
    file.write("Denominator coefficients: " + str(denominator_coeffs) + "\n")
