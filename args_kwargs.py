def args_connect(*args):
    print(type(args))
    print(args)

args_connect('localhost', 22)

def kwargs_connect(**kwargs):
    print(type(kwargs))
    print(kwargs)

kwargs_connect(host='localhost', port=22)

def args_kwargs_connect(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)

args_kwargs_connect('localhost', 22, host='localhost', port=22)