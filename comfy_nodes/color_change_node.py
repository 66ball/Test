import numpy as np


class ColorChangeNode:
    """ComfyUI node to fill the entire image with a chosen color."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "red": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                "green": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                "blue": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = "Color"

    def run(self, image, red=1.0, green=0.0, blue=0.0):
        color = np.array([red, green, blue], dtype=image.dtype)
        result = np.zeros_like(image)
        result[...] = color
        return (result,)


NODE_CLASS_MAPPINGS = {"ColorChangeNode": ColorChangeNode}
NODE_DISPLAY_NAME_MAPPINGS = {"ColorChangeNode": "Color Change Node"}

