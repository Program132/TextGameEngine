# Description

The player class gives you a specific object to create a character, the player of your game.

# Constructors

By default:
- `x = 0` The initial position on the x-axis
- `y = 0` The initial position on the y-axis
- `char = 'P'` The character representing the player
- `health = 100` The initial health of the player

Define a specific player: ``Player(X, Y, CHAR)``, 
example:
```python
p = Player(5, 3, 'A')
```

# Constructors

`getHealth()` Return the current health of the player.

`getX()` Return the current x position of the player.

`getY()` Return the current y position of the player.

`getChar()` Return the character representing the player.

`setHealth(health: int)` Set the health of the player.

`setX(x: int)` Set the x position of the player.

`setY(y: int)` Set the y position of the player.

`setChar(c: str)` Set the character representing the player.