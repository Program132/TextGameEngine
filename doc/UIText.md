# Description

The `UIText` class provides an interface to create a text box UI element, with configurable position, size, alignment, text content, and border characters. This class generates a rectangular box that can display text aligned horizontally and vertically.

# Constructor

The `UIText` constructor allows for creating a text box with specific dimensions, defaulting to a centered alignment:
- `x` : X position of the top-left corner (default is 3)
- `y` : Y position of the top-left corner (default is 0)
- `sx` : Width of the text box (default is 6)
- `sy` : Height of the text box (default is 1)

Example:
```python
from src.UI import UIText
ui_text = UIText(x=5, y=3, sx=10, sy=2)
```

# Methods

`getPosX`
Return X position of the top left corner.

`getPosY`
Return Y position of the top left corner.

`setPosX(x: int)`
Update X position of the top left corner.

`setPosY(y: int)`
Update Y position of the top left corner.

`getSizeX`
Return X size of the object (the rectangle).

`getSizeY`
Return Y size of the object (the rectangle).

`setSizeX(x: int)`
Update X size of the object (the rectangle).

`setSizeY(y: int)`
Update Y size of the object (the rectangle).

`getAlignmentX`
Return the alignment on the axis X

`getAlignmentY`
Return the alignment on the axis Y

`setAlignmentX(alignment: Alignment)`
Update the alignment on the axis X

`setAlignmentY(alignment: Alignment)`
Update the alignment on the axis Y

`getText`
Return the text content.

`setText(text: str)`
Update the text content.

`getBorderLeftRightChar`
Get the character of the left and right from the rectangle.

`getBorderUpChar`
Get the character of the top from the rectangle.

`getBorderBottomChar`
Get the character of the bottom from the rectangle.

`setBorderUpChar(c: str)`
Get the character of the top from the rectangle.

`setBorderBottomChar(c: str)`
Get the character of the bottom from the rectangle.

`getPoints`
Return the points of the object

