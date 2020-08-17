# opencv-draw-annotation

A library for formatting and drawing annotations (e.g. bounding boxes) on images using opencv


## Install
```
pip install opencv-draw-annotation
```

## Basic Usage
```python
#test/demo.py

import cv2
from opencv_draw_annotation import draw_bounding_box

image = cv2.imread('./demo.jpg')

box = (105,145,575, 755)#xmin,ymin,xmax,ymax
draw_bounding_box(image, box, labels=["Cat", "Felis Catus"], color='blue')

cv2.imwrite('./demo-output.jpg', image)
```

![demo-output](https://sethpipho.github.io/opencv-draw-annotation/test/demo-output.jpg)


## Docs

```python
def draw_bounding_box(image, 
                      box, #xmin,ymin,xmax,ymax
                      labels=[], 
                      color='red', 
                      font_face = cv2.FONT_HERSHEY_DUPLEX, 
                      font_size = .5, 
                      font_weight = 1,
                      font_color = 'white',
                      text_padding = 3,
                      border_thickness = 2
                      ):
```

### Colors

Color parameters (color, font_color) are strings and must be a valid hex color code (e.g. **'#eb4034'**) or one of the built in color names: **'red', 'orange', 'yellow', 'green', 'blue-green', 'blue' 'purple', 'black' 'white'**. 