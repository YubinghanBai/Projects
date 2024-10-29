from math import sqrt

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

# def golden_update(guess):
#     return 1/guess+1

# def square_close_to_successor(guess):
#     return approx_eq(guess*guess,guess+1)

def approx_eq(x, y, tolerance=1e-15):
    return abs(x-y) < tolerance

# phi=1/2+sqrt(5)/2
# def improve_test():
#     approx_phi=improve(golden_update, square_close_to_successor)
#     assert approx_eq(phi,approx_phi) #improve_test 函数在 assert 语句执行成功后会返回 None。
#     print(approx_phi)



def average(x,y):
    return (x+y)/2
def sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x*x,a)
    return improve(sqrt_update,sqrt_close)

print(sqrt(3))