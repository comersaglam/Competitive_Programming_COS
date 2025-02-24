def dothis(x, y = 8):
    print(x*y)


import inspect

def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }
sign = get_default_args(dothis)
print(sign)
dothis(2,8)