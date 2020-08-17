import numpy as np
import cv2
from opencv_draw_annotation import draw_bounding_box


image = np.zeros((1000,1000,3), np.uint8)
image.fill(255)

draw_bounding_box(image, (100,100,200,200), labels=['Test','This is a label'])

draw_bounding_box(image, (100,300,200,400), labels=['Larger Font Size'], font_scale=.75)

draw_bounding_box(image, (100,500,200,600), labels=['More Padding', 'text_padding = 10'], text_padding=10)

draw_bounding_box(image, (100,700,200,800), labels=['border_thickness = 5'], border_thickness=5 )


draw_bounding_box(image, (400,10,500,100), labels=['Auto label position'] )

cv2.imwrite('test-output.png', image)
