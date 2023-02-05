# write a program to count for how many people a singer sings
# it should be able to differentiate the years and names and based on that it has to count

# ((t[0],t[1]),(t[0],t[1]),(t[0],t[1]),(t[0],t[1]))
# nums =(t[0],t[0],t[0],t[0])
# names = (t[1],t[1],t[1],t[1])

num = ()
names = ()

def get_data(atuple):
    
    nums = ()
    names = ()
    
    for t in atuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_num = min(nums)
    max_nums = max(nums)
    people = len(words)
    return (min_num,max_num, people)


