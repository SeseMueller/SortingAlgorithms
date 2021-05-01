import tkinter #TKInter for displaying the visualization
import random #Random to shuffle the test list
import time #Time to let time pass between stages of the sorting process

Interface = tkinter.Tk() #The window that will be displayed

Interface.title("Sorting Algorithms") 

testCanvas = tkinter.Canvas(Interface,bg="gray",height=720,width=1080) #Creates the Canvas on which the bars will be drawn
Interface.resizable(0,0) #Stops the window from being resized

def draw(data,colored,color):
    """
    Draws the given data to the screen. 
    The List (or tuple) "colored" contains the indecies that should not be colored in red, but in the given color "color".
    """
    testCanvas.delete("all") #Clears the Canvas

    for i in range(100): #Loops over all data
        localColor = "red"

        if i in colored: #If the special color should be used, apply it
            localColor = color
        
        #Calculates the positions of the bars 
        x1= i*10.8 
        x2= i*10.8 +10.8
        y1= 720
        y2= 715 - data[i]*7.2
        rect = testCanvas.create_rectangle((x1,y1,x2,y2),fill=localColor) #Draws the bars in their corresponding colors

    testCanvas.pack()
    Interface.update() #Updates the window to display the changes

def bubble(data):
    """
    A simple Implementation of the Bubblesort algorithm.
    """
    n = len(data)

    for i in range(n): #Loops over all elements
        for j in range(0,n-i-1): #Loops over one element less each time
            if(data[j]>data[j+1]): #Swaps two entries if they are in the wrong order
                data[j], data[j+1] = data[j+1], data[j]

                draw(data,(j,j+1),"yellow") #Draws the data both times, but in yellow if they were swapped
            else:
                draw(data,(j,j+1),"blue") #Draws the values that were compared, but not swapped in blue
            time.sleep(0.01) #Sleeps for a short period of time to run at a reasonably speed

def insertion(data):
    """
    A simple Implementation of the Insertionsort algorithm. 
    """
    for i in range(len(data)): #Loops over all elements
        for j in range(i-1,-1,-1): #Loops over all already sorted elements in reverse order
            if(data[j]>data[j+1]): #If these two values are out of order, swap them
                data[j], data[j+1] = data[j+1], data[j]

                draw(data, (j,j+1),"yellow") #Draw with yellow, because these two values were swapped.
                time.sleep(0.01)
            else:
                draw(data, (j,j+1),"blue") #Draw with blue, because the right place was found and nothing was changed
                time.sleep(0.01)
                break

def selection(data):
    """
    A simple Implementation of the Selectionsort algorithm.
    """
    for i in range(len(data)): #Loops over all elements
        for j in range(i,-1,-1): #Loops over all already sorted elements in reverse order
            if(data[j]<data[i]): #If the value at j is lower than the value at i, the value at i should be inserted at j

                temp = data[i] #Stores the value at i
                del data[i] #Deletes that value at i
                data.insert(j+1,temp) #Reinserts the value at j

                draw(data,(i,j),"yellow") #Draws with yellow, because the data changed

                time.sleep(0.01)
                break
            else: #If the value is not yet low enough, continue
                draw (data,(i,j),"blue") #Draw with blue, because nothing changed
                time.sleep(0.01)
        else: #If the value was not able to be inserted anywhere in the already sorted list
            temp = data[i]
            del data[i]
            data.insert(0,temp) #Put the value at i to the beginning

            draw(data,(i,0),"yellow") #Draw with yellow, because the data changed

            time.sleep(0.01)


givenList = list(range(100)) #Generates a list from 0 to 99, inclusive
for i in range(len(givenList)): #Shuffles this list
    chosen = random.randint(i,len(givenList)-1)
    givenList[i] , givenList[chosen] = givenList[chosen] , givenList[i]

draw(givenList,(),"") #Draws the initial list in all red


try:

    #Executes one of the algorithms

    #bubble(givenList) 
    selection(givenList) 
    #insertion(givenList) 

except tkinter.TclError: #If the User closes the window, stop the program so it doesn't throw an error.
     exit()

draw(givenList,(givenList),"green") #At the end, draw the entire list in green because it's sorted
Interface.mainloop() #Doesn't close the window when it's done