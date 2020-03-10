'''
        [54,26,93,17,77,31,44,55,20]     长度为9
    第一趟：[26,54,93,17,77,31,44,55,20] 54和26交换
    第二趟：[26,54,93,17,77,31,44,55,20] 不交换
    第三趟：[26,54,17,93,77,31,44,55,20] 17和93交换
    第四趟：[26,54,17,77,93,31,44,55,20] 77和93交换
    第五趟：[26,54,17,77,31,93,44,55,20] 31和93交换
    第六躺：[26,54,17,77,31,44,93,55,20] 44和93交换
    第七趟：[26,54,17,77,31,44,55,93,20] 55和93交换
    第八趟：[26,54,17,77,31,44,55,20,93] 20和93交换

    列表中有n项，那第一遍比较比对需要n-1次

    第二遍：[26,17,54,31,44,55,20,73,93] 需要n-2次
    第三遍：[17,26,31,44,20,54,55,73,93] 需要n-3次
    第四遍：[17,26,31,20,44,54,55,73,93] ...
    第五遍：[17,26,20,31,44,54,55,73,93]
    第六遍：[17,20,26,31,44,54,55,73,93]

'''


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:  #倒序变为 <
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] =temp
alist= [54,26,93,17,77,31,44,55,20] 
bubbleSort(alist)
print(alist)


#短冒泡排序
def bubbleSort(alist):
    flag = True
    passnum = len(alist) - 1


    while flag and passnum>0:
        flag = False
        for i in range (passnum):
            if alist[i] > alist[i+1]:  #倒序变为 <
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] =temp
                flag = True
alist= [54,26,93,17,77,31,44,55,20] 
bubbleSort(alist)
print(alist)


#选择排序
def selectionSort(alist):
    for fillsort in range(len(alist)-1,0,-1):
        maxPos = 0
        for location in range(1,fillsort+1):
            if alist[location] > alist[maxPos]:
                maxPos = location

        temp = alist[fillsort]
        alist[fillsort] = alist[maxPos]
        alist[maxPos] = temp

alist= [54,26,93,17,77,31,44,55,20] 
selectionSort(alist)
print(alist)


'''
    插入排序
'''
def insertSort(alist):
    for i in range(1,len(alist)):
        currenValue = alist[i]
        while i > 0 and alist[i - 1] > currenValue:
            alist[i] = alist[i - 1]
            i = i - 1

        alist[i]  =currenValue

alist = [54,26,93,17,77,31,44,55,20] 
insertSort(alist)
print(alist)