'''
    练习：
        写一个函数需要一个列表和我们正在搜索的项作为参数，
        并返回一个是否存在的布尔值   found = False
'''

def foundSearch(alist,item):
    found = False
    pos = 0
    while pos < len(alist) and not found:
        if alist[pos]  == item:
            found = True
        else:
            pos = pos + 1

    return found

alist = [1,3,5,8,12,62]
print(foundSearch(alist,12))
print(foundSearch(alist,20))


'''
    升序[17,20,25,30,56,76,99]
    假设寻找的项在列表中
    假设寻找的项不在列表中， 如：50   ---我们在30-56比对一下
'''
#当知道list为升序
def orderSearch(alist,item):
    found = False
    pos = 0
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found
alist = [17,20,25,30,56,76,99]
print(orderSearch(alist,25))
print(orderSearch(alist,35))



'''
    二分查找:从中间开始查找 ---每次都是从中间项进行对比
'''
#有序  [17,20,25,30,56,76,99]
def binarySearch(alist,item):
    found = False
    first = 0
    last = len(alist) - 1

    while first<=last and not found:
        # 中间
        midpoint = (first+last) // 2

        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


alsit = [17,20,25,30,56,76,99]
print(binarySearch(alist,88))


#递归实现二分查找
def dgbinarySearch(alist,item):

    midpoint = len(alist) // 2
    if alsit[midpoint] == item:
        return True
    else:
        if alist[midpoint] > item:
            return dgbinarySearch(alist[:midpoint],item)
        else:
            return dgbinarySearch(alist[midpoint+1:],item)

alsit = [17,20,25,30,56,76,99]
print(dgbinarySearch(alist,88))   