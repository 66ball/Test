# Test

## ColorChangeNode

`ColorChangeNode` fills the entire input image with the specified color.
It accepts either a NumPy array or a PyTorch tensor as input and will
internally convert tensors to NumPy arrays if necessary.

### Parameters

- `image` (`IMAGE`): Input image tensor.
- `red`, `green`, `blue` (`FLOAT`): Components of the color to apply.

### Example

```python
from comfy_nodes.color_change_node import ColorChangeNode
import numpy as np

node = ColorChangeNode()
image = np.zeros((2, 2, 3), dtype=np.float32)
colored, = node.run(image, red=1.0, green=0.0, blue=0.0)
```

## RGBAdjustContrastFeatherNode

`RGBAdjustContrastFeatherNode` scales each color channel of the input image,
adjusts overall contrast, and optionally applies a feathering blur. The node
supports both NumPy arrays and PyTorch tensors as input images and will safely
convert tensors to NumPy arrays when PyTorch is unavailable.

### Parameters

- `image` (`IMAGE`): Input image tensor.
- `red`, `green`, `blue` (`FLOAT`): Multipliers for the color channels.
- `contrast` (`FLOAT`): Contrast factor, where `1.0` means no change.
- `feather` (`INT`): Radius of the box blur used for feathering.

### Example

```python
from comfy_nodes.rgb_adjust_node import RGBAdjustContrastFeatherNode
import numpy as np

node = RGBAdjustContrastFeatherNode()
image = np.zeros((2, 2, 3), dtype=np.float32)
modified, = node.run(image, red=1.5, green=1.0, blue=1.0, contrast=1.2, feather=1)
```
