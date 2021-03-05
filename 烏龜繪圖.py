import turtle as bigturtlehead
bigturtlehead.color('red',)

l=int(input("How many angle you want"))

for i in range(l):
  bigturtlehead.begin_fill()
  bigturtlehead.forward(30)
  bigturtlehead.left(360/l)

