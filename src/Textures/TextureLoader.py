import json
from src.Textures.Texture import Texture

class TextureLoader:
    @staticmethod
    def load_from_file(filepath: str):
        with open(filepath, "r") as f:
            data = json.load(f)
        return TextureLoader.load_from_dict(data)

    @staticmethod
    def load_from_dict(data: dict):
        textures = {}
        for name, tex_data in data.items():
            width = tex_data["width"]
            height = tex_data["height"]
            pixels = tex_data["pixels"]

            tex = Texture(width, height)
            for y in range(height):
                for x in range(width):
                    color = tuple(pixels[y][x])
                    tex.setPixelColor(x, y, color)

            textures[name] = tex
        return textures
