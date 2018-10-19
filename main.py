#тест
l = [i  for i in range(10)]
print(l)
print(type(l))

d={i: i**6 for i in range(10)}
print(d)
print(type(d))

s={i for i in range(10)}
print(s)
print(type(s))

g=(i for i in range(10))
print(g)
#print(type

points = []
for x in range(5):
	for y in range(3):
		points.append((x, y))

print(points)


def hypervalue(*args):
	print(args)
	print(type(args))

hypervalue(23,4,5,5,34,'sd',"hello")
