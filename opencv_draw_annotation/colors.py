def hex_to_BGR(x):
    return (int(x[5:7], base=16), int(x[3:5], base=16), int(x[1:3], base=16))

def is_hex(x):
    return x[0] == "#" and len(x) == 7



colors_str_to_hex = {
    'red'   : '#e74c3c',
    'orange': '#e67e22',
    'yellow': '#f1c40f',
    'green' : '#2ecc71',
    'blue-green' : '#1abc9c',
    'blue'  : '#3498db',
    'purple': '#9b59b6',
    'black' : '#2c3e50',
    'white' : '#ecf0f1'
}

colors_str_to_BGR = {k:hex_to_BGR(v) for k,v in colors_str_to_hex.items()}


def convert_color(x):
    if is_hex(x):
        color = hex_to_BGR(x)
    elif x in colors_str_to_BGR.keys():
        color = colors_str_to_BGR[x]
    else:
        raise ValueError('Invalid color: color string must be a hex code or one of ' + str(list(colors_str_to_BGR.keys())))

    return color
