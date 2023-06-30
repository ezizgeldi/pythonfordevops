"""
    Write a python function  that  takes  a name as an argument and prints that name 
"""
# def  first_task(name):
#     print(f"My dog's name is {name}" )

# first_task('jack')


#write a generator  that alternates between returning Even and Old




def gem_alter():
    old = 'old'
    even = 'even'
    while True:
        old, even = even, old
        yield old


start_geb = gem_alter()

for start_geb in range(10):
    print(start_geb())