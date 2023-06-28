import sys

# def count():
#     n=0
#     while True:
#         n +=1 
#         yield n
# counter = count()
# print(next(counter))
# print(next(counter))

# def  fib():
#     first = 0
#     second = 1
#     while True:
#         first, second = second, first + second

#         yield first

# count_fib = fib()

# for x in count_fib:
#     print(x)
#     if x > 12:
#         break



list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range(100))

print(sys.getsizeof(list_o_nums))
print(sys.getsizeof(gen_o_nums))

# print(list_o_nums)


# for x in gen_o_nums:
#     print (x) 
#     if x > 5:
#         break