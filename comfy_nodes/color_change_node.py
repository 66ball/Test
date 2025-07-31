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
        if not isinstance(image, np.ndarray) and hasattr(image, "detach"):
            arr = image.detach().cpu().numpy()
        else:
            arr = np.asarray(image)

        dtype = arr.dtype if isinstance(arr.dtype, np.dtype) else np.float32
        color = np.array([red, green, blue], dtype=dtype)

        result = np.zeros_like(arr)
        result[...] = color
        return (result,)


NODE_CLASS_MAPPINGS = {"ColorChangeNode": ColorChangeNode}
NODE_DISPLAY_NAME_MAPPINGS = {"ColorChangeNode": "Color Change Node"}

