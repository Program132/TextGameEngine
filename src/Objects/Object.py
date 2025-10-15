import abc
from src.Enums.EventType import EventType
from src.Utils.Color import Color
from src.Textures.Texture import Texture

class Object:
    GRAVITY = 9.8

    def __init__(self, x, y, char="O"):
        self.x = float(x)
        self.y = float(y)
        self.vx = 0.0
        self.vy = 0.0
        self.char = char
        self.Anchored = True
        self.CanCollide = True
        self.width = 1
        self.height = 1
        self.fill = True
        self.points = []
        self.events = {}
        self.currently_touching = set()
        self.texture = None
        self.was_moving = False
        self.is_grounded = False
        self.animations = {}
        self.current_animation = None

        # FIX: Nouvelles propriétés pour stocker le décalage de l'animation (ex: le 'head bob')
        self.animation_offset_x = 0.0
        self.animation_offset_y = 0.0

        self.updatePoints()

    def add_animation(self, name: str, animation: 'Animation'):
        self.animations[name] = animation

    def start_animation(self, name: str, force_restart=False):
        if name in self.animations:
            anim = self.animations[name]
            if anim != self.current_animation or force_restart:
                if self.current_animation:
                    self.current_animation.stop()
                self.current_animation = anim
                anim.start()
        elif self.current_animation:
            self.current_animation.stop()
            self.current_animation = None

    def stop_animation(self):
        if self.current_animation:
            self.current_animation.stop()
            self.current_animation = None
        # FIX: Réinitialiser les offsets d'animation lorsque l'animation s'arrête
        self.animation_offset_x = 0.0
        self.animation_offset_y = 0.0


    def getX(self): return int(self.x)
    def setX(self, value): self.x = float(value); self.updatePoints()
    def getY(self): return int(self.y)
    def setY(self, value): self.y = float(value); self.updatePoints()

    def addEvent(self, event_type: EventType, func):
        if event_type not in self.events:
            self.events[event_type] = []
        self.events[event_type].append(func)

    def triggerEvent(self, event_type: EventType, **kwargs):
        if event_type in self.events:
            for func in self.events[event_type]:
                func(**kwargs)

    def getPoints(self): return self.points

    def updatePoints(self):
        self.points = []

        # FIX: Les points sont calculés en utilisant la position de base (self.x, self.y)
        # PLUS le décalage d'animation (animation_offset_x/y).
        base_x = self.x + self.animation_offset_x
        base_y = self.y + self.animation_offset_y

        for dy in range(self.height):
            for dx in range(self.width):
                if self.fill or dy in [0, self.height - 1] or dx in [0, self.width - 1]:

                    px = int(base_x) + dx
                    py = int(base_y) + dy

                    color = (255, 255, 255)
                    if self.texture:
                        tx = dx % self.texture.width
                        ty = dy % self.texture.height
                        color = self.texture.getPixelColor(tx, ty)
                    self.points.append((px, py, (self.char, color)))

    def update(self, delta, level):
        moving_now = not self.Anchored and (self.vx != 0 or self.vy != 0)
        self.is_grounded = False

        # L'animation s'exécute, ce qui met à jour animation_offset_x/y (voir Keyframe corrigé)
        if self.current_animation:
            self.current_animation.update(delta)

        if not self.Anchored:
            self.vy += self.GRAVITY * delta

            new_x = self.x + self.vx * delta
            new_y = self.y + self.vy * delta

            self.check_vertical_collision(level, new_y)
            self.check_horizontal_collision(level, new_x)

        # Les points sont mis à jour avec la NOUVELLE self.x/self.y et l'animation_offset_x/y
        self.updatePoints()

        if moving_now:
            self.triggerEvent(EventType.MOVING, obj=self)
        if self.was_moving and not moving_now:
            self.triggerEvent(EventType.MOVED, obj=self)
        self.was_moving = moving_now

    def check_vertical_collision(self, level, new_y):
        old_y = self.y
        self.y = new_y
        collided = False

        for obj in level.objects:
            if obj is self or not obj.CanCollide:
                continue

            if (self.x < obj.x + obj.width and
                self.x + self.width > obj.x and
                self.y < obj.y + obj.height and
                self.y + self.height > obj.y):

                if self.vy > 0:  # en bas
                    self.y = obj.y - self.height
                    self.is_grounded = True
                elif self.vy < 0:  # en haut
                    self.y = obj.y + obj.height

                self.vy = 0
                collided = True
                self.trigger_touch(obj)

        if not collided:
            self.y = new_y

    def check_horizontal_collision(self, level, new_x):
        old_x = self.x
        self.x = new_x
        collided = False

        for obj in level.objects:
            if obj is self or not obj.CanCollide:
                continue

            if (self.x < obj.x + obj.width and
                self.x + self.width > obj.x and
                self.y < obj.y + obj.height and
                self.y + self.height > obj.y):

                if self.vx > 0:
                    self.x = obj.x - self.width
                elif self.vx < 0:
                    self.x = obj.x + obj.width

                self.vx = 0
                collided = True
                self.trigger_touch(obj)

        if not collided:
            self.x = new_x

    def trigger_touch(self, obj):
        if obj not in self.currently_touching:
            self.triggerEvent(EventType.TOUCHED, obj=self, other=obj)
        self.currently_touching.add(obj)
        self.triggerEvent(EventType.TOUCHING, obj=self, other=obj)

    def onCollision(self, other): self.updatePoints()

    def applyTexture(self, texture: 'Texture'):
        self.texture = texture
        self.updatePoints()

    def setColor(self, c):
        if isinstance(c, tuple) and len(c) == 3:
            tex = Texture(self.width, self.height)
            tex.setAllPixelsColor(c)
            self.applyTexture(tex)
        elif hasattr(c, "get") and isinstance(c, Color):
            tex = Texture(self.width, self.height)
            tex.setAllPixelsColor(c.get())
            self.applyTexture(tex)