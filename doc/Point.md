# Description

A point is a simple char in the "UI", it can be everything you want.

# Constructor

By default:
- x = 0
- y = 0
- char = '*'

Define a specific position: ``Point(X, Y)``, 
example:``p = Point(10,10)``

Define a specific "window" and another character as background: ``Point(X, Y, CHAR)``, 
example:
```python
p = Point(10, 10, "$")
```

# Methods

`getX()` Return the abs of the point.

`getY()` Return the ord of the point.

`getChar()` Return the character of the point.

`setX(x: int)` Take an int for the new abs of the point.

`setY(x: int)` Take an int for the new ord of the point.

`setChar(x: int)` Take an int for the new ord of the point.