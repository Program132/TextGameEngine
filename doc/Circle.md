# Description

This class allows you to draw a circle using customizable characters for the top, bottom, left, and right borders. 
The circle is defined by a center point (`x`, `y`) and a radius (`r`). The inside of the circle remains empty.

# Constructor

By default:
- `x = 0`: X-coordinate of the circle's center.
- `y = 0`: Y-coordinate of the circle's center.
- `r = 1`: Radius of the circle.
- `UpChar = '_'`: Character representing the top of the circle.
- `LeftRightChar = '|'`: Character representing the left and right sides of the circle.
- `DownChar = '¯'`: Character representing the bottom of the circle.
- `VoidChar = ''`: The empty space inside the circle.

Exemple:

```python
from src.Models.Circle import Circle
from src.Engine import Engine
from src.Level import Level

engine = Engine(50, 5, ".")
mainLevel = Level(engine)
mainLevel.addObject(Circle(10, 3, 2))
engine.setCurrentLevel(mainLevel)
engine.display()
```
```
...................................................
.........._........................................
.........   .......................................
........| . |......................................
.........   .......................................
..........¯........................................
```


# Methods

`getCenterX()`  
Returns the X-coordinate of the circle's center.

`getCenterY()`  
Returns the Y-coordinate of the circle's center.

`getRayon()`  
Returns the radius of the circle.

`getUpChar()`  
Returns the character used for the top of the circle.

`getLeftRightChar()`  
Returns the character used for the left and right sides of the circle.

`getDownChar()`  
Returns the character used for the bottom of the circle.

`getVoidChar()`  
Returns the character representing the empty space inside the circle.

`setCenterX(x: int)`  
Sets a new X-coordinate for the circle's center.

`setCenterY(y: int)`  
Sets a new Y-coordinate for the circle's center.

`setRayon(r: int)`  
Sets a new radius for the circle.

`setUpChar(char: str)`  
Sets a new character for the top of the circle.

`setLeftRightChar(char: str)`  
Sets a new character for the left and right sides of the circle.

`setDownChar(char: str)`  
Sets a new character for the bottom of the circle.

`setVoidChar(char: str)`  
Sets a new character for the empty space inside the circle.

`getPoints()`  
Calculates and returns a list of `Point` objects representing all the points that form the visual representation of the circle.