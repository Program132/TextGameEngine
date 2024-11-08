# Description

The `Inputs` class provides a way to listen for keyboard input and trigger specific callbacks when a particular key is pressed. It helps manage user input in an efficient way, tracking both the key state and associated action.

# Constructors

Create an `Inputs` instance by specifying:
- `key` : The key to listen for (case-insensitive)
- `callback` : The function to be called when the key is pressed

Example of creating an `Inputs` instance:
```python
from src.Inputs import Inputs

def example_callback():
    print("Key pressed!")

input_listener = Inputs("a", example_callback)
```

# Methods

`listenForInput()`
Continuously listens for the specified key. When the key is pressed, if it is the first press (not held down), it triggers the callback function.

`setKey(key: str)`
Sets a new key for the listener. This key will be used for input detection.

`setCallback(callback)`
Sets or updates the callback function. Only callable functions will be assigned.

`getKey()`
Returns the current key that the listener is monitoring.