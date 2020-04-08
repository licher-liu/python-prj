import datetime


def log(text):
    # 装饰器函数，用于打印一行函数被调用的时间
    def decorator(func):
        def wrapper(*args, **kw):
            print(text, "function: [%s] called" % func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


now = datetime.datetime.now()


def runtime():
    # 函数运行时间装饰器
    def decorator(func):
        def wrapper(*args, **kw):
            start_time = datetime.datetime.now()
            func(*args, **kw)
            end_time = datetime.datetime.now()
            print("*"*10, "[function:%s]"%func.__name__, "*"*10)
            print("start： [%s] \nend:    [%s]" % (start_time, end_time))
            return func
        return wrapper
    return decorator


# @log(str(now))
@runtime()
def add(a, b):
    return a + b

@log("log message: " + str(now))
def sub(a, b):
    return a - b


def main():
    sum = add(5, 10)
    result = sub(10, 5)

    # print(now)


if __name__ == "__main__":
    main()
