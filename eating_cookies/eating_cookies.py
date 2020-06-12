'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n, cache=None):
    # base case
    if n == 0:
        return 1
    # check for negative n values
    elif n < 0:
        return 0
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if not cache:
            cache = [0 for _ in range(n+1)]
    # represent recursive case where there are still cookies to be eaten
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

if __name__ == "__main__":
# Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
