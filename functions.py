# ### fucntion is a mechanism for encapsulating  a block of code ###

# def position(first, second):

#     print(f'this is the {first} argument')
#     print(f'this is the {second} argument')

# position(1, 2)


# def keyword(first=1,second=2):
#     print(f'this is the {first} argument')
#     print(f'this is the {second} argument')

# keyword()

def second(input):
    return input*3

def first(input):
    return input*45

functions = [second, first]
for func in functions:
    print(func(3))

