# Minecraft JSON gradient generator. If you use this script in any of your personal projects, please credit me and link the repository.
# Script by Bash Elliott.

import numpy as np

# Hex to RGB and RGB to Hex functions by Sachin Rastogi. 
# https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
def hextorgb(hex):
    hex = hex.lstrip('#')
    return(tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)))

def rgbtohex(rgb):
    return '%02x%02x%02x' % rgb

def split(word):
    return list(word)

# Initialize decorator variables.
bold = False
underline = False
italics = False

# Gets text and colors as hex code. Can only accept two colors.
text = list(input("Text: "))
ColorA = hextorgb(input("Color A: "))
ColorB = hextorgb(input("Color B: "))

# Sets decorator variables. If any of these return ANYTHING other than "true", it assumes they're false.
if input("Bold?: ") == "true":
    bold = True
if input("Underline?: ") == "true":
    underline = True
if input("Italics?: ") == "true":
    italics = True

# Sets the number of RGB values to make in the following array.
numPoints = len(text)

# Creates am array of equally spaced RGB values between ColorA and ColorB inclusive.
points = np.linspace(ColorA, ColorB, numPoints, dtype=int)

# Initializes array:hexes, then sets the array to array:points, ~hexified~.
hexes = []
for i in range(len(points)):
    hexes.append((rgbtohex(tuple(points[i]))))

# This mess generates the final text.
final = '["",'
for i in range(len(hexes)):
    doBold = ""
    doUnderline = ""
    doItalics = ""
    
    # Sets the strings to be used if the user sets their respective decorator variables to be true.
    if bold == True:
        doBold = '"bold":true,'
    else:
        doBold = ""

    if italics == True:
        doItalics = '"italic":true,'
    else:
        doItalics = ""

    if underline == True:
        doUnderline = '"underlined":true,'
    else:
        doUnderline = ""

    # The main beast. Generates an individual json item for each character in string:text then slaps it onto the end of the final string.
    final = final + '{{"text":"{}",{}{}{}"color":"#{}"}}'.format(text[i], doBold, doItalics, doUnderline, hexes[i])
    # If this is the last character, don't add a comma. Otherwise, do!
    if i != len(hexes) - 1:
        final = final + ','
# Finish off the json string.
final = final + ']'

# Print it out for the user to copy and use as fit.
print(final)