'''
乱序字符是指一个字符串只是另一个字符串的重新排列
前提：字符串由26个小写字母集合组成，长度相同
比如： python  typhon   head  deah
目的：
    写一个布尔函数（返回值是布尔值的函数）
    solutions1（‘abcd’,'dbca')

'''

#1、穷举法：排除；原因：如果字符串过长，20个长度 20！

#检查  第一个字符串是不是出现在第二个字符串中
def solutions1(s1,s2):
    alist = list(s2)

    pos1 = 0
    flag = False
    while flag and pos1 < len(s1):
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1


        if found:
            alist[pos2] = None
            pos1 = pos1 + 1
        else:
            flag = False

    return flag

print(solutions1('abcd','cabd'))
print(solutions1('python','tphona'))


#计数和比较法   aaaabbbbcccc  ccccaaaabbbb
#计算每个字符出现的次数 26 = [a,b,c,d...]
#算法复杂度 

def solutions2(s1,s2):
    c1 = [0] * 26 #记录s1中字母出现的次数[4,4,4,0,0,0...]
    c2 = [0] * 26

    #ord()返回的是字符在阿斯克码中的数字
    for i  in range (len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] +1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1


    count = 0 #如果某个字符在s1和s2中出现的次数相同，namecount+1
    flag = True

    while count < 26 and flag:
        if c1[count] == c2[count]:
            count = count + 1
        else:
            flag = False
        
    return flag

print(solutions2('aaaabbbbcccc','bbbbaaaacccc'))
print(solutions2('python','thonpy'))

#排序和比较：即使s1,s2不同 他们都是由完全相同的字符串组成的
#我们可以按照从a-z排序每一个字符串，如果两个字符相同，那这两个字符就是乱序字符穿
#aaaabbbbcccc bbbbccccaaaa
def solutions3(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    #排序  排序通常复杂度O（n^2)或者O(logn)
    alist1.sort()
    alist2.sort()

    flag = True

    pos = 0

    while pos < len(s1) and flag:
        if alist1[pos]  == alist2[pos]:
            pos = pos + 1
        else:
            flag = False
    return flag

print(solutions3('aaaabbbbcccc','bbbbaaaacccc'))
print(solutions3('python','typhon'))

