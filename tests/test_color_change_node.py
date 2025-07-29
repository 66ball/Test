import numpy as np
from comfy_nodes.color_change_node import ColorChangeNode

def test_apply_color_only_in_mask():
    node = ColorChangeNode()
    image = np.zeros((2, 2, 3), dtype=np.float32)
    mask = np.array([[1, 0], [0, 0]], dtype=np.float32)
    result, = node.run(image, mask, red=0.2, green=0.4, blue=0.6)
    expected = np.zeros_like(image)
    expected[0, 0] = [0.2, 0.4, 0.6]
    assert np.allclose(result, expected)

def test_mask_dimension_handling():
    node = ColorChangeNode()
    image = np.zeros((1, 1, 3), dtype=np.float32)
    mask = np.array([[[1.0]]], dtype=np.float32)
    result, = node.run(image, mask, red=0.3, green=0.3, blue=0.3)
    assert np.allclose(result[0, 0], [0.3, 0.3, 0.3])
