def div(a,b):
    sol= a/b
    print(sol)
def modify_div(fun):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return fun(a,b)
    return inner
div=modify_div(div)
div(4,8)