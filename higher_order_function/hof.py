def apply_function(f,x):
    return f(x)
def double(n):
    return n*2

result = apply_function(double,10)
print(result)

def multiplier(factor):
    def multiply(x):
        return x*factor
    return multiply

double = multiplier(2)
print(double(10))