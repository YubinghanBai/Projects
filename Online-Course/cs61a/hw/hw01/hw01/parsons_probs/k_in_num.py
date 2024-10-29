def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    if num==0:
        return False
    while num>0:
        temp = num%10
        num//=10
        if k==temp:
            return True
print(k_in_num(3, 123))  # True
print(k_in_num(2, 123))  # True
print(k_in_num(5, 123))  # False
print(k_in_num(0, 0))  # False