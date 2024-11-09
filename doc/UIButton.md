# Description

The `UIButton` class represents a clickable button in a UI, extending the `UIText` class to add functionality for detecting key presses and triggering a callback action. 
Each button displays text with an assigned key, which is shown in parentheses.

# Constructor

The `UIButton` constructor allows for creating a button with a specific position, size, and assigned activation key. The default key is 'S'.
- `x` : X position of the button’s top-left corner (default is 3)
- `y` : Y position of the button’s top-left corner (default is 0)
- `sx` : Width of the button (default is 6)
- `sy` : Height of the button (default is 1)
- `key` : Key assigned to activate the button (default is `'S'`)

Example:
```python
from src.UI import UIButton
button = UIButton(x=5, y=3, sx=10, sy=2, key='p')
```

# Methods 

**The UIButton inherits all methods from the [UIText](UIText.md) class, allowing full customization of the button’s appearance, position, alignment, and borders.**

`setOnClick(callback)`
Sets the callback function to be executed when the button is clicked. The callback function must be callable.

`listenForClick()`
Monitors if the assigned key is pressed. When pressed, it triggers the on_click_callback function if it has been set, ensuring the button is not triggered multiple times in a single press.

`getKey()`
Returns the key currently assigned to the button for activation.

`setKey(key: str)`
Sets a new activation key for the button. The button’s display text is updated to reflect the new key in parentheses.