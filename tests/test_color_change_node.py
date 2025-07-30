import numpy as np
from comfy_nodes.color_change_node import ColorChangeNode

def test_fill_entire_image():
    node = ColorChangeNode()
    image = np.zeros((2, 2, 3), dtype=np.float32)
    result, = node.run(image, red=0.2, green=0.4, blue=0.6)
    expected = np.zeros_like(image)
    expected[...] = [0.2, 0.4, 0.6]
    assert np.allclose(result, expected)

def test_preserve_shape():
    node = ColorChangeNode()
    image = np.random.rand(3, 4, 3).astype(np.float32)
    result, = node.run(image, red=1.0, green=0.0, blue=0.0)
    assert result.shape == image.shape
