def toStr(n,base):
    str1 = '0123456789ABCDEF'
    #比如0,1 < 2
    if n < base:
        return str1[n]
    else:
        return toStr(n//base,base) + str1[n%base]

print(toStr(233,16))



#不使用while或for
#使用小学的内容：连加 计算[1,3,5,7,9]的和
#递归计算
'''
    listSum1([1,3,5,7,9])
  =1 + listSum1([3,5,7,9])
  =3 + listSum1([5,7,9])
  =5 + listSum1([7,9])
  =7 + listSum1([9])
 '''
def listSum1(numList):
    if len(numList)  == 1:
        return numList[0]
    else:
        return numList[0] + listSum1(numList[1:])

print(listSum1([1,3,5,7,9]))



'''
计算[1,3,5,7,9]
'''
def listSum2(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    return sum

print(listSum2([1,3,5,7,9]))



#栈  实现递归

from  pythonds.basic.stack import Stack

rStack = Stack()

def toStr(n,base):
    convertString = '0123456789ABCDEF'

    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n%base])
        n = n // base
    res  = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res
print(toStr(1453,16)) #5AD  = 5*16^2 + 10*16^1 + 13*16^0
