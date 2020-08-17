import cv2
from opencv_draw_annotation import draw_bounding_box


image = cv2.imread('./demo.jpg')

box = (50,75,285,380)#xmin,ymin,xmax,ymax
draw_bounding_box(image, box, labels=["Cat", "Felis Catus"], color='blue')


cv2.imwrite('./demo-output.jpg', image)