# Description

The main class which contain objects, parameter for your game, etc.

You can set size of your game, add objects, remove objects, the character for the background.

# Constructor

By default:
- size_x = 20
- size_y = 8
- char = '.'

Define a specific "window": ``Engine(X, Y)``, 
example:
```python
e = Engine(10,10)
```

Define a specific "window" and another character as background: ``Engine(X, Y, CHAR)``, 
example:
```python
e = Engine(10,10, "A")
```

# Methods

`display()` Show the game.

`addObject(object)` Add an object ([Point](Point.md), [Segment](Segment.md), etc.) to list of objects

`removeObject(x:int ,y:int)` Remove an object from list of objects (need the position, so X and Y)

`refresh()` Refresh the "UI" of the game

