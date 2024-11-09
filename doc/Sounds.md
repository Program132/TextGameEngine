# Description

The `Sounds` class allows for the management and playback of audio files in your game.

# Constructor

By default:
- `pathSound = ""`: The file path of the audio file to be played.
- `repeat = False`: Whether the audio should loop continuously.
- `audio = None`: Placeholder for the audio object once loaded.
- `is_playing = False`: A boolean indicating whether the audio is currently playing.

Example:

```python
from src.Sounds import Sounds

sound = Sounds("path/to/sound.wav", repeat=True)
sound.play()
```

# Methods

`play()`
Plays the audio file specified by pathSound. If repeat is set to True, the audio loops continuously until stopped. 
If the file is not found, an error message is printed.

`stop()`
Stop the audio if it is currently playing.

`setPath(path: str)`
Sets a new file path for the audio file.

`getPath()`
Returns the current file path of the audio file.