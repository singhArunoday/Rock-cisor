from tkinter import *
from PIL import Image,ImageTk
import random

root = Tk()

root.title("Sync Interns Task 2")
root.configure(bg="white")

rock_img_user=ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_user=ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_user=ImageTk.PhotoImage(Image.open("scissors.png"))

rock_img_comp=ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissors.png"))

user_label= Label(root,image=scissor_img_user)
comp_label= Label(root,image=scissor_img_comp)
user_label.grid(row=1,column=0)
comp_label.grid(row=1,column=4)

user_identifier=Label(root,text="User",font=50,bg="white").grid(row=0,column=0)
comp_identifier=Label(root,text="Computer",font=50,bg="white").grid(row=0,column=4)


msg=Label(root,font=50,bg="white",fg="black")
msg.grid(row=1,column=2)

def updatemsg(x):
    msg['text'] =x


def winner(user,comp):
    if user==comp:
        updatemsg("It's Tie!!")
        
    elif user=="Rock":
        if comp=="Paper":
            updatemsg("You Loose")
        else:
            updatemsg("You Won")

        
    elif user=="Paper":
        if comp=="Scissor":
            updatemsg("You Loose")

        elif comp=="Rock":
            updatemsg("You Won")

        else:
            updatemsg("You Loose")
    

    elif user=="Scissor":
        if comp=="Rock":
            updatemsg("You Loose")
        else:
            updatemsg("You Won")

    else:
        pass
                
choices=["Rock","Paper","Scissor"]

def choice(x):
    #for Comp
    comp_choice=choices[random.randint(0,2)]
    
    if comp_choice=="Rock":
        comp_label.configure(image=rock_img_comp)
    elif comp_choice=="Paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    #user
    if x=="Rock":
        user_label.configure(image=rock_img_user)
    elif x=="Paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)

    winner(x,comp_choice)
        
rock=Button(root,width=20,height=2,text="Rock",bg="blue",fg="black",command=lambda:choice("Rock")).grid(row=2,column=1)
rock=Button(root,width=20,height=2,text="Paper",bg="blue",fg="black",command=lambda:choice("Paper")).grid(row=2,column=2)
rock=Button(root,width=20,height=2,text="Scissor",bg="blue",fg="black",command=lambda:choice("Scissor")).grid(row=2,column=3)



root.mainloop()
