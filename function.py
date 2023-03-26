
# Tradational function, can modify the variables
my_nums = [1,2,3,4]

def add_to_nums(num):
    return my_nums.append(num)

add_to_nums(4)

print(my_nums)


# Pure Functions cannot modify the values outside its scope

def add_to_nums_pure(my_nums,num):
    n_lst = my_nums.copy()
    n_lst.append(num)
    return n_lst
print(my_nums)
a = add_to_nums_pure(my_nums,43)
print(a)




n_lst = my_nums.copy()
def add_to_nums_pure(num):
    n_lst.append(num)
    return n_lst
a = add_to_nums_pure(4093)
print(a)