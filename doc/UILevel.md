# Description

The `UILevel` class manages a collection of UI objects within a defined 2D grid, creating a scene or level in a UI system. 
Each level can contain multiple objects and is rendered with a customizable background character.

# Constructor

The `UILevel` constructor initializes a level with a specified width and height. The default dimensions are 20x7.
- `x` : Width of the level grid (default is 20)
- `y` : Height of the level grid (default is 7)

Example:
```python
from src.UI import UILevel
level = UILevel(x=30, y=10)
```

# Methods

`getSizeX()`
Returns the width of the level grid.

`setSizeX(x: int)`
Sets a new width for the level grid.

`getSizeY()`
Returns the height of the level grid.

`setSizeY(y: int)`
Sets a new height for the level grid.

`getPointsMap()`
Returns the dictionary storing points for each object in the level.

`setPointsMap(points_map: dict)`
Sets a new dictionary of points to represent the level.

`getObjects()`
Returns the list of objects currently in the level.

`setObjects(objects: list)`
Sets a new list of objects for the level.

`getBackgroundChar()`
Returns the character used as the background in empty areas of the level.

`setBackgroundChar(char: str)`
Sets a new background character for empty areas in the level.

`addObject(obj)`
Adds a new object to the level. Objects can be of any class implementing the UIText class or similar.

`removeObject(obj)`
Removes a specified object from the level.

`removeAllObjects()`
Removes all objects from the level.

`display()`
Renders the level grid to the console, printing each object's position as defined by its points, and fills empty spaces with the background character.

`getPoint(x: int, y: int)`
Returns the point at coordinates (x, y) if present, or None if no point exists at that position.