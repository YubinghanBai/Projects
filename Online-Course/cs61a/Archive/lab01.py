def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    mul=1
    for i in range(n,k,-1):
        mul*=i
    return mul
print(falling(6,3))


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    y_str=str(y)
    sum=0
    for i in range(len(y_str)):
        sum+=int(y_str[i])
    return sum
    # 法二
    # total =0
    # while y>0:
    #     total,y=total+y%10,y//10
print(sum_digits(1234567890))
print(sum_digits(12345))

def double_eights(n): #EthanTemp #cs61aProblemsets


    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    count=0
    while n>0:

def k_occurrence(k, num):
    occurrence = 0
    while num > 0:
        if num % 10 == k:
            occurrence += 1
        num //= 10
    return occurrence