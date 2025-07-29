# Test

## ColorChangeNode

`ColorChangeNode` recolors pixels in an input image wherever the provided mask is non-zero.

### Parameters

- `image` (`IMAGE`): Input image tensor.
- `mask` (`MASK`): Mask tensor. Pixels with values other than zero will be recolored.
- `red`, `green`, `blue` (`FLOAT`): Components of the color to apply.

### Example

```python
from comfy_nodes.color_change_node import ColorChangeNode
import numpy as np

node = ColorChangeNode()
image = np.zeros((2, 2, 3), dtype=np.float32)
mask = np.array([[1, 0], [0, 0]], dtype=np.float32)
colored, = node.run(image, mask, red=1.0, green=0.0, blue=0.0)
```
