import cv2

def hex_to_BGR(x):
    return (int(x[5:7], base=16), int(x[3:5], base=16), int(x[1:3], base=16))

def draw_bounding_box(frame, 
                      box, 
                      labels=[], 
                      color=(60, 76, 231), 
                      font_face = cv2.FONT_HERSHEY_DUPLEX, 
                      font_scale = .5, 
                      font_weight = 1,
                      font_color = (255,255,255),
                      text_padding = 3,
                      border_thickness = 2
                      ):

    xmin,ymin,xmax,ymax = box
    xmin,ymin,xmax,ymax = int(xmin),int(ymin),int(xmax), int(ymax)
     
    frame = cv2.rectangle(frame, (xmin,ymin), (xmax, ymax), color, border_thickness)

    text_dims = [cv2.getTextSize(x, font_face, font_scale, font_weight) for x in labels]
    total_label_height = sum([x[0][1] for x in text_dims]) + sum([x[1] for x in text_dims])  + (text_padding * len(labels) * 2) 
  
    border_offset = (border_thickness // 2) if border_thickness % 2 == 0 else (border_thickness // 2) + 1

    label_xmin = xmin - border_offset
    label_ymin = ymin - total_label_height - border_offset
    for i,label in enumerate(labels):

        text_width = text_dims[i][0][0]
        text_height = text_dims[i][0][1]
        text_baseline = text_dims[i][1]
        label_height = text_dims[i][0][1] + text_dims[i][1] + text_padding * 2

        label_xmax = label_xmin + text_width + text_padding * 2
        label_ymax = label_ymin + label_height

        cv2.rectangle(frame, (label_xmin, label_ymin), (label_xmax, label_ymax), color, -1)
        cv2.putText(frame, label,(label_xmin + text_padding, label_ymin + text_height + text_baseline), font_face, font_scale,(255,255,255), font_weight, cv2.LINE_AA)
        
        label_ymin = label_ymax
        
       


    #cv2.rectangle(frame, (xmin - (border_thickness//2),ymin - baseline - text_height - text_padding * 2 - border_thickness // 2), (xmin + text_width + text_padding * 2, ymin), color, -1)
    #cv2.putText(frame, labels[0],(xmin - border_thickness + text_padding ,ymin - baseline - text_padding ), font_face, font_scale,(255,255,255), font_weight, cv2.LINE_AA)