import cv2
from .colors import convert_color


def draw_bounding_box(frame, 
                      box, 
                      labels=[], 
                      color='red', 
                      font_face = cv2.FONT_HERSHEY_DUPLEX, 
                      font_scale = .5, 
                      font_weight = 1,
                      font_color = 'white',
                      text_padding = 3,
                      border_thickness = 2
                      ):

       
    color = convert_color(color)
    font_color = convert_color(font_color)

    box = [int(x) for x in box]
    xmin,ymin,xmax,ymax = box
    
    #draw bounding box
    frame = cv2.rectangle(frame, (xmin,ymin), (xmax, ymax), color, border_thickness)

    text_dims = [cv2.getTextSize(x, font_face, font_scale, font_weight) for x in labels]
    total_label_height = sum([x[0][1] for x in text_dims]) + sum([x[1] for x in text_dims])  + (text_padding * len(labels) * 2) 
  
    border_offset = (border_thickness // 2) if border_thickness % 2 == 0 else (border_thickness // 2) + 1

    label_xmin = xmin - border_offset
    label_ymin = ymin - total_label_height - border_offset
    if label_ymin < 0:
        label_ymin = ymax + border_offset


    for i,label in enumerate(labels):

        text_width = text_dims[i][0][0]
        text_height = text_dims[i][0][1]
        text_baseline = text_dims[i][1]
        label_height = text_dims[i][0][1] + text_dims[i][1] + text_padding * 2

        label_xmax = label_xmin + text_width + text_padding * 2
        label_ymax = label_ymin + label_height

        cv2.rectangle(frame, (label_xmin, label_ymin), (label_xmax, label_ymax), color, -1)
        cv2.putText(frame, label,(label_xmin + text_padding, label_ymin + text_height + text_padding), font_face, font_scale,(255,255,255), font_weight, cv2.LINE_AA)
        
        label_ymin = label_ymax
        
       