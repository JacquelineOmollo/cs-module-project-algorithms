'''
Input: a List of integers
Returns: a List of integersMoving Zeroes
'''
def moving_zeroes(arr):
    non_zero =[ 0 for i in range(arr.count(0))]
    zero = [i for i in arr if i != 0]
    zero.extend(non_zero)
    return (zero)



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")