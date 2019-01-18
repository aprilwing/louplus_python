#!/usr/bin/env python3
import copy

def compute(base, value):
    #base2 = base[:] 另一种写法
    base2 = copy.copy(base)
    base2.append(value)
    print(sum(base2))

if __name__=='__main__':
    testlist = [10, 20, 30]
    compute(testlist, 15)
    compute(testlist, 25)
    compute(testlist, 35)


