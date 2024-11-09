# Description

The `Score` class allows you to manage a scoring system in your game, including tracking and updating multiple score types. Each score type has its own name and value, and you can control how scores are displayed with titles and predecessors.

# Constructor

By default:
- `scores = {}`: A dictionary to store score names and their corresponding values.
- `enableTitle = True`: A boolean to toggle the display of the title.
- `enablePredecessorScore = True`: A boolean to toggle the display of the predecessor score.
- `title = "Score: "`: The title displayed before the score.
- `predecessorScore = "- "`: A string that appears before each score.

Example:

```python
from src.UI import Alignment, Score

score = Score()
score.addScore("PlayerScore", 100)
score.setTitle("High Scores")
score.setAlignment(Alignment.CENTER)
print(score.getScore("PlayerScore"))
```

# Methods

`addScore(scoreName: str, scoreDefaultValue)`
Adds a new score with a given name and default value to the score list.

`getScore(scoreName: str)`
Returns the value of the specified score.

`updateScore(scoreName: str, value)`
Updates the value of the specified score.

`getScores()`
Returns all the scores as a dictionary.

`changeTitle(t: bool)`
Enables or disables the display of the title.

`changePredecessorScoreName(t: bool)`
Enables or disables the display of the predecessor score.

`setTitle(n: str)`
Sets a new title for the score display.

`setPredecessorScore(n: str)`
Sets a new predecessor string for the score display.

`showTitle()`
Returns the boolean value indicating if the title is enabled.

`showPredecessorScore()`
Returns the boolean value indicating if the predecessor score is enabled.

`getTitle()`
Returns the current title.

`getPredecessorScore()`
Returns the current predecessor string.

`setAlignment(alignment: Alignment)`
Sets the alignment for the text displayed in the score output. Available options are Alignment.LEFT, Alignment.CENTER, and Alignment.RIGHT.

`getAlignment()`
Returns the current alignment setting.

`alignText(text: str, width: int) -> str`
Applies the specified alignment to the given text, fitting it within the specified width. This method uses the alignment attribute to determine how to align each line (left, center, or right).