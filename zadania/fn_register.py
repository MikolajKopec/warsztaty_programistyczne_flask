class Fn_register:
    def __init__(self):
        self.sl = {}
    def register(self,name = None):
        def impl(function):
            nonlocal name
            if name is None:
                name = function.__name__
            self.sl[name]=function
            return function
        return impl
    def call(self,name):
        return self.sl[name]

fn = Fn_register()

@fn.register('p')
def printer(x):
    print(x)

print(fn.sl)
fn.call('p')('Hello, World!')