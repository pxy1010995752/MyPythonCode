# 多个装饰器装饰同一参数
def outer_1(func):
    def inner(*args, **kwargs):
        print("3.5")
        ret = func(*args, **kwargs)
        return ret

    return inner


@outer_1
def outer(func):
    def inner(*args, **kwargs):
        print("123")
        ret = func(*args, **kwargs)
        print("456")
        return ret

    return inner


@outer
def index(k1, k2, k3):
    print("非常复杂")

    return k1, k2, k3


ret = index(1, 2, k3=3)

# 装饰器目的：
# 在不改变原函数代码，不改变原函数调用方式的前提情况下，让它在执行原函数之前或之后，做点什么操作
# 只要函数应用装饰器，那么函数就将被重新定义，重新定义为：装饰器的内层函数
# @outer
# 1、执行outer函数，将index作为参数传递
# 2、将outer的返回值，重新赋值给index
