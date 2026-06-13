import random as rn
import config
import render
def GenerateStars(canvas, stars_remaining):
    if stars_remaining <= 0:
        return
    x= rn.randrange(-config.universeDiameterLightSeconds,config.universeDiameterLightSeconds)
    y= rn.randrange(-config.universeDiameterLightSeconds,config.universeDiameterLightSeconds)
    render.paint(canvas,x,y,"#FFFFFF")
    print(x,y)
    canvas.after(0, lambda: GenerateStars(canvas, stars_remaining-1))