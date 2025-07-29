import numpy as np
import pytest
from comfy_nodes.color_change_node import ColorChangeNode


def test_apply_color_only_in_mask_numpy():
    node = ColorChangeNode()
    image = np.zeros((2, 2, 3), dtype=np.float32)
    mask = np.array([[1, 0], [0, 0]], dtype=np.float32)
    result, = node.run(image, mask, color="blue")
    expected = np.zeros_like(image)
    expected[0, 0] = [0.0, 0.0, 1.0]
    assert np.allclose(result, expected)


def test_apply_color_only_in_mask_torch():
    torch = pytest.importorskip("torch")
    node = ColorChangeNode()
    image = torch.zeros(2, 2, 3)
    mask = torch.tensor([[0, 1], [0, 0]], dtype=image.dtype)
    result, = node.run(image, mask, color="green")
    expected = image.clone()
    expected[0, 1] = torch.tensor([0.0, 1.0, 0.0])
    assert torch.allclose(result, expected)
