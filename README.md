# Test

## ColorChangeNode

`ColorChangeNode` recolors pixels in an input image wherever the provided mask is non-zero using a color selected from a small palette.

### Parameters

- `image` (`IMAGE`): Input image tensor.
- `mask` (`MASK`): Mask tensor. Pixels with values other than zero will be recolored.
- `color` (`STRING`): Name of the color to apply. One of `red`, `green`, `blue`, `yellow`, `cyan`, `magenta`, `white`, or `black`.

### Example

```python
from comfy_nodes.color_change_node import ColorChangeNode
import numpy as np

node = ColorChangeNode()
image = np.zeros((2, 2, 3), dtype=np.float32)
mask = np.array([[1, 0], [0, 0]], dtype=np.float32)
colored, = node.run(image, mask, color="green")
```
