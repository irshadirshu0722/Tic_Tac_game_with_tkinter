

from  tkinter  import *

import pprint
currentuser = "X"
userchange={
    "X":"O",
    "O":"X"
}
res=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

boxes = []



window =Tk()
window.title("Tic Tac Toe")
window.config(width=500,height=500,bg="white")

state="normal"
def iswon(cuser):
    print("function inner",cuser)
    if (res[0][0]==cuser and res[0][1]==cuser and res[0][2]==cuser) or (res[1][0]==cuser and res[1][1]==cuser and res[1][2]==cuser) or (res[2][0]==cuser and res[2][1]==cuser and res[2][2]==cuser) or (res[0][0] == cuser and res[1][0] == cuser and res[2][0] == cuser) or (res[0][1] == cuser and res[1][1] == cuser and res[2][1] == cuser) or (res[0][2] == cuser and res[1][2] == cuser and res[2][2] == cuser) or (res[0][0] == cuser and res[1][1] == cuser and res[2][2] == cuser) or (res[0][2] == cuser and res[1][1] == cuser and res[2][0] == cuser):
        return True

def disablebutton():
    print("enter")
    for box in boxes:
        box.config(state="disabled")


def checkallboxclicked():
    isavailable=False
    for r in range(3):
        for c in range(3):
            if res[r][c]==-1:
                isavailable=True
    if not isavailable:
        label = Label(text=f"Draw", font=("Arial", 40, "normal"))
        label.grid(column=0, row=3, columnspan=3)
        disablebutton()
        return



def Addicon(box,r,c):
    global  currentuser,userchange,res,state
    if res[r][c]==-1:
        box.config(text=currentuser)
        res[r][c]=currentuser

        if iswon(currentuser):
            disablebutton()
            label = Label(text=f"user:{currentuser} Won",font=("Arial",40,"normal"))
            label.grid(column=0, row=3,columnspan=3)
            return
        else :


            currentuser = userchange[currentuser]

            current_user.config(text=f"user:{currentuser}")
        checkallboxclicked()




#-------------------------UI design-------------------------------------


heading = Label(text="Tic Tac Toe" , font=("Arial",40,"normal"))

heading.grid(column=0,row=0 ,columnspan=3)

current_user = Label(text=f"user:{currentuser.lower()}" , font=("Arial",40,"normal"))

current_user.grid(column=1,row=1)

for i in range(3):
    for j in range(3):
        new_box = Button(width=5, height=2, text="", font=("Arial", 50, "normal"), bg="grey")
        new_box.config(command=lambda b=new_box, r=i, c=j: Addicon(b, r, c))
        new_box.grid(column=j, row=i+2)
        boxes.append(new_box)



window.mainloop()

