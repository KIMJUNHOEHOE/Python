import turtle as t

angle = 45
colors = ['red','green','blue','yellow','purple','cyan','magenta','violet']

for i in range(1,50):
    mod = (i-1)%8
    print(mod)
    t.color(colors[mod])
    t.pensize(i/10)
    t.forward(i * 2)
    t.left(angle)

t.done()