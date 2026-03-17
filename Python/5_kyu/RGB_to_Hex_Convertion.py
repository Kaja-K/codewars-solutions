"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal 
representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range 
must be rounded to the closest valid value.

    255, 255, 255 --> "FFFFFF"
    255, 255, 300 --> "FFFFFF"
    0, 0, 0       --> "000000"
    148, 0, 211   --> "9400D3"

"""


def col(rgb):
    if rgb > 255:
        rgb = 255
    elif rgb < 0:
        rgb = 0
    return rgb


def rgb(r, g, b):
    return "{:02x}{:02x}{:02x}".format(col(r), col(g), col(b)).upper()
