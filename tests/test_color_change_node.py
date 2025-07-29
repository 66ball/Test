import numpy as np
import pytest
from comfy_nodes.color_change_node import ColorChangeNode


def test_colorize_numpy_image():
    node = ColorChangeNode()
    image = np.zeros((1, 1, 3), dtype=np.float32)
    result, = node.run(image, color="red")
    expected = np.array([[[1.0, 0.0, 0.0]]], dtype=np.float32)
    assert np.allclose(result, expected)


def test_colorize_torch_image():
    torch = pytest.importorskip("torch")
    node = ColorChangeNode()
    image = torch.zeros(1, 1, 3)
    result, = node.run(image, color="blue")
    expected = torch.tensor([[[0.0, 0.0, 1.0]]], dtype=image.dtype)
    assert torch.allclose(result, expected)
