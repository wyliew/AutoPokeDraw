"""
Auto-drawer for http://pokedraw.net/
All coordinates assume a screen resolution of 1366x768, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser, and Let's Draw has been clicked.
"""
import math
import win32api, win32con, win32gui
import ImageGrab
import os
import time

# Globals
# ------------------
ref_x_pad = 148
ref_y_pad = 111
draw_x_pad = 774
draw_y_pad = 111
colors_x_pad=  804
colors_y_pad = 548
color_coords = [(829,571), (891,571), (955,571), (1017,571), (1079,571), (1145,571),
				(829,629), (891,629), (955,629), (1017,629), (1079,629), (1145,629)]
color_rgb = [(244,42,53), (255,162,0), (255,213,0), (168,191,18), (46,181,47), (0,170,181), 
			(50,90,197), (250,208,222), (148,109,155), (135,94,55), (142,150,155), (0,0,0)]
pixelMap = {}

def mousePos(cord):
    win32api.SetCursorPos(cord)

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(.02)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def get_cords():
	x,y = win32api.GetCursorPos()
	return (x, y)

def grabRef():
	refBox = (ref_x_pad + 1,ref_y_pad + 1,ref_x_pad + 425,ref_y_pad + 427)
	return ImageGrab.grab(refBox)

def grabDraw():
	drawBox = (draw_x_pad + 1,draw_y_pad + 1,draw_x_pad + 425,draw_y_pad + 427)
	return ImageGrab.grab(drawBox)

def grabColors():
	colorsBox = (colors_x_pad + 1,colors_y_pad + 1,colors_x_pad + 365,colors_y_pad + 110)
	return ImageGrab.grab(colorsBox)

#Returns closest index actually
def getClosestPixel(pixel):
	if pixel in pixelMap:
		return pixelMap[pixel]
	else:
		red = pixel[0]
		green = pixel[1]
		blue = pixel[2]
		
		closestPixel = color_rgb[0]
		closestIndex = 0
		diff = math.fabs(closestPixel[0] - red) + math.fabs(closestPixel[1] - green) + math.fabs(closestPixel[2] - blue)
		for index, pix in enumerate(color_rgb):
			tempDiff = math.fabs(pix[0] - red) + math.fabs(pix[1] - green) + math.fabs(pix[2] - blue)
			if (tempDiff <= diff):
				diff = tempDiff
				closestPixel = pix
				closestIndex = index
		pixelMap[pixel] = closestIndex
		return closestIndex

def main():
	ref = grabRef()	
	colors = grabColors()	
	draw = grabDraw()
	startTime = time.time()
	for x in range (0, ref.size[0], 8):
		for y in range (0, ref.size[1], 8):
			refPixel = ref.getpixel((x,y))
			if refPixel != (255,255,255):
				closestPixel = getClosestPixel(refPixel)
				coord = color_coords[closestPixel]
				mousePos(coord)
				leftClick()
				mousePos((draw_x_pad + x, draw_y_pad + y ) )
				leftClick()
	endTime = time.time()
	print 'It took ' + str(endTime - startTime) + ' seconds'


main()