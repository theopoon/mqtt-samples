#!/usr/bin/python
import time
from sense_hat import SenseHat

sense = SenseHat()

black = [0,0,0]
grey = [53,63,56]


pixels = [
[0,0,0],[53,63,56],[53,63,56],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[53,63,56],
[0,0,0],[0,0,0],[255,229,30],[254,152,2],[0,0,0],[0,0,0],[0,0,0],[255,229,30],
[0,0,0],[0,0,0],[0,0,0],[255,229,30],[255,229,30],[255,229,30],[255,229,30],[254,152,2],
[254,152,2],[254,152,2],[0,0,0],[255,229,30],[0,0,0],[255,229,30],[255,229,30],[0,0,0],
[254,152,2],[254,152,2],[0,0,0],[255,1,66],[255,229,30],[255,229,30],[255,229,30],[254,152,2],
[0,0,0],[165,74,44],[0,0,0],[255,229,30],[254,152,2],[254,152,2],[254,152,2],[0,0,0],
[0,0,0],[165,74,44],[255,229,30],[254,152,2],[255,229,30],[254,152,2],[255,229,30],[0,0,0],
[0,0,0],[0,0,0],[255,229,30],[254,152,2],[165,74,44],[165,74,44],[254,152,2],[0,0,0]
]


#print len(pixels)

sense.set_pixels(pixels)

print "Pika!"
