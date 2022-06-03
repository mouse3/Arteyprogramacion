from turtle import *
from PIL import Image 
import turtle 
from tkinter import *
import math 
from PIL import Image 


  
def fractal1():
    speed('fastest') 
  
    rt(-90) 
  
    angle = 30
  
    def y(sz, level):    
  
        if level > 0: 
            colormode(255) 
          
        
        
        
        
            pencolor(0, 255//level, 0) 
          
        
            fd(sz) 
  
            rt(angle) 
  
        
        
            y(0.8 * sz, level-1) 
          
            pencolor(0, 255//level, 0) 
          
            lt( 2 * angle ) 
  
        
        
            y(0.8 * sz, level-1) 
          
            pencolor(0, 255//level, 0) 
          
            rt(angle) 
            fd(-sz) 
           
          
    y(100, 7) 
def fractal2():
    xa = -2.0
    xb = 1.0
    ya = -1.5
    yb = 1.5
  
    maxIt = 255 
  
    imgx = 512
    imgy = 512
    image = Image.new("RGB",(imgx, imgy)) 
  
    for y in range(imgy): 
        zy = y * (yb - ya) / (imgy - 1)  + ya 
        for x in range(imgx): 
            zx = x * (xb - xa) / (imgx - 1)  + xa 
            z = zx + zy * 1j
            c = z 
            for i in range(maxIt): 
                if abs(z) > 2.0: break
                z = z * z + c 
            image.putpixel((x, y),(i % 4 * 64, i % 8 * 32, i % 16 * 16)) 
  
    image.show() 
def espiralfibonacci():
    def fiboPlot(n): 
        a = 0
        b = 1
        square_a = a 
        square_b = b 
  
    
        x.pencolor("blue") 
  
    
        x.forward(b * factor) 
        x.left(90) 
        x.forward(b * factor) 
        x.left(90) 
        x.forward(b * factor) 
        x.left(90) 
        x.forward(b * factor) 
  
    
        temp = square_b 
        square_b = square_b + square_a 
        square_a = temp 
      
    
        for i in range(1, n): 
            x.backward(square_a * factor) 
            x.right(90) 
            x.forward(square_b * factor) 
            x.left(90) 
            x.forward(square_b * factor) 
            x.left(90) 
            x.forward(square_b * factor) 
  
        
            temp = square_b 
            square_b = square_b + square_a 
            square_a = temp 
  
    
        x.penup() 
        x.setposition(factor, 0) 
        x.seth(0) 
        x.pendown() 
  
    
        x.pencolor("red") 
  
    
        x.left(90) 
        for i in range(n): 
            print(b) 
            fdwd = math.pi * b * factor / 2
            fdwd /= 90
            for j in range(90): 
                x.forward(fdwd) 
                x.left(1) 
            temp = a 
            a = b 
            b = temp + b 
  
  
    factor = 1
  
    n = int(input('Enter the number of iterations(must be > 1): ')) 
  
    if n > 0: 
        print("Fibonacci series for", n, "elements :") 
        x = turtle.Turtle() 
        x.speed(100) 
        fiboPlot(n) 
        turtle.done() 
    else: 
        print("Number of iterations must be > 0") 
def sierpinskitriangulo():
    def sierpinski(canvas, x, y, size, level):
        x = float(x)
        y = float(y)
        if (level == 0):
            canvas.create_polygon(x, y, x+size, y, x+size/2, y-size*math.sqrt(3)/2,fill="green")
        else:
            sierpinski(canvas, x, y, size/2, level-1)
            sierpinski(canvas, x+size/2, y, size/2, level-1)
            sierpinski(canvas, x+size/4, y-size*math.sqrt(3)/4,size/2, level-1)
    root = Tk()
    myCanvas = Canvas(root, width = 600, height=600)
    myCanvas.pack()
    sierpinski(myCanvas, 50, 500, 500, 3)
    root.mainloop()
def Julia():
    if __name__ == "__main__": 
    
    
    
        w, h, zoom = 1920,1080,1
   
    
        bitmap = Image.new("RGB",(w, h), "white") 
  
    
    
        pix = bitmap.load() 
     
    
    
        cX, cY = -0.7, 0.27015
        moveX, moveY = 0.0, 0.0
        maxIter = 255
   
        for x in range(w): 
            for y in range(h): 
                zx = 1.5*(x - w/2)/(0.5*zoom*w) + moveX 
                zy = 1.0*(y - h/2)/(0.5*zoom*h) + moveY 
                i = maxIter 
                while zx*zx + zy*zy < 4 and i > 1: 
                    tmp = zx*zx - zy*zy + cX 
                    zy,zx = 2.0*zx*zy + cY, tmp 
                    i -= 1
  
            
            
                pix[x,y] = (i << 21) + (i << 10) + i*8
      
        
        bitmap.show() 




banner = """
  /$$$$$$              /$$                                                                                                                                  /$$                    
 /$$__  $$            | $$                                                                                                                                 |__/                    
| $$  \ $$  /$$$$$$  /$$$$$$    /$$$$$$        /$$   /$$        /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$   /$$$$$$$ /$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$$ /$$__  $$|_  $$_/   /$$__  $$      | $$  | $$       /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|____  $$| $$_  $$_  $$ |____  $$ /$$_____/| $$ /$$__  $$| $$__  $$
| $$__  $$| $$  \__/  | $$    | $$$$$$$$      | $$  | $$      | $$  \ $$| $$  \__/| $$  \ $$| $$  \ $$| $$  \__/ /$$$$$$$| $$ \ $$ \ $$  /$$$$$$$| $$      | $$| $$  \ $$| $$  \ $$
| $$  | $$| $$        | $$ /$$| $$_____/      | $$  | $$      | $$  | $$| $$      | $$  | $$| $$  | $$| $$      /$$__  $$| $$ | $$ | $$ /$$__  $$| $$      | $$| $$  | $$| $$  | $$
| $$  | $$| $$        |  $$$$/|  $$$$$$$      |  $$$$$$$      | $$$$$$$/| $$      |  $$$$$$/|  $$$$$$$| $$     |  $$$$$$$| $$ | $$ | $$|  $$$$$$$|  $$$$$$$| $$|  $$$$$$/| $$  | $$
|__/  |__/|__/         \___/   \_______/       \____  $$      | $$____/ |__/       \______/  \____  $$|__/      \_______/|__/ |__/ |__/ \_______/ \_______/|__/ \______/ |__/  |__/
                                               /$$  | $$      | $$                           /$$  \ $$                                                                             
                                              |  $$$$$$/      | $$                          |  $$$$$$/                                                                             
                                               \______/       |__/                           \______/                                                                              
                                              """
print(banner)
print("fractal 1 ->> 1")
print("fractal 2 ->> 2")
print("espiral de fibonacci ->> 3")
print("Triangulo de Sierpinski ->> 4")
input = input("que quieres ver?:")
if input == "1":
    fractal1()
if input == "2":
    fractal2()
if input == "3":
    espiralfibonacci()
if input == "4":
    sierpinskitriangulo()
if input == "5":
    Julia()
