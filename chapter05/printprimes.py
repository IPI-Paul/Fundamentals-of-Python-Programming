# Listing 5.36
# Uses a while loop to display all prime numbers up to a value entered by the 
# user
# Author: Rick Halterman
# Last modified: 

max_value = int(input('Display primes up to what value? '))
value = 2 # Smallest prime number
while value <= max_value:
    # See if value is prime
    is_prime = True # Provisionally, value is prime
    # Try all possible factors from 2 to value -1
    trial_factor = 2
    while trial_factor < value:
        if value % trial_factor == 0:
            is_prime = False        # Found a factor
            break                   # No need to continue; it is not prime
        trial_factor += 1           # Try the next potential factor
    if is_prime:
        print(value, end = ' ')     # Display the prime number
    value += 1                      # Try the next potential prime number
print()                             # Move to the next line