'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # base case
    if n == 0:
        return 1
    # check for negative n values
    elif n <= 0:
        return 0
    # represent recursive case where there are still cookies to be eaten
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
