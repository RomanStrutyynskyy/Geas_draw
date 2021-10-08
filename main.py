import fmod
import math
import random
 
class Gear:

    def __init__(self, m, z):
        self.ngear = 0
        self.cx = 250
        self.cy = 250
        self.m = m # module
        self.z = z # nteeth
        self.d = self.m * self.z
        self.da = self.m * (self.z+2)
        self.df = self.m * (self.z-2.5)
        self.r, self.ra, self.rf = self.d/2, self.da/2, self.df/2
        self.stepa = 360/self.z
                            
    def draw_teeth(self):
        a = ''
        ai = ''
        evolute = []
        #forming Involute points data
        for i in range (0, 361):
            t=math.radians (i)
            x=self.rf*(math.cos(t)+t*math.sin(t))+self.cx
            y=self.rf*(math.sin(t)-t*math.cos(t))+self.cy
            y1=self.cy-(y-self.cy)
            evolute.append ((x,y,y1))
            dist=math.hypot(self.cx-x,  self.cy-y)
            if dist > self.ra:
                break
        #draving oll teeth via rotation transform
        for i in range (1, self.z+1):
            alf = math.radians(self.stepa*i)
            cr = -math.radians(self.stepa*0.37)#correction angle
            for n in range (0, len(evolute)):
                x = self.cx+(evolute[n][0]-self.cx)*math.cos(alf+cr)-(evolute[n][1]-self.cy)*math.sin(alf+cr)
                y = self.cy+(evolute[n][1]-self.cy)*math.cos(alf+cr)+(evolute[n][0]-self.cx)*math.sin(alf+cr)
                a += str(x) + ',' + str(y) + ' '
            for n in range (len(evolute)-1,-1,-1):
                x = self.cx+(evolute[n][0]-self.cx)*math.cos(alf-cr)-(evolute[n][2]-self.cy)*math.sin(alf-cr)
                y = self.cy+(evolute[n][2]-self.cy)*math.cos(alf-cr)+(evolute[n][0]-self.cx)*math.sin(alf-cr)
                a += str(x) + ',' + str(y) + ' '
        fmod.draw('polygon', a, '000000', 1)# draw teeth
        fmod.draw_complex(self)# draw cirkles
        fmod.txt(self.cx, self.cy, self.ngear)
        
        
            
            
        
    
#/////////////////////////////////////////////////////////////////
fmod.start()


g = []
m = 3.5
z = 20
ngears = 8
aaa =80 #+/- angle
#----------------
for i in range (0,ngears):
    g.append(i)
    g[i] = Gear(m, random.randint(18,46))
    g[i].cx, g[i].cy, g[i].ngear = 150, 250, i
    
a = ''
for i in range (0,ngears-1):
    fi = math.radians(random.randint(-aaa,aaa))
    g[i+1].cx = (g[i].r+g[i+1].r) * math.cos(fi) + g[i].cx
    g[i+1].cy = (g[i].r+g[i+1].r) * math.sin(fi) + g[i].cy
    azymuth =-math.atan2(g[i].cx-g[i+1].cx, g[i].cy-g[i+1].cy)
    az = round (math.degrees(azymuth), 2)
    ast = str(i) + ' - ' + str(i+1)
    
    
for i in range (0, ngears):
    a += str(g[i].cx) + ',' + str(g[i].cy) + ' '
    g[i].draw_teeth()
fmod.draw('polyline', a, 'ff22aa', 0.5)

 




                                 
    
    


#/*/*/*/*/*/*/*/*/*/*/*/*/*/*
fmod.eend()

    
