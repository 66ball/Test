# Test

## ColorChangeNode

`ColorChangeNode` recolors an entire image using a color from a small palette.

### Parameters

- `image` (`IMAGE`): Input image tensor.
- `color` (`STRING`): Name of the color to apply. One of `red`, `green`, `blue`, `yellow`, `cyan`, `magenta`, `white`, or `black`.

### Example

```python
from comfy_nodes.color_change_node import ColorChangeNode
import numpy as np

node = ColorChangeNode()
image = np.zeros((2, 2, 3), dtype=np.float32)
colored, = node.run(image, color="green")
```
