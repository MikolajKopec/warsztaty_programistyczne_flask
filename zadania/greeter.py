def greeter(greeting):
    def impl(who):
        print(greeting+who)
    return impl
hello = greeter("Hello")
hello('Eniu')