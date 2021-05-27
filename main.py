import tkinter
from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3
############################ FUNCTIONALITY PART ########################################################################

engine =pyttsx3.init() #create an object of engine class
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

def search():
    data = json.load(open('data.json'))
    word = enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning = data[word]
        textArea.delete(0.0,END)  #delete everything in textarea before writing something else
        for item in meaning:
            textArea.insert(END,u'\u2022'+item+"\n\n")
    elif len(get_close_matches(word,data.keys()))>0:
        close_match = get_close_matches(word,data.keys())[0]
        res = messagebox.askyesno('Confirm',f'Did you mean {close_match} instead?')
        if res==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)
            meaning = data[close_match]
            textArea.delete(0.0,END)
            for item in meaning:
                textArea.insert(END,u'\u2022'+item+'\n\n')
        else:
            messagebox.showerror("Information", f'The word {word} does not exist,please double check it')
            enterwordEntry.delete(0, END)
            textArea.delete(0.0, END)
    else:
        messagebox.showinfo("Information",f'The word {word} does not exist')
        enterwordEntry.delete(0,END)
        textArea.delete(0.0,END)

def clear():
    enterwordEntry.delete(0,END)
    textArea.delete(1.0,END)

def iexit():
    res = messagebox.askyesno('Confirm','Do you want to exit?')
    if res:
        root.destroy()
    else:
        pass

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textArea.get(1.0,END))
    engine.runAndWait()





############################## GUI PART ################################################################################
#in order to create the window, we use only one method with is inside the module tkinter
root = Tk()  #Tk is a class

root.geometry('1000x626+100+30')  #qe me qendru ne pozite statike ndaj x(100) dhe y(30)
root.title("Hello Talking Dictionary")
root.resizable(0,0) # dmth nuk mundesh me bo change ne width ose ne height

bgImage = PhotoImage(file="bg.png")

bgLabel = Label(root,image=bgImage)
bgLabel.place(x=0,y=0)

enterwordLabel= Label(root, text="Enter Word", font=("castellar",29,'bold'), foreground="red3", background="whitesmoke")
enterwordLabel.place(x=530, y=20)

enterwordEntry = Entry(root,font=("arial",23,'bold'), justify=CENTER,bd=8,relief=GROOVE)
enterwordEntry.place(x=510, y=80)

searchImage = PhotoImage(file='search.png')
searchButton = Button(root,image=searchImage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=search)
searchButton.place(x=620, y=150)

micImage= PhotoImage(file='mic.png')
micButton = Button(root,image=micImage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=wordaudio)
micButton.place(x=710,y=153)


meaningLabel= Label(root, text="Meaning", font=("castellar",29,'bold'), foreground="red3", background="whitesmoke")
meaningLabel.place(x=530, y=240)

textArea = Text(root,width=34,height=8,font=('arial',18,'bold'),bd=8,relief=GROOVE)
textArea.place(x=530, y=300)
# add a scroll bar to textarea
# # Create a scrollbar
# scroll_bar = tkinter.Scrollbar(root)
#
# # Pack the scroll bar
# # Place it to the right side, using tk.RIGHT
# scroll_bar.pack(side=tkinter.RIGHT)

# Pack it into our tkinter application
# Place the text widget to the left side
#textArea.pack(side=tkinter.LEFT)




audioImage = PhotoImage(file='microphone.png')
audioButton = Button(root,image=audioImage, bd = 0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',command=meaningaudio)
audioButton.place(x=530, y= 555)

clearImage = PhotoImage(file='clear.png')
clearButton = Button(root,image=clearImage, bd = 0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',command=clear)
clearButton.place(x=660, y= 555)

exitImage = PhotoImage(file='exit.png')
exitButton= Button(root,image=exitImage, bd = 0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke',command = iexit)
exitButton.place(x=790, y= 555)

def enter_function(event):
    searchButton.invoke()
root.bind('<Return>',enter_function)






root.mainloop()  # in order for the window to remain in hold, this mainloop() method exists inside Tk class.



