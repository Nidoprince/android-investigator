import tkinter as tk
import random
from placeMaker import *

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.begin()

    def begin(self):
        self.edge = []
        for x in range(5):
            self.edge.append(tk.Label(self,text=" "))
            self.edge[x].grid(row=11+x,column=0)
        if(self.loadSave()):
            self.createWidgets(self.place)
            if(self.conversation!="False"):
                self.talk(self.conversation)
        else:
            self.startScreen()
            
    def startScreen(self):
        self.cats = tk.Canvas(self, bg = 'black', height = 300, width = 500)
        self.inv = tk.PhotoImage(file="privateinvestocat.gif")
        self.inv = self.inv.subsample(3,3)
        self.cats.create_image(250,150,image=self.inv)
        self.cats.image=self.inv
        self.cats.grid(row=0,column=0,rowspan=6,columnspan=10)
        self.text=tk.Text(self, width=50,height=5)
        self.text.insert(0.0,"Tell me your name son.")
        self.text["state"]='disabled'
        self.text.grid(row=7,column=2,rowspan=4,columnspan=6)
        self.enter = tk.Entry(self,bd=5)
        self.enter.grid(row=13,column=3,columnspan=2)
        self.buttons = [tk.Button(self)]
        self.buttons[0]["text"] = "Tell Name"
        self.buttons[0]["command"] = self.submitName
        self.buttons[0].grid(row=13,column=5)
        self.conversation = "False"
        
    def submitName(self):
        self.name = self.enter.get()
        self.enter.grid_forget()
        del self.enter
        self.text["state"]='normal'
        self.text.delete(0.0,20.20)
        self.text.insert(0.0,"So they call you "+self.name+" huh?")
        self.text["state"]='disabled'
        self.text.grid(row=7,column=2,rowspan=4,columnspan=6)
        self.buttons[0]["text"] = "Continue"
        self.buttons[0]["command"] = lambda: middle.go("testroom.room")
        self.buttons[0].grid(row=13,column=5)

    def changeText(self,text):
        self.text["state"]='normal'
        self.text.delete(0.0,20.20)
        self.text.insert(0.0,text)
        self.text["state"]='disabled'
        self.text.grid(row=7,column=2,rowspan=4,columnspan=6)
       
    def go(self,file):
        self.cats.grid_forget()
        self.text.grid_forget()
        for x in self.buttons:
            x.grid_forget()
        self.place=file
        self.conversation = "False"
        self.createWidgets(self.place)

    def talk(self,file):
        self.text.grid_forget()
        for x in self.buttons:
            x.grid_forget()
        self.conversation=file
        self.createWidgets(self.conversation)
        
        
    def createWidgets(self,kwenda):
        location = Place(loadRoom(kwenda))
        if(location.picNum()>0):
            self.cats = tk.Canvas(self, bg = 'blue', height = 300, width = 500)
            pic = []
            for x in range(location.picNum()):
                pic.append(tk.PhotoImage(file=location.getPicFile(x)))
                pic[x] = pic[x].subsample(3,3)
                self.cats.create_image(location.getPicCoor(x),image=pic[x])
            self.cats.image=pic
            self.cats.grid(row=0,column=0,rowspan=6,columnspan=10)
        
        self.text=tk.Text(self, width=50,height=5)
        self.text.insert(0.0,eval(location.getText()))
        self.text["state"]='disabled'
        self.text.grid(row=7,column=2,rowspan=4,columnspan=6)

        self.buttons = []
        for x in range(location.buttonNum()):
            self.buttons.append(tk.Button(self, text=location.getButtonName(x), fg=location.getButtonColor(x)))
            self.buttons[x]["command"] = eval(location.getButtonEffect(x))
            self.buttons[x].grid(row=location.getButtonRow(x),column=location.getButtonCol(x),rowspan=location.getButtonRowS(x),columnspan=location.getButtonColS(x))
        
    def loadSave(self):
        save = open("save.dat","r")
        if(eval(save.readline())==False):
            save.close()
            return False
        else:
            self.name = save.readline().strip()
            self.place = save.readline().strip()
            self.conversation = save.readline().strip()
            save.close()
            return True

    def say_hi(self):
        print("hi there, everyone!")

    def killCan(self):
        self.cats.delete("all")

    def rand(self):
        print(random.randrange(0,10))

    def quit(self):
        saveText="True\n"
        saveText+=self.name+"\n"
        saveText+=self.place+"\n"
        saveText+=self.conversation
        save = open("save.dat","w")
        save.write(saveText)
        save.close()
        top.destroy()

    def reset(self):
        save = open("save.dat","w")
        save.write("False")
        save.close()
        top.destroy()
        
    def drawPic(self):
        self.cats.create_line(random.randrange(0,500),random.randrange(0,300),random.randrange(0,500),random.randrange(0,300))

top = tk.Tk()
middle = Application(master = top)
middle.mainloop()
