# Listing 8.5
# Uses a better algoritm than Listing 7.14. It is based on one of the oldest 
# algorithms known, attributed to Euclid around 300 BC
# Author: Rick Halterman
# Last modified: 

def gcd(m, n):
    """ 
    Uses Euclid's method to compute the greatest common divisor (also called 
    greatest common factor) of m and n.
    Returns the GCD of m and n.
    """
    if n == 0:
        return m
    else:
        return gcd(n, m % n)
    
def iterative_gcd(num1, num2):
    """
    Uses a niave algorithm to compute the greatest common divisor (also called 
    greatest common factor) of m and n.
    Returns the GCD of m and n.
    """
    # Determine the smaller of num1 and num2
    min = num1 if num1 < num2 else num2
    # 1 definitely is a common factor to all ints
    largest_factor = 1
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largest_factor = i  # Found larger factor
    return largest_factor

def main():
    """ Try out the gcd function """
    for num1 in range(1, 101):
        for num2 in range(1, 101):
            print("gcd of", num1, "and", num2, "is", gcd(num1, num2), " vs ", \
                  iterative_gcd(num1, num2))
            
main()