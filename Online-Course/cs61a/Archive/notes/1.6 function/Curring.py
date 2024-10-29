"""
Curring柯里化
每个函数接受一个参数。给定一个函数 f(x, y)，
定义另一个函数 g 使得 g(x)(y) 等价于 f(x, y)。
在这里，g 是一个高阶函数，它接受单个参数 x 并返回另一个接受单个参数 y 的函数。
这种转换称为柯里化（Curring）。
"""
def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h
def map_to_range(start,end,f):
    while start<end:
        print(f(start))
        start += 1

map_to_range(0,10,curried_pow(2))

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f

pow_curried=curry2(pow)
