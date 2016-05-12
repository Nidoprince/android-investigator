class Place:
    def __init__(self, everything):
        print(everything)
        self.pics = everything[0]
        self.text = everything[1]
        self.buttons = everything[2]

    def picNum(self):
        return len(self.pics)
    
    def getPicCoor(self,n):
        return [int(self.pics[n][1]),int(self.pics[n][2])]

    def getPicFile(self,n):
        return self.pics[n][0]

    def getText(self):
        return self.text

    def buttonNum(self):
        return len(self.buttons)
    
    def getButtonName(self,n):
        return self.buttons[n][0]

    def getButtonColor(self,n):
        return self.buttons[n][1]

    def getButtonEffect(self,n):
        return self.buttons[n][2]

    def getButtonRow(self,n):
        return int(self.buttons[n][3])
    def getButtonCol(self,n):
        return int(self.buttons[n][4])
    def getButtonRowS(self,n):
        return int(self.buttons[n][5])
    def getButtonColS(self,n):
        return int(self.buttons[n][6])

def loadRoom(file):
    room = open(file,"r")
    roomType = room.readline().strip()
    if(roomType=="ALL"):
        nextL = room.readline().strip()
        pictures = []
        while(nextL!="###"):
            pictures.append(nextL.split())
            nextL = room.readline().strip()
    if(roomType=="ALL" or roomType=="TALK"):
        nextL = room.readline().strip()
        text = ""
        while(nextL!="###"):
            text+=nextL+"\n"
            nextL = room.readline().strip()
    if(roomType=="ALL" or roomType=="TALK"):
        nextL = room.readline().strip()
        buttons = []
        while(nextL!="###"):
            buttons.append(nextL.split("|"))
            nextL = room.readline().strip()
    room.close()
    if(roomType=="ALL"):
        return([pictures,text,buttons])
    elif(roomType=="TALK"):
        return([[],text,buttons])
        
    
