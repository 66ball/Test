import numpy as np
from comfy_nodes.rgb_adjust_node import RGBAdjustContrastFeatherNode

def test_color_and_contrast():
    node = RGBAdjustContrastFeatherNode()
    image = np.ones((1, 1, 3), dtype=np.float32) * 0.5
    result, = node.run(image, red=2.0, green=0.5, blue=1.0, contrast=1.0, feather=0)
    expected = np.array([[[1.0, 0.25, 0.5]]], dtype=np.float32)
    assert np.allclose(result, expected)

def test_feather_blur():
    node = RGBAdjustContrastFeatherNode()
    image = np.zeros((3, 3, 3), dtype=np.float32)
    image[1,1] = [1.0, 1.0, 1.0]
    result, = node.run(image, feather=1)
    center = result[1,1,0]
    assert center < 1.0 and center > 0.0
