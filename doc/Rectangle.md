# Description

A rectangle is defined by two points: the top-left corner and the bottom-right corner. It can be graphically represented using segments for its sides.

# Constructor

By default:
- `up_x = 0`: X-coordinate of the top-left corner.
- `up_y = 0`: Y-coordinate of the top-left corner.
- `down_x = 1`: X-coordinate of the bottom-right corner.
- `down_y = 1`: Y-coordinate of the bottom-right corner.
- `collide = False`: Indicates whether the rectangle can collide.

Define a rectangle without collision detection:
```python
r = Rectangle(0, 0, 10, 5)
```

Define a rectangle with collision detection:
```python
r = Rectangle(2, 2, 8, 6, True)
```

# Methods

`getUpX()`
Returns the X-coordinate of the top-left corner.

`getUpY()`
Returns the Y-coordinate of the top-left corner.

`getDownX()`
Returns the X-coordinate of the bottom-right corner.

`getDownY()`
Returns the Y-coordinate of the bottom-right corner.

`getCanCollide()`
Returns True if the rectangle can collide, otherwise False.

`setUpX(x: int)`
Sets the X-coordinate of the top-left corner.

`setUpY(y: int)`
Sets the Y-coordinate of the top-left corner.

`setDownX(x: int)`
Sets the X-coordinate of the bottom-right corner.

`setDownY(y: int)`
Sets the Y-coordinate of the bottom-right corner.

`setCanCollide(c: bool)`
Sets the collision property of the rectangle.

`getSegments()`
Returns a list of segments representing the four sides of the rectangle:
- One segment for the top (horizontal, '-').
- One segment for the bottom (horizontal, '-').
- One segment for the left (vertical, '|').
- One segment for the right (vertical, '|').

`getPoints()`
Returns a list of all points forming the sides of the rectangle, using the segments defined by the `getSegments()` method.