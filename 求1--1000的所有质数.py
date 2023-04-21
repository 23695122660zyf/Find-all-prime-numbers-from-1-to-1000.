s = []
for i in range(2, 2001):
    flag = True
    for j in range(2, i):
        if 0 == i % j:
            flag = False
    if flag:
        print(i)
        s.append(str(i)[-1])

c1 = s.count('1')
c3 = s.count('3')
c7 = s.count('7')
c9 = s.count('9')
print('3有', c3, '次')
print('1有', c1, '次')
print('7有', c7, '次')
print('9有', c9, '次')
print('共有', len(s), '个质数')
c = [c1, c3, c7, c9]
if max(c) == c1:
    print('擂主为1，共', c1, '次')
elif max(c) == c3:
    print('擂主为3，共',c3,'次')
elif max(c) == c7:
    print('擂主为7，共',c7,'次')
else:
    print('擂主为9，共',c9,'次')
