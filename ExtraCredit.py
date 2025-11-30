"""
Reverse-multiple searcher

Assignment goals:
- Verify the claim 2178 * 4 = 8721 (using strings) and show if it is true or false.
- Use loops to find all 4-digit numbers n such that n * 4 = reverse(n).
- Try 5-digit and larger numbers.
- Make the program generic so it can work for any number of digits.
- Measure run time and comment on whether CPU time is an issue.
- Include simple shortcuts (for example: 2178 * 4 must be > 8000).
"""

import time


# --------- Core helper: check "reverse multiple" using strings --------- #

def is_reverse_multiple(n, factor=4):
    """
    Return True if factor * n is the digit-wise reverse of n.

    Implementation must be string-based:
    - convert the number to a string
    - reverse the string
    - compare with the product, also as a string
    """
    s = str(n)           # original number as string
    reversed_s = s[::-1] # string reversed
    product = factor * n
    product_s = str(product)

    return product_s == reversed_s


# --------- Part 1: Verify the specific claim 2178 * 4 = 8721 --------- #

n = 2178
factor = 4

print("=== Checking the specific claim: 2178 * 4 = 8721 ===\n")

original_str = str(n)
reversed_str = original_str[::-1]
product_str = str(n * factor)

print("Number as string:           ", original_str)
print("Reversed number as string:  ", reversed_str)
print("Actual 2178 * 4 as string:  ", product_str)

if is_reverse_multiple(n, factor):
    print("Result: The claim is TRUE – 2178 * 4 is the reverse of 2178.\n")
else:
    # This is what really happens: 2178 * 4 = 8712, not 8721
    print("Result: The claim is FALSE – 2178 * 4 is NOT the reverse of 2178.\n")


# --------- Generic search for any digit length --------- #

def find_reverse_multiples(num_digits, factor=4):
    """
    Find all num_digits-digit numbers n such that factor * n = reverse(n).

    Generic:
    - works for 2 digits, 3 digits, 4 digits, ..., etc.
    - uses a small shortcut: we only search n such that factor * n
      still has num_digits digits.
    """
    # Smallest num_digits-digit number, e.g., num_digits=4 -> 1000
    start = 10 ** (num_digits - 1)
    # One past the largest num_digits-digit number, e.g., 4 -> 10000
    end = 10 ** num_digits

    # Shortcut:
    # We need factor * n to still be a num_digits-digit number.
    # That means: factor * n <= 10^num_digits - 1
    # So n <= (10^num_digits - 1) / factor.
    max_n_by_product_digits = (10 ** num_digits - 1) // factor
    upper_limit = min(end, max_n_by_product_digits + 1)

    results = []

    for n in range(start, upper_limit):
        if is_reverse_multiple(n, factor):
            results.append(n)

    return results


def timed_search(num_digits, factor=4):
    """
    Time how long it takes to search all num_digits-digit numbers
    for the property: factor * n = reverse(n).
    """
    print(f"=== Searching for {num_digits}-digit numbers n with n * {factor} = reverse(n) ===")

    t0 = time.perf_counter()
    matches = find_reverse_multiples(num_digits, factor)
    t1 = time.perf_counter()

    elapsed = t1 - t0

    if matches:
        print("Matches found:", matches)
        for m in matches:
            print(f"  {m} * {factor} = {factor * m}")
    else:
        print("No matches found.")

    print(f"Search time: {elapsed:.6f} seconds\n")
    return elapsed


# --------- Part 2: 4-digit numbers --------- #

time_4 = timed_search(4, 4)


# --------- Part 3: 5-digit numbers and bigger --------- #

time_5 = timed_search(5, 4)
time_6 = timed_search(6, 4)  # example “bigger number” case


# --------- Part 4: CPU time discussion --------- #

print("=== CPU Time Summary (seconds) ===")
print(f"4-digit search : {time_4:.6f}")
print(f"5-digit search : {time_5:.6f}")
print(f"6-digit search : {time_6:.6f}\n")

print("Comment on CPU time:")
print("- The number of values to check grows as the number of digits grows.")
print("- However, for 4, 5, or 6 digits, the total time is still very small")
print("  on a modern CPU, so brute-force search is fine for this assignment.")
print("- For extremely large digit counts, we would need more math shortcuts")
print("  instead of checking every possible number.\n")

print("Example shortcut reasoning for 2178:")
print("- 2178 is a 4-digit number, so 2178 * 4 must be between 4000 and 9999.")
print("- To be the reverse, the product must start with '8', so it is in the")
print("  8000–8999 range. That implies the original number must start with '2'")
print("  (because 4 * 2xxx is around 8xxx). This narrows the 4-digit search")
print("  down to 2000–2499 instead of 1000–2499.")
