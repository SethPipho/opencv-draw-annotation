import cv2
from opencv_draw_annotation import draw_bounding_box, hex_to_BGR


image = cv2.imread('./test.jpg')

box = (105,145,575, 755)#xmin,ymin,xmax,ymax
draw_bounding_box(image, box, labels=["Cat", "Felis Catus"], color=hex_to_BGR('#9b59b6'))


cv2.imwrite('test-output.jpg', image)