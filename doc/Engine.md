# Description

The main class which contains objects, parameter for your game, etc.

You can set the size of your game, add objects, remove objects, the character for the background.

# Constructor

By default:
- `size_x = 20` The size of x-axis
- `size_y = 8` The size of y-axis
- `char = '.'` The background character
- `mainLevel = None` The current level

Define a specific "window": ``Engine(X, Y)``, 
example:
```python
from src import Engine
e = Engine(10,10)
```

Define a specific "window" and another character as background: ``Engine(X, Y, CHAR)``, 
example:
```python
from src import Engine
e = Engine(10,10, "A")
```

# Methods

`getSizeX()` Return the size on the x-axis.

`getSizeY()` Return the size on the y-axis.

`getChar()` Return the character for the background.

`display()` Call the level display function.

`refresh()` Refresh the "UI" of the game

`setCurrentLevel(l: Level)` Set the current level of the game.
