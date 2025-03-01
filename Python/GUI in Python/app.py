from tkinter import *
from mydb import database
from tkinter import messagebox
from myapi import API

class NLPAap:
    
    def __init__(self):
        
        self.dbo = database()
        self.apio = API()
        
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap("resources/favicon.ico")
        self.root.geometry("350x600")
        self.root.configure(bg="#34495E")
        
        self.login_gui()
        
        self.root.mainloop()


    def login_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))
        heading.configure(font=("verdana",24,"bold"))

        #email section:
        Label1 = Label(self.root,text="Enter e-mail")                     
        Label1.pack(pady=(10,10))                                         
        
        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        #password section
        Label2 = Label(self.root,text="Enter Password")                    
        Label2.pack(pady=(10,10))                                         
        
        self.password_input = Entry(self.root,width=50,show="*")
        self.password_input.pack(pady=(5,10),ipady=4)
        
        #login button
        lgn_btn = Button(self.root,text="Login",width=20,height=1,command=self.perform_login)
        lgn_btn.pack(pady=(10,10))
        
        #Register redirect section
        Label3 = Label(self.root,text="Not a member ?")                   
        Label3.pack(pady=(10,10))                                          
        
        redirect_btn = Button(self.root,text="Register Now",width=20,height=1,command=self.register_gui)
        redirect_btn.pack(pady=(10,10))

        
    def register_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white")  
        heading.pack(pady=(30,30))                                         
        heading.configure(font=("verdana",24,"bold"))         
        
        #name section
        Label0 = Label(self.root,text="Enter Name")                     
        Label0.pack(pady=(10,10))                                         
        
        self.name_input = Entry(self.root,width=50)                             
        self.name_input.pack(pady=(5,10),ipady=4)              

        #email section:
        Label1 = Label(self.root,text="Enter e-mail")                     
        Label1.pack(pady=(10,10))                                         
        
        self.email_input = Entry(self.root,width=50)                             
        self.email_input.pack(pady=(5,10),ipady=4)                               

        #password section
        Label2 = Label(self.root,text="Enter Password")                    
        Label2.pack(pady=(10,10))                                         
        
        self.password_input = Entry(self.root,width=50,show="*")                 
        self.password_input.pack(pady=(5,10),ipady=4)                            

        #Register button
        register_btn = Button(self.root,text="Register",width=20,height=1,command=self.perform_registeration)
        register_btn.pack(pady=(10,10))
        
        #login redirect section
        Label3 = Label(self.root,text="Already a member ?")                   
        Label3.pack(pady=(10,10))                                          
        
        lgn_btn = Button(self.root,text="Login Now",width=20,height=1,command=self.login_gui)    
        lgn_btn.pack(pady=(10,10))
        
    
    def perform_registeration(self):
        
        #fetching data from GUI
        
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.add_data(name,email,password)
        
        if response:
            messagebox.showinfo("Success", "Registration Successful. You can login now.")
        else:
            messagebox.showerror("Error", "Email already exists")
            

    def perform_login(self):
        
        email = self.email_input.get()
        password = self.password_input.get()
        
        response = self.dbo.search(email,password)
        
        if response:
            messagebox.showinfo("Success", "Login Successful")
            self.home_gui()
        else:
            messagebox.showerror("Error","Incorrect Email/Password")
            

    def home_gui(self):
        
        self.clear()
        
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))                                         
        heading.configure(font=("verdana",24,"bold"))       
        
        sentiment_btn = Button(self.root,text="Sentiment Analysis",width=30,height=4,command=self.sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
        
        ner_btn = Button(self.root,text="Named Entity Recognition",width=30,height=4,command=self.NER_analysis)
        ner_btn.pack(pady=(10,10))
        
        emotion_btn = Button(self.root,text="Emotion Prediction",width=30,height=4,command=self.emotion_analysis)
        emotion_btn.pack(pady=(10,10))
        
        logout_btn = Button(self.root,text="Logout",width=20,height=1,command=self.login_gui)     
        logout_btn.pack(pady=(10,10))
        
        
    def sentiment_analysis(self):
        
        self.clear()
        
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))                                         
        heading.configure(font=("verdana",24,"bold"))   
        
        heading2 = Label(self.root,text="Sentiment Analysis",bg="#34495E",fg="white")
        heading2.pack(pady=(5,20))                                         
        heading2.configure(font=("verdana",20))   
        
        Label1 = Label(self.root,text="Enter the Text to Analyze")                   
        Label1.pack(pady=(10,10))    
        
        self.sentiment_input = Entry(self.root,width=50)                
        self.sentiment_input.pack(pady=(5,10),ipady=4) 
        
        sentiment_btn = Button(self.root,text="Analyze Sentiment",width=20,height=1,command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))
        
        self.sentiment_result = Label(self.root,text="",bg="#34495E",fg="white")
        self.sentiment_result.pack(pady=(10,10))
        self.sentiment_result.configure(font=("verdana"))     
        
        goback_btn = Button(self.root,text="Go to home",width=20,height=1,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
        
    def NER_analysis(self):
        
        self.clear()
        
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))                                         
        heading.configure(font=("verdana",24,"bold"))   
        
        heading2 = Label(self.root,text="Named Entity Recognition",bg="#34495E",fg="white")
        heading2.pack(pady=(5,20))                                         
        heading2.configure(font=("verdana",18))   
        
        Label1 = Label(self.root,text="Enter the Text")                   
        Label1.pack(pady=(10,10))    
        
        self.ner_input = Entry(self.root,width=50)                
        self.ner_input.pack(pady=(5,10),ipady=4) 
        
        ner_btn = Button(self.root,text="Get Recognition",width=20,height=1,command=self.do_ner_analysis)
        ner_btn.pack(pady=(10,10))
        
        self.ner_result = Label(self.root,text="",bg="#34495E",fg="white")
        self.ner_result.pack(pady=(10,10))
        self.ner_result.configure(font=("verdana"))     
        
        goback_btn = Button(self.root,text="Go to home",width=20,height=1,command=self.home_gui)
        goback_btn.pack(pady=(10,10))
        
        
    def emotion_analysis(self):
        
        self.clear()
        
        heading = Label(self.root,text="NLP App",bg="#34495E",fg="white")
        heading.pack(pady=(30,30))                                         
        heading.configure(font=("verdana",24,"bold"))   
        
        heading2 = Label(self.root,text="Emotion Analysis",bg="#34495E",fg="white")
        heading2.pack(pady=(5,20))                                         
        heading2.configure(font=("verdana",20))   
        
        Label1 = Label(self.root,text="Enter the Text")                   
        Label1.pack(pady=(10,10))    
        
        self.emotion_input = Entry(self.root,width=50)                
        self.emotion_input.pack(pady=(5,10),ipady=4) 
        
        emotion_btn = Button(self.root,text="Get Analysis",width=20,height=1,command=self.do_emotion_analysis)
        emotion_btn.pack(pady=(10,10))
        
        self.emotion_result = Label(self.root,text="",bg="#34495E",fg="white")
        self.emotion_result.pack(pady=(10,10))
        self.emotion_result.configure(font=("verdana"))     
        
        goback_btn = Button(self.root,text="Go to home",width=20,height=1,command=self.home_gui)
        goback_btn.pack(pady=(10,10))    
        
        
#-----------------------------------------------------------------------------------------------------------------#
    def do_sentiment_analysis(self):
            
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text) 
        
        txt = ''
        for i in result["sentiment"]:
            txt = txt + i + " -> " + str(result["sentiment"][i]) + "\n"
            
        print(result)
        self.sentiment_result['text'] = txt
        

    def do_ner_analysis(self):
            
        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)
        
        print(result)
        txt = ''
        for i in result["entities"]:
            for j in i: 
                txt = txt + j + ": " + str(i[j]) + "\n"
            txt = txt + "\n"

        self.ner_result['text'] = txt
        
        
    def do_emotion_analysis(self):
            
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)
        
        txt = ''
        for i in result["emotion"]:
            txt = txt + i + " -> " + str(result["emotion"][i]) + "\n"
            
        print(txt)
        self.emotion_result['text'] = txt
        

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

nlp = NLPAap()
