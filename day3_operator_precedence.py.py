# Day 3 – Operator Precedence & Associativity
# Demonstrates precedence and associativity rules in Python

print("---- Operator Precedence & Associativity ----\n")

# 1. * and / are evaluated before + and -

print(2+3*5) # Output: 17, because 3*5 is evaluated first
print((2-3)*5) # Output: 25, because (2+3) is evaluated first   
print(10-4/2) # Output: 8.0, because 4/2 is evaluated first
print((10-4)/3) # Output: 2.0, because (10-4) is evaluated first, then divided by 3    


# 2. Exponentiation (**) is right-associative

print(2**3**2) # Output: 512, because 3**2 is evaluated first, then 2**9  


# 3. binds tighter   than unary minus
print(-3**2) # Output: -9, because exponentiation is evaluated before unary minus
print((-3)**2) # Output: 9, because the parentheses change the order of evaluation, so -3 is evaluated first, then squared

# 4. left-to-right associativity for same-precedence operators

print(100 / 5 * 2)        # Expected: 40.0 -> / and * have same precedence; evaluated left to right
print(10 - 5 - 2)         # Expected: 3 -> - operators have same precedence; evaluated left to right


# 5. one expression mixing arithmetic, comparison, and logical operators (and, or, not)

print(3 + 4 * 2 > 10 and 5 < 3) #expected: False -> 4*2 is evaluated first, 
                                 #then 3+8=11, then 11>10 is True, and 5<3 is False, so True and False is False
print(3 + 4 * 2 > 10 or 5 < 3)  #expected: True -> 4*2 is evaluated first, 
                                 #then 3+8=11, then 11>10 is True, and 5<3 is False, so True or False is True




