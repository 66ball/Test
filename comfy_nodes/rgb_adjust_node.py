import numpy as np

class RGBAdjustContrastFeatherNode:
    """ComfyUI node to adjust color, contrast, and apply feathering."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "red": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.01}),
                "green": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.01}),
                "blue": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 2.0, "step": 0.01}),
                "contrast": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 3.0, "step": 0.01}),
                "feather": ("INT", {"default": 0, "min": 0, "max": 10}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run"
    CATEGORY = "Color"

    def _box_blur(self, image, radius):
        if radius <= 0:
            return image
        k = 2 * radius + 1
        pad = radius
        padded = np.pad(image, ((pad, pad), (pad, pad), (0, 0)), mode="edge")
        out = np.zeros_like(image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                region = padded[i:i + k, j:j + k]
                out[i, j] = region.mean(axis=(0, 1))
        return out

    def run(self, image, red=1.0, green=1.0, blue=1.0, contrast=1.0, feather=0):
        color = np.array([red, green, blue], dtype=image.dtype)
        result = image * color
        result = (result - 0.5) * contrast + 0.5
        result = np.clip(result, 0.0, 1.0)
        result = self._box_blur(result, int(feather))
        return (result,)


NODE_CLASS_MAPPINGS = {"RGBAdjustContrastFeatherNode": RGBAdjustContrastFeatherNode}
NODE_DISPLAY_NAME_MAPPINGS = {"RGBAdjustContrastFeatherNode": "RGB Adjust Contrast Feather Node"}
