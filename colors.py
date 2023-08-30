from PIL import Image
import requests
from io import BytesIO
import webcolors
import pandas as pd
import webcolors
  
def closest_colour(requested_colour):
    """
    closest_colour takes a requested color in the form of an RGB tuple and 
    returns the closest CSS3 color name based on the Euclidean distance between 
    the RGB components of the requested color and the predefined CSS3 colors.
    """
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def top_colors(url, n=10):
    """
    top_colors takes a URL and an optional parameter n (default value is 10) which specifies the number of top colors to return.
    """
    # read images from URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    # convert the image to rgb
    image = img.convert('RGB')
     
    # resize the image to 100 x 100
    image = image.resize((100,100))
     
    detected_colors =[]
    for x in range(image.width):
        for y in range(image.height):
            detected_colors.append(closest_colour(image.getpixel((x,y))))
    Series_Colors = pd.Series(detected_colors)
    output=Series_Colors.value_counts()/len(Series_Colors)
    return(output.head(n).to_dict())