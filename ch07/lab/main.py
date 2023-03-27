import rectangle

Rectangle = rectangle.Rectangle(0,0,0,0)

#Rectangle Test:
r = Rectangle(10, 10, 10, 10)
assert((r.x, r.y, r.height, r.width) == (10,10,10,10))
r = Rectangle(-1, 1, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,1,1))
r = Rectangle(1, -5, 1, 1)
assert((r.x, r.y, r.height, r.width) == (1,5,1,1))
r = Rectangle(1, 1, -10, 1)
assert((r.x, r.y, r.height, r.width) == (1,1,10,1))
r = Rectangle(1, 1, 1, -1000)
assert((r.x, r.y, r.height, r.width) == (1,1,1,1000))

