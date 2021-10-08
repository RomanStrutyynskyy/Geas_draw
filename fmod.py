import math
import random
  
def start():
    #fi = open ('1.txt' , 'r')
    fo = open('2.svg','w')
    start_text = """<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<svg version = "1.1"
     baseProfile="full"
     xmlns = "http://www.w3.org/2000/svg" 
     xmlns:xlink = "http://www.w3.org/1999/xlink"
     xmlns:ev = "http://www.w3.org/2001/xml-events"
     height = "1500px"  width = "1500px">
    
     <g>"""
    fo.write(start_text + '\n')
    fo.close()
def draw(typ, points, color, thickness):
    fo = open('2.svg','a')
    lexem1 = '\n\n'
    lexem2 = '<{0} stroke="#{1}" '.format(typ, color)
    lexem3 = 'stroke-width="{0}px" '.format(str(thickness))
    lexem4 = 'fill="none" points="{0}" />'.format(points)
    fo.write(lexem1 + lexem2 + lexem3 + lexem4)
    fo.close()

def crkl(x,y,r):
    a1  =random.randint(16,250)
    a2 = random.randint(16,250)
    a3  =random.randint(16,250)
    z1 = str(format(a1, 'x'))
    z2 = str(format(a2, 'x'))
    z3 = str(format(a3, 'x'))
    fo = open('2.svg','a')
    lex = '<circle cx="{0}" cy="{1}" r="{2}" fill="#{3}{4}{5}"/>'.format(x,y,r,z1,z2,z3)

    fo.write(lex)
    fo.close()
    
def eend():
    fo = open('2.svg','a')
    fo.write('\n\n'+ '</g>' + '\n'+ '</svg>')
    fo.close()


def draw_gear(cx, cy, d, typ, color, thickness):
    points = ''
    for i in range(0, 361):
        x = d*math.cos(math.radians(i)) + cx
        y = d*math.sin(math.radians(i)) + cy
        points += (str (round(x, 2)) + ',' + str (round(y, 2)) + ' ')
    draw(typ, points, color, thickness)
    
def draw_complex(a):
    color = ('ff1100','00ff11','00ffaa')
    r = (a.r, a.ra, a.rf)
    t = (0.6, 0.4, 0.4)
    for n in range (0,3):
        points = ''
        for i in range(0, 361):
            x = r[n]*math.cos(math.radians(i)) + a.cx
            y = r[n]*math.sin(math.radians(i)) + a.cy
            points += (str (round(x, 2)) + ',' + str (round(y, 2)) + ' ')
        draw('polyline', points, color[n], t[n])
    points = (str(a.cx) + ',' + str(a.cy) + ' ' +str(a.cx) + ',' + str(a.cy-a.ra))
    draw('polyline', points, 'ddaa00', 0.9)

def txt(x,y,a):
    x, y, a = str(x), str(y), str(a)
    fo = open('2.svg','a')
    fo.write('<text x="'+x +'" y="'+y+'" font-family="Arial">'+a+'</text>')
    fo.close()

    #GOST_type_А_Italic
    
    
    
    
    


