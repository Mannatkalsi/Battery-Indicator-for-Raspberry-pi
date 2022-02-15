import os
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer, QSize

led = 2
def led_status():
    global LEDLIGHT
    if(led == 0):
        LEDLIGHT ="Off"
    elif(led==1):
        LEDLIGHT ="Soft"
    elif(led==2):
        LEDLIGHT ="Full"

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'About Charging'
        self.left = 150
        self.top = 100
        self.width = 320
        self.height = 200
        
        #timer to get led status every 0.5 second
        self.timer_led=QTimer()
        self.timer_led.timeout.connect(self.getLedStatus) #connect function
        self.timer_led.start(500)
        self.initUI()
    
     # User Interface   
    def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
        
            btn = QMessageBox.question(self, 'Battery', "Is battery Fully charged ?",QMessageBox.Yes | QMessageBox.No)
            if btn == QMessageBox.Yes:
                f = open('Timer.txt','w') #if user selects yes we clean the values in text file
                f.close()
                self.Count(100)#change to 55 mins so, t = 3300
            elif btn == QMessageBox.No:
                #self.Read()
                f = open('Timer.txt', 'r') #if user select no we read the value from text file 
                t = int(f.read())
                #print(t)
                self.Count(t)
                
            
            self.show()
    
    def Count(self,t): 
        while t:
            min, sec = divmod(t,60)
            timer = '{:02d}:{:02d}'.format(min,sec)
            print(timer, end="\r")
            time.sleep(1)
            f = open("Timer.txt", "w")
            f.close()
            f = open("Timer.txt", "a")
            f.write(str(t))
            f.close()
            if t > 0:
                self.getLedStatus()
               #Check led status
                if(LEDLIGHT == "Soft"):
                    t-=3
                    
                if(LEDLIGHT == "Full"):
                    t-=5
                    
                if(LEDLIGHT == "Off"):
                    t-=1
                    
                if(t== 55):#change to 10 mins t = 600
                    print("Battery Low!")
                    self.Warn()
                    #os.system("play /home/pi/Desktop/beep2.mp3")
                    
                elif(t == 15):#change to 5 mins , t = 300
                    print("Battery very Low!")
                    self.Warn()
                    #os.system("play /home/pi/Desktop/beep2.mp3")
    # warning function                
    def Warn(self):
        btn = QMessageBox.information(self,'Battery Low', " Please Charge your device ",QMessageBox.Ok, self.close())
        
     #getting LED status   
    def getLedStatus(self):
        #read Led Status
        led_status()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
            