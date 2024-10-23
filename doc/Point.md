# Description

A point is a simple char in the "UI", it can be everything you want.

# Constructor

By default:
- `x = 0`: X position
- `y = 0`: Y position
- `char = '*'`: Character for the representation in the game
- `canCollide = False`: Collision between the object and Player object (from Player class)
- `tags = []`: Properties of the point

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

`hasTag(name: str)` Take the tag name, return true if the point has this tag

`addTag(name: str)` Take the tag name, add the tag into tags list of the point.

`removeTag(name: str)` Take the tag name, remove the tag from tags list.