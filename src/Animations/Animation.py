class Animation:
    def __init__(self, loop=True):
        self.keyframes = []
        self.loop = loop
        self.running = False
        self.current_time = 0.0
        self.duration = 0.0
        self.last_keyframe_index = -1
        self.original_positions = {}

    def add_keyframe(self, keyframe):
        self.keyframes.append(keyframe)
        self.keyframes.sort(key=lambda k: k.time_offset)
        self.duration = max(self.duration, keyframe.time_offset)

    def start(self):
        self.running = True
        self.current_time = 0.0
        self.last_keyframe_index = -1

        # Only store original positions for keyframes that don't apply delta-movement (dx/dy),
        # or remove this section entirely since texture keyframes don't need it.
        # Since your player parts rely on the root for movement, we will rely on Player.sync_parts
        # to handle positioning and keep the animation clean.
        self.original_positions = {} # Keep this empty to stop recording absolute start positions.

        if self.keyframes:
            self.keyframes[0].apply()
            self.last_keyframe_index = 0

    def stop(self):
        self.running = False
        # FIX: When stopping, remove any temporary position change applied by the last keyframe.
        # This is a good practice, but not strictly required if 'idle' animation resets to dy=0.
        # Your 'idle' animation already sets dy=0 in its first keyframe (at 0.0).

    def update(self, delta):
        if not self.running or not self.keyframes:
            return

        self.current_time += delta

        if self.current_time >= self.duration:
            if self.loop and self.duration > 0:
                # FIX: When looping, do NOT reset position to a stored 'original_position'.
                # The root object is responsible for the part's base position.
                self.current_time %= self.duration
                self.last_keyframe_index = -1
            else:
                self.running = False
                self.keyframes[-1].apply()
                return

        start_index = self.last_keyframe_index + 1 if self.last_keyframe_index != -1 else 0
        for i in range(start_index, len(self.keyframes)):
            kf = self.keyframes[i]
            if kf.time_offset <= self.current_time:
                kf.apply()
                self.last_keyframe_index = i
            else:
                break
                