import numpy as np
try:
    import torch
except Exception:  # pragma: no cover - torch optional
    torch = None


class ColorChangeNode:
    """ComfyUI node to recolor an image to a selected palette color."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "color": (
                    "STRING",
                    {
                        "default": "red",
                        "choices": [
                            "red",
                            "green",
                            "blue",
                            "yellow",
                            "cyan",
                            "magenta",
                            "white",
                            "black",
                        ],
                    },
                ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = "Color"

    def run(self, image, color="red"):
        palette = {
            "red": [1.0, 0.0, 0.0],
            "green": [0.0, 1.0, 0.0],
            "blue": [0.0, 0.0, 1.0],
            "yellow": [1.0, 1.0, 0.0],
            "cyan": [0.0, 1.0, 1.0],
            "magenta": [1.0, 0.0, 1.0],
            "white": [1.0, 1.0, 1.0],
            "black": [0.0, 0.0, 0.0],
        }
        rgb = palette.get(color, palette["red"])

        if torch is not None and isinstance(image, torch.Tensor):
            color_t = image.new_tensor(rgb)
            result = image.clone()
            result[...] = color_t
        else:
            result = np.array(image, copy=True)
            result[...] = np.array(rgb, dtype=np.float32)
        return (result,)


NODE_CLASS_MAPPINGS = {"ColorChangeNode": ColorChangeNode}
NODE_DISPLAY_NAME_MAPPINGS = {"ColorChangeNode": "Color Change Node"}

