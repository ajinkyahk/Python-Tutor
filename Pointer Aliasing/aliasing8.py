# test whether heap objects "jiggle" between steps
x = [1, [2, [3, None]]]
y = [4, [5, [6, None]]]

x[1][1] = y[1] # hopefully no jiggle!

x = set(['apple', 'banana', 'carrot'])
