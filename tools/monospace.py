# Make your font Monospace!
print "Script by Charles @ https://wonderunit.com/"

# JUST CHANGE THIS VALUE FOR WIDTH:
width = 600
  
import math

# Clear the kerning table, if any
Glyphs.font.kerning = {}

num = 0

for glyph in Glyphs.font.glyphs:
  for layer in glyph.layers:
    glyphWidth = layer.bounds.size.width
    leftSpace = math.floor((width - glyphWidth)/2)
    layer.LSB = leftSpace
    layer.width = width
    num+=1
    
print "Done! {} glyphs were monospaced.".format(num)