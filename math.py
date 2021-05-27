#
# Cheat Sheet for Math Statistics Exam
#

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from prettytable import PrettyTable


print('enter sample like 2 5 1 321 3')
data = sorted(list(map(int,input().split())))

xn = Counter(data)

x = list(xn.keys())
n = list(xn.values())
w = [i / sum(xn.values()) for i in xn.values()]
R = max(x) - min(x)
Xv = sum([x[i] * n[i] for i in range(len(x))]) / sum(n)
Db = sum([(x[i] - Xv) ** 2 for i in range(len(x))]) / sum(n)
Ub = Db ** .5
s = (sum(n) / (sum(n) - 1)) ** .5
V = 100 * Ub / Xv
Mo = x[n.index(max(n))]

F = [(0, -float('inf'), x[0])]
F += [(n[i], x[i], x[i + 1]) for i in range(len(x) - 1)]
F += [(1, x[-1], float('inf'))]

table = PrettyTable()
table.title = 'Discrete series'
table.field_names = ['x', *x]
table.add_row(['n', *n])
table.add_row(['w', *w])
print(table, '\n')

middle = 0 if len(F) % 2 == 1 else 1
print("		  0, {} < x <= {}".format(F[0][1], F[0][2]))
for f in range(1, len(F) - 1):
	if f == len(F) // 2 - middle:
		print("F*(x) = {", "{}/{}, {} < x <= {}".format(sum(n[0:f]), sum(n), F[f][1], F[f][2]))
	else:
		print("		  {}/{}, {} < x <= {}".format(sum(n[0:f]), sum(n), F[f][1], F[f][2]))
print("		  1, {} < x < {}\n".format(F[-1][1], F[-1][2]))

print("R = max(x) - min(x) =", R)
print("Xв = ", Xv)
print("Db = ", Db)
print("Ub = ", Ub)
print("s  = ", s)
print("V  = ", V)
print("Mo = ", Mo)

def createLine(name, x, y, colorLine="blue", grid=True, width=3, xname="x", yname="y"):
	plt.title(name)
	plt.axis([0, 1.5 * max(x), 0, 1.5 * max(y)])
	x1, y1 = x[1::], y[1::]
	x2, y2 = x[:-1], y[:-1]
	plt.xlabel(xname,loc="right")
	plt.ylabel(yname,loc="center")
	plt.plot(x1, y1, x2, y2, marker = 'o', color = colorLine, linewidth = width)
	plt.grid(grid)

plt.figure(figsize=(12, 4))

plt.figtext(0.5, -0.1, "figtext")
plt.suptitle("Polygons")

plt.subplot(121)
createLine('frequency', x, n, yname="n")

plt.subplot(122)
createLine("relative frequency", x, w, yname="w")

plt.show()
