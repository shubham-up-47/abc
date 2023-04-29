from kivy.app import App                                      # for window
from kivy.uix.widget import Widget                            # for widgets
from kivy.uix.screenmanager import ScreenManager, Screen      # for window manager
from kivy.properties import ObjectProperty                    # for defining window properties       
from kivy.lang import Builder                                 # for using kivyLang
from kivy.uix.popup import Popup                              # for popup window
from kivy.uix.floatlayout import FloatLayout                  # for float layout
import pandas as pd                                           # for data manipulation & analysis         


class windowManager(ScreenManager):               # class for managing screens
    pass
   
kv = Builder.load_file('loginMain.kv')            # load kv file 
sm = windowManager()                              # screen manager element

users = pd.read_csv(f'login.csv')      # read database 
 



class PopupWindow(Widget):    # calling popup function
    def btn(self):
        popFun()
   
class P(FloatLayout):         # to build GUI for popup window (for unsuccessful login/signup)
    pass
   
def popFun():                 # displaying popup content   
    show = P()
    window = Popup(title="popup", content=show, size_hint=(None,None), size=(300,300))
    window.open()
  



class loginWindow(Screen):                  # to validate login info
    email = ObjectProperty(None)            # object1
    pwd = ObjectProperty(None)              # object2

    def validate(self):                                          # validating self objects 
        if self.email.text not in users['Email'].unique():       # email not present already
            popFun()
        else: 
            sm.current = 'logdata'          # switch screen to show login successful  
            self.email.text = ""            # reset email text
            self.pwd.text = ""              # reset pwd text          
    
class loginMain(App):                       # to build gui for login window
    def build(self):
        return sm

class logDataWindow(Screen):               # to build gui for successful login window 
    pass
  
  


class signupWindow(Screen):                                                                 # to store signup info
    name2 = ObjectProperty(None)                                                            # object1
    email = ObjectProperty(None)                                                            # object2
    pwd = ObjectProperty(None)                                                              # object3

    def signupbtn(self): 
                                                                                            # creating dataFrame for the info
        user = pd.DataFrame([[self.name2.text,self.email.text,self.pwd.text]], columns=['Name','Email','Password'])
        
        if self.email.text != "":
            if self.email.text not in users['Email'].unique():                              # if email is not already used  
                user.to_csv(f'login.csv', mode='a', header=False, index=False)   # append data in append mode
                sm.current = 'login'                                                        # switch to login window 
                self.name2.text = ""                                                        # reset name2 text
                self.email.text = ""                                                        # reset email text
                self.pwd.text = ""                                                          # reset pwd text
        else:                                                                               # invalid input
            popFun()
       


  
sm.add_widget(loginWindow(name='login'))              # adding login window/screen
sm.add_widget(signupWindow(name='signup'))            # adding signup window/screen
sm.add_widget(logDataWindow(name='logdata'))          # adding logdata window/screen
  



if __name__=="__main__":      # driver function
    loginMain().run()


 
 