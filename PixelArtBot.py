from math import sqrt
import pyautogui
import time
from PIL import Image
from subprocess import call


COLORS = (
    (95, 0, 12),
    (183, 0, 41),
    (255, 53, 0),
    (255, 159, 0),
    (255, 209, 37),
    (255, 247, 176),
    (0, 153, 90),
    (0, 198, 107),
    (113, 235, 71),
    (0, 104, 97),
    (0, 148, 161),
    (0, 198, 185),
    (20, 65, 154),
    (38, 132, 231),
    (66, 230, 243),
    (58, 42, 186),
    (92, 77, 255),
    (137, 171, 255),
    (116, 15, 149),
    (172, 59, 185),
    (255, 162, 255),
    (218, 6, 144),
    (255, 40, 116),
    (255, 142, 161),
    (95, 57, 31),
    (146, 91, 22),
    (255, 172, 98),

    (0, 0, 0),
    (66, 67, 67), 
    (125, 129, 132),
    (207, 210, 213),
    (255, 255, 255),
)


def get_closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


def color_to_pos(rgb):
    if rgb == (95, 0, 12):
        return (40, 880)
    elif rgb == (183, 0, 41):
        return (100, 880)
    elif rgb == (255, 53, 0):
        return (160, 880)
    elif rgb == (255, 159, 0):
        return (220, 880)
    elif rgb == (255, 209, 37):
        return (280, 880)
    elif rgb == (255, 247, 176):
        return (340, 880)
    elif rgb == (0, 153, 90):
        return (400, 880)
    elif rgb == (0, 198, 107):
        return (460, 880)
    elif rgb == (113, 235, 71):
        return (520, 880)
    elif rgb == (0, 104, 97):
        return (580, 880)
    elif rgb == (0, 148, 161):
        return (640, 880)
    elif rgb == (0, 198, 185):
        return (700, 880)
    elif rgb == (20, 65, 154):
        return (760, 880)
    elif rgb == (38, 132, 231):
        return (820, 880)
    elif rgb == (66, 230, 243):
        return (880, 880)
    elif rgb == (58, 42, 186):
        return (940, 880)
    elif rgb == (92, 77, 255):
        return (1000, 880)
    elif rgb == (137, 171, 255):
        return (1060, 880)
    elif rgb == (116, 15, 149):
        return (1120, 880)
    elif rgb == (172, 59, 185):
        return (1180, 880)
    elif rgb == (255, 162, 255):
        return (1240, 880)
    elif rgb == (218, 6, 144):
        return (1300, 880)
    elif rgb == (255, 40, 116):
        return (1360, 880)
    elif rgb == (255, 142, 161):
        return (1420, 880)
    elif rgb == (95, 57, 31):
        return (1480, 880)
    elif rgb == (146, 91, 22):
        return (1540, 880)
    elif rgb == (255, 172, 98):
        return (1600, 880)

    elif rgb == (0, 0, 0):
        return (1640, 880)
    elif rgb == (66, 67, 67):
        return (1690, 880)
    elif rgb == (125, 129, 132):
        return (1750, 880)
    elif rgb == (207, 210, 213):
        return (1820, 880)
    elif rgb == (255, 255, 255):
        return (1870, 880)


north = (950, 450)
east = (1050, 550)
south = (950, 640)
west = (880, 550)

place = (960, 930)
confirm = (1050, 937)

#filename = input("Enter File Name : ")
filename = "Rainbow.png"
img = Image.open(filename)
pixels = img.load()
wid, hgt = img.size
wid -= 1
hgt -= 1
xpos = 0
ypos = 18
direction = east

time.sleep(2)

while True:
    pixcolor = pixels[xpos, ypos]

    rgbcolor = (pixcolor[0], pixcolor[1], pixcolor[2])
    color = closest_color(rgbcolor)
    pos = color_to_pos(color)

    call(["screencapture", "-R 0,540,1920,1", "screenshot.png"])
    time.sleep(0.2)
    img2 = Image.open("screenshot.png")
    pixels2 = img2.load()
    pixcolor2 = pixels2[direction[0],0]

    rgbcolor2 = (pixcolor2[0], pixcolor2[1], pixcolor2[2])

    if color == rgbcolor2 and xpos != wid and xpos != 0:
        time.sleep(0.1)
    else:
        pyautogui.click(place[0], place[1])
        time.sleep(0.4)
        pyautogui.click(pos[0], pos[1])
        time.sleep(0.05)
        pyautogui.click(confirm[0], confirm[1])

        time.sleep(0.9)

    if ypos % 2 == 0:
        if xpos == wid:
            ypos += 1
            direction = south
        else:
            xpos += 1
            direction = east
    else:
        if xpos == 0:
            ypos += 1
            direction = south
        else:
            xpos -= 1
            direction = west

    pyautogui.click(direction[0], direction[1])

    

    

