#-*-coding:utf-8

# 1번
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 2번
print()
pin = "881120-1068234"
print(pin[7])

# 3번
print()
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# 4번
print()
a = ["Life", "is", "too", "short"]
# result = " ".join(a)
# result = "{0} {1} {2} {3}".format(a[0], a[1], a[2], a[3])
result = a[0] + " " + a[1] + " " + a[2] + " " + a[3]
print(result)

# 5번
print()
a = (1, 2, 3)
a = a + (4,)
print(a)

# 6번
print()
a = {"a" : 90, "b" : 80, "c" : 70}
result = a.pop("b") # 해당하는 값을 추출하여 반환
# result = a["b"]
# del(a["b"])
print(a)
print(result)

# 7번
print()
# b[1]도 4로 변경됨
# b와 a는 같은 리스트의 주소를 참조하고 있기 때문임