import numpy as np

try:
    import torch
    import torch.nn.functional as F
except Exception:  # pragma: no cover - torch may not be available during tests
    torch = None
    F = None

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

    def _box_blur_torch(self, image, radius):  # pragma: no cover - torch unavailable in tests
        if radius <= 0:
            return image
        k = 2 * radius + 1
        pad = radius
        weight = torch.ones((image.shape[2], 1, k, k), device=image.device, dtype=image.dtype) / (k * k)
        img = image.permute(2, 0, 1).unsqueeze(0)
        blurred = F.conv2d(F.pad(img, (pad, pad, pad, pad), mode="replicate"), weight, groups=image.shape[2])
        return blurred.squeeze(0).permute(1, 2, 0)

    def run(self, image, red=1.0, green=1.0, blue=1.0, contrast=1.0, feather=0):
        if torch is not None and isinstance(image, torch.Tensor):  # pragma: no cover - torch not in CI
            color = torch.tensor([red, green, blue], dtype=image.dtype, device=image.device)
            result = image * color
            result = (result - 0.5) * contrast + 0.5
            result = torch.clamp(result, 0.0, 1.0)
            result = self._box_blur_torch(result, int(feather))
            return (result,)
        else:
            arr = np.asarray(image)
            color = np.array([red, green, blue], dtype=arr.dtype)
            result = arr * color
            result = (result - 0.5) * contrast + 0.5
            result = np.clip(result, 0.0, 1.0)
            result = self._box_blur(result, int(feather))
            return (result,)


NODE_CLASS_MAPPINGS = {"RGBAdjustContrastFeatherNode": RGBAdjustContrastFeatherNode}
NODE_DISPLAY_NAME_MAPPINGS = {"RGBAdjustContrastFeatherNode": "RGB Adjust Contrast Feather Node"}
