# Description

A segment represents a straight line between two points, with a specific character for display, and can be configured to detect collisions.

# Constructor

By default:
- `x1 = 0`: X-coordinate of the first point.
- `y1 = 0`: Y-coordinate of the first point.
- `x2 = 0`: X-coordinate of the second point.
- `y2 = 0`: Y-coordinate of the second point.
- `collide = False`: Indicates whether the segment can collide.
- `char = '-'`: The character used to represent the segment by default.

Define a horizontal segment with collision detection:
```python
s = Segment(0, 0, 10, 0, True)
```

Define a vertical segment with a different character:
```python
s = Segment(5, 5, 5, 10, False, "|")
```

# Methods

`getX1()`
Returns the X-coordinate of the first point of the segment.

`getY1()`
Returns the Y-coordinate of the first point of the segment.

`getX2()`
Returns the X-coordinate of the second point of the segment.

`getY2()`
Returns the Y-coordinate of the second point of the segment.

`getCanCollide()`
Returns True if the segment can collide, otherwise False.

`getChar()`
Returns the character used to represent the segment.

`setX1(x: int)`
Sets the X-coordinate of the first point.

`setY1(y: int)`
Sets the Y-coordinate of the first point.

`setX2(x: int)`
Sets the X-coordinate of the second point.

`setY2(y: int)`
Sets the Y-coordinate of the second point.

`setCanCollide(canCollide: bool)`
Sets the collision property of the segment.

`setChar(char: str)`
Sets the character used to represent the segment.

`getPoints()`
Returns a list of Point objects representing all points in the segment. This method uses a line-drawing algorithm to connect the two points (x1, y1) and (x2, y2).