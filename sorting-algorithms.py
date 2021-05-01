import tkinter
import random
import time

Interface = tkinter.Tk()

Interface.title("Test")

testCanvas = tkinter.Canvas(Interface,bg="gray",height=720,width=1080)

def draw(data,colored,color):
    testCanvas.delete("all")

    for i in range(100):
        localColor = "red"
        if i in colored:
            localColor = color
        value = data[i]
        x1= i*10.8
        x2= i*10.8 +10.8
        y1= 720
        y2= 715 - value*7.2
        rect = testCanvas.create_rectangle((x1,y1,x2,y2),fill=localColor)
    testCanvas.pack()
    Interface.update()

def bubble(data):
    n = len(data)

    for i in range(n):
        for j in range(0,n-i-1):
            if(data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]

                draw(data,(j,j+1),"yellow")
            else:
                draw(data,(j,j+1),"blue")
            time.sleep(0.01)

def insertion(data):
    for i in range(0,len(data)):
        for j in range(i-1,-1,-1):
            if(data[j]>data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]

                draw(data, (j,j+1),"yellow")
                time.sleep(0.01)
            else:
                draw(data, (j,j+1),"blue")
                time.sleep(0.01)
                break

def selection(data):
    for i in range(0,len(data)):
        for j in range(i,-1,-1):
            if(data[j]<data[i]):
                temp = data[i]
                del data[i]
                data.insert(j+1,temp)

                draw(data,(i,j),"blue")

                time.sleep(0.01)
                break
            else:
                draw (data,(i,j),"yellow")
                time.sleep(0.01)
        else:
            temp = data[i]
            del data[i]
            data.insert(0,temp)

            draw(data,(i,0),"blue")

            time.sleep(0.01)


givenList = list(range(100))
for i in range(len(givenList)):
    chosen = random.randint(i,len(givenList)-1)
    givenList[i] , givenList[chosen] = givenList[chosen] , givenList[i]

draw(givenList,(),"")

selection(givenList)

draw(givenList,(),"")
Interface.mainloop()