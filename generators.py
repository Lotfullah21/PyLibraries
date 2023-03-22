"""
any method or procedure with yield statement in it is called a generator
it has a stopIteration exception when reached the end of iteration.
it has a next() method which stops/starts execution of the procedure

"""

def fibTest():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        # fibn = fibn_1 + fibn_2
        next = fibn_1 + fibn_2
        yield next
        fibn_1 = fibn_2
        fibn_2 = next

foo = fibTest()
foo.__next__()


