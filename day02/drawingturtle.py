import math
import turtle as t

var1 = input('색깔입력 : [red, blue] ')
var2 = int(input('한변의 길이 입력 : [100-200] '))

t.color(var1)
t.pensize(3)

t.left(0)
t.forward(var2)

t.left(120)
t.forward(var2)

t.left(120)
t.forward(var2)

t.left(30)
t.forward(var2)

t.left(90)
t.forward(var2)

t.left(90)
t.forward(var2)

t.left(135)
t.forward(math.sqrt(var2**2+var2**2))

t.left(135)
t.forward(var2)

t.left(135)
t.forward(math.sqrt(var2**2+var2**2))

t.done()
