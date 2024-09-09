diamSmall = 10;
diamLarge = 3 * diamSmall;


def setup() :
    fullScreen()
 
def draw():
    background(255, 215, 0)
    stroke(0)
    fill(0)
     
    for x in range (0, width, 5 * diamSmall): 
        for y in range (0, height, 5 * diamSmall):
            ellipse(x, y, diamSmall, diamSmall)
        
    
    translate(5 * diamSmall, 5 * diamSmall)
        
    for x in range (0, width, 2 * 5 * diamSmall):
        for y in range (0, height, 2 * 5 * diamSmall):
            ellipse(x, y, diamLarge, diamLarge)
 
