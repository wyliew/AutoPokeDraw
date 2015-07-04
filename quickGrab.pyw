
"""
Auto-drawer for http://pokedraw.net/
All coordinates assume a screen resolution of 1366x768, and Chrome 
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser, and Let's Draw has been clicked.
"""

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
def screengrab():
	refBox = (ref_x_pad + 1,ref_y_pad + 1,ref_x_pad + 425,ref_y_pad + 427)
	refIm = ImageGrab.grab(refBox)

	drawBox = (draw_x_pad + 1,draw_y_pad + 1,draw_x_pad + 425,draw_y_pad + 427)
	drawIm = ImageGrab.grab(drawBox)

	colorsBox = (colors_x_pad + 1,colors_y_pad + 1,colors_x_pad + 365,colors_y_pad + 110)
	colorsIm = ImageGrab.grab(colorsBox)

	test = drawIm.getpixel((550,550))
	print test

def main():
	screengrab()

if __name__ == '__main__':
	main()