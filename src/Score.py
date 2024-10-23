class Score:
    def __init__(self):
        self.scores = {}
        self.enableTitle = True
        self.enablePredecessorScore = True
        self.title = "Score.md: \n"
        self.predecessorScore = "- "

    def getScores(self):
        return self.scores

    def addScore(self, scoreName: str, scoreDefaultValue):
        self.scores[scoreName] = scoreDefaultValue

    def getScore(self, scoreName: str):
        if scoreName in self.scores.keys():
            return self.scores[scoreName]
        return None

    def updateScore(self, scoreName: str, value):
        if scoreName in self.scores.keys():
            self.scores[scoreName] = value

    def changeTitle(self, t: bool):
        self.enableTitle = t

    def changePredecessorScoreName(self, t: bool):
        self.enablePredecessorScore = t

    def showTitle(self):
        return self.enableTitle

    def showPredecessorScore(self):
        return self.enablePredecessorScore

    def setTitle(self, n: str):
        self.title = n

    def setPredecessorScore(self, n: str):
        self.predecessorScore = n

    def getTitle(self):
        return self.title

    def getPredecessorScore(self):
        return self.predecessorScore
