class Keyframe:
    def __init__(self, time_offset: float, target=None, texture=None, x=None, y=None, dx=None, dy=None):
        self.time_offset = time_offset
        self.target = target
        self.texture = texture
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def apply(self):
        if not self.target:
            return

        # Apply texture changes directly (no position interference)
        if self.texture:
            self.target.applyTexture(self.texture)

        # Apply absolute position (x, y) if defined, but these should be used rarely
        # on player parts unless it's a specific keyframe for a static position.
        if self.x is not None:
            self.target.setX(self.x)
        if self.y is not None:
            self.target.setY(self.y)

        # FIX: Instead of modifying the object's coordinates directly (which makes them drift
        # from the root), store the delta changes in the object's 'animation_offset' property.
        if self.dx is not None:
            self.target.animation_offset_x = self.dx
        if self.dy is not None:
            self.target.animation_offset_y = self.dy

        # If no delta is provided, it should explicitly reset the offset to 0.0
        if self.dx is None:
            self.target.animation_offset_x = 0.0
        if self.dy is None:
            self.target.animation_offset_y = 0.0
            
