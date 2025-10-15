class UIObject:
    class Alignment:
        LEFT = 0
        CENTER = 1
        RIGHT = 2
        TOP = 0
        MIDDLE = 1
        BOTTOM = 2

    def __init__(self, x=0, y=0, align_x=Alignment.LEFT, align_y=Alignment.TOP, visible=True):
        self.x = x
        self.y = y
        self.align_x = align_x
        self.align_y = align_y
        self.visible = visible
        self.computed_x = x
        self.computed_y = y

    def compute_position(self, term_cols, term_rows, content_width=0, content_height=0):
        if self.align_x == self.Alignment.LEFT:
            self.computed_x = self.x
        elif self.align_x == self.Alignment.CENTER:
            # Calcul correct de l'alignement au centre
            self.computed_x = term_cols // 2 - content_width // 2 + self.x
        elif self.align_x == self.Alignment.RIGHT:
            self.computed_x = term_cols - content_width + self.x

        if self.align_y == self.Alignment.TOP:
            self.computed_y = self.y
        elif self.align_y == self.Alignment.MIDDLE:
            self.computed_y = term_rows // 2 - content_height // 2 + self.y
        elif self.align_y == self.Alignment.BOTTOM:
            self.computed_y = term_rows - content_height + self.y

    def display(self):
        pass

    def update(self, delta):
        pass

    def get_screen_position(self):
        return self.computed_x, self.computed_y