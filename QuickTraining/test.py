print("hello world")

"""
range関数は、指定した分だけ出力する
"""
for i in range(1,5):
    print(i)

"""
変数
"""
x=200
y="hello world!"

print(x)
print(y)

"""
四則演算
"""
print(x+1)
print(x-2)
print(x*6)
print(x/4)

"""
データ型
"""
print(type(x))
print(type(y))

"""
変数
"""
print(3 * "hello" + "world")

b = 'I\'m good.' #
print(b)

"""
型変換（キャスト）
"""
a = int(1.0)
print(10 - a)

print(10 - int("5"))
print("Hello" + "World!")


"""
リスト型
"""
li = [1,2,3,4,5]
print(li)
print(len(li))

li[0] = 100

print(li)

li1 = [1,2,3]
li2 = [4,5,6]

li3 = li1 + li2
print(li3)
print(li3[0:4])
print(li3[2:5])
print(li3[:])

"""
タプル型
"""
t=(5,10)
print(t[0])

t2 = t,(1,2,3)
print(t2)

t3 = "hello",
print(t3)
print(type(t3))

"""
辞書型
"""
profile = {"name":"apple","color":"red","remarks":"hoge"}
print(profile["name"])
print(profile["color"])
profile["price"] = 140
print(profile)


"""
if文
"""
t = True
if t:
    print("trueです")

f = False
if f:
    print("Trueです")
else:
    print("Falseです")

score = 60

if score == 100:
    print("満点")
elif score > 70:
    print("合格")
else:
    print("不合格")


"""
for文
"""
for i in range(0,5):
    print(i)

"""
関数
"""
def getHello():
    print("Hello")

getHello()

def say_hello(name = "ななし"):
    print("こんにちは"+name+"さん")

say_hello("田中")
say_hello()
