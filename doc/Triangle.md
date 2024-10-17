# Description

Draw a triangle using this class, you can have a classic triangle with 
the highest vertice above the base of your triangle, or an inverted triangle

Example:
```
...................................................
...................................................
...................................................
...........Ʌ........\¯/............................
........../_\........V.............................
...................................................
```

# Constructor

By default:
- `seg = None`: The segment that represent your base
- `x_up = 0`: X-coordinate of the highest vertice
- `y_up = 0`: Y-coordinate of the highest vertice
- `upPointChar = 'Ʌ'`: The character by default for a classic triangle.
- `upPointCharInverted = 'V'`: The character by default for an inverted triangle.
- `canCollide = False`: Disable collision by default.


# Methods

`getBase()`  
Returns the base segment of the triangle.

`getUpPoint()`  
Returns an instance of the `Point` class that represents the apex of the triangle.

`getUpPointChar()`  
Returns a string representing the character used for the upright apex.

`getUpPointCharInverted()`  
Returns a string representing the character used for the inverted apex.

`getCanCollide(self)`  
Returns if there is collision enable or not.

`setBase(base: Segment)`  
Sets a new base segment for the triangle.

`setUpPoint(p: Point)`  
Sets a new apex point for the triangle.

`setUpPointChar(c: str)`  
Sets a new character for the apex when it is oriented upright.

`setUpPointCharInverted(c: str)`  
Sets a new character for the apex when it is oriented upside down.

`setCanCollide(c: bool)`  
Sets collision of the object.

`getPoints()`  
Calculates and returns a list of `Point` objects representing all points that form the triangle's visual representation.