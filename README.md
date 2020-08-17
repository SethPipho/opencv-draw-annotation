# opencv-draw-annotation

A library for formatting and drawing annotations (e.g. bounding boxes) on images using opencv

```
pip install opencv-draw-annotation
```

```python

import cv2
from opencv_draw_annotation import draw_bounding_box

image = cv2.imread('./demo.jpg')

box = (105,145,575, 755)#xmin,ymin,xmax,ymax
draw_bounding_box(image, box, labels=["Cat", "Felis Catus"], color='blue')


cv2.imwrite('./demo-output.jpg', image)
```

![demo-output](https://sethpipho.github.io/opencv-draw-annotation/test/demo-output.jpg)