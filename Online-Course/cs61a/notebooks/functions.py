#1.可接受任意数量参数的函数
import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    #' %s="%s"' % item ,使用 % 操作符来将变量或值插入字符串中
    #假设item=("size","large")-->' size="large"'
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value)) #转义value中的特殊字符,保护内容不受HTML注入攻击的风险,以确保他们不会被解析成HTML标签
    return element

# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)

# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')


#2.只接受关键字参数的函数
"""
强制关键字参数
如果在参数列表中出现一个 *，之后的所有参数都必须使用关键字来传递


"""
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

minimum(1, 5, 2, -5, 10) # Returns -5
minimum(1, 5, 2, -5, 10, clip=0) # Returns 0


#3.给函数参数增加元信息(使用函数参数注解)
def add(x:int, y:int) -> int:
    return x + y

#4.返回多个值的函数
"""
myFunc看似返回了多个值,实际上是先创建了一个元祖后返回的
用逗号生成一个元组,而不是括号
将结果赋值给多个变量--元组解包
返回结果也可以赋值给单个变量--元组本身

"""
def myFunc():
    return 1, 2, 3
a,b,c=myFunc()
a
b
c
x=myFunc()
x

#5.定义有默认参数的函数
"""
在函数定义中给参数指定一个默认值，并放到参数列表最后
如果默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用None作为默认值
传递一个None值和不传值两种情况是有差别的
默认参数的值应该是不可变的对象，比如None、True、False、数字或字符串
不能,命名为[],以免后续下次调用时修改函数默认值
"""
#仅测试是否某个默认参数有值传进来
_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
#默认参数仅仅在函数定义时赋值一次
x=42
def spam(a,b=x):
    print(a,b)
spam(1)#1 42
x=23 #Has no effect
spam(1) #1 42