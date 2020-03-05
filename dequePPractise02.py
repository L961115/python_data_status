
# class Deque:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def addFront(self, item):
#         self.items.append(item)

#     def addRear(self, item):
#         self.items.insert(0,item)

#     def removeFront(self):
#         return self.items.pop()

#     def removeRear(self):
#         return self.items.pop(0)

#     def size(self):
#         return len(self.items)


#双端队列--回文词
def palchecker(astring):
    chardeque = []
    for ch in astring:
        chardeque.append(ch)

    flag = True
    while len(chardeque) > 1 and flag:
        first = chardeque.pop()
        last = chardeque.pop(0)
        if first != last:
            flag = False
    return flag

print(palchecker("山西运煤车煤运山西"))

#专业版
from pythonds.basic.deque import Deque
def palChecker(aSting):
    chardeque = Deque()
    for ch in aSting:
        chardeque.addFront(ch)

    flag = True
    while len(chardeque) >1 and flag:
        first = chardeque.removeFront()
        last = chardeque.removeRear()

        if first != last:
            flag = False

    return flag
print(palChecker('上海自来水来自上海'))
