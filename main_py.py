from tkinter import *
import pandas
import random
import time
#from sklearn.utils import shuffle
#df = shuffle(df)
df = pandas.read_csv("HSK/HSK_3_pinyin.csv")
column_list = []
right = 0
wrong = 0
current_word = 0
word_count_list = []
wrong_words = []

def inc_r():
    global current_word
    a = len(df) - 1
    if current_word == a:
        current_word = 0
    global right
    right += 1
    l1 = Label(window,text=getText(),width=15,height=5,font=("Helvetica", 32))
    l1.grid(row=0, column=1)
    l2 = Label(window,text="Right: {}".format(right),width=15,height=5,font=("Helvetica", 32))
    l2.grid(row=0, column=0)
    l3 = Label(window,text="Wrong: {}".format(wrong),width=15,height=5,font=("Helvetica", 32))
    l3.grid(row=0, column=2)

    global column_list
    column_list = []

    b2 = Button(window,text=getAnsText(),command=inc_r,width=12,height=3,font=("Helvetica", 32))
    b2.grid(column=Retrieve_Random_Column_Number(),row=1)
    b1 = Button(window,text=getRandomText(),command=inc_w,width=12,height=3,font=("Helvetica", 32))
    b1.grid(column=Retrieve_Random_Column_Number(),row=1)
    b3 = Button(window,text=getRandomText(),command=inc_w,width=12,height=3,font=("Helvetica", 32))
    b3.grid(column=Retrieve_Random_Column_Number(),row=1)


def inc_w():
    global wrong_words
    global current_word
    a = current_word - 1

    if a in wrong_words:
        pass
    else:
        wrong_words.append(a)

    a = len(df) - 1
    if current_word == a:
        current_word = 0
    global wrong
    wrong += 1
    l1 = Label(window,text=getText(),width=15,height=5,font=("Helvetica", 32))
    l1.grid(row=0, column=1)
    l2 = Label(window,text="Right: {}".format(right),width=15,height=5,font=("Helvetica", 32))
    l2.grid(row=0, column=0)
    l3 = Label(window,text="Wrong: {}".format(wrong),width=15,height=5,font=("Helvetica", 32))
    l3.grid(row=0, column=2)

    global column_list
    column_list = []

    b2 = Button(window,text=getAnsText(),command=inc_r,width=12,height=3,font=("Helvetica", 32))
    b2.grid(column=Retrieve_Random_Column_Number(),row=1)
    b1 = Button(window,text=getRandomText(),command=inc_w,width=12,height=3,font=("Helvetica", 32))
    b1.grid(column=Retrieve_Random_Column_Number(),row=1)
    b3 = Button(window,text=getRandomText(),command=inc_w,width=12,height=3,font=("Helvetica", 32))
    b3.grid(column=Retrieve_Random_Column_Number(),row=1)
    for i in wrong_words:
        print(df.iloc[i,0])
    print("\n\n\n\n")

def exit():
    global wrong_words
    global column_list
    global right
    global wrong
    global current_word
    global word_count_list
    global window_2
    window.quit()
    window_2 = Tk()
    window_2.wm_title("Session Summary")
    window_2.geometry("395x690+850+100")
    label_2 = Label(window_2,text="Words to review",width=15,height=4,font=("Helvetica", 32),highlightbackground="red",borderwidth=5)
    label_2.grid(column=0,row=0)
    list1 = Listbox(window_2,font=("Helvetica", 32))
    list1.grid(row=1,column=0,columnspan=10,rowspan=10,padx=20,pady=20)
    for i in wrong_words:
        if df.iloc[i,0] == "B":
            pass
        else:
            list1.insert(END,df.iloc[i,0] + " : " + df.iloc[i,1] + " : " + df.iloc[i,2])
    column_list = []
    right = 0
    wrong = 0
    current_word = 0
    word_count_list = []
    wrong_words = []

    button_1 = Button(window_2,text="Go again",height=2,width=8,font=("Helvetica", 32),highlightbackground="red",highlightthickness=5,command=destroy_2)
    button_1.grid(row=13,column=0,padx=32,pady=32)
    window_2.mainloop()
def destroy_2():
    global window_2
    window_2.destroy()
    l2 = Label(window,text="Right: 0",width=15,height=5,font=("Helvetica", 32))
    l2.grid(row=0, column=0)
    l3 = Label(window,text="Wrong: 0",width=15,height=5,font=("Helvetica", 32))
    l3.grid(row=0, column=2)
def getText():
    global text
    global current_word
    global random_letter_var
    random_letter_var = random.randrange(0,len(df))
    text = df.iloc[current_word,1] + "\n" +df.iloc[current_word,0]
    while text == "B":
        random_letter_var = random.randrange(0,len(df))
        text = df.iloc[current_word,0]
    return text

def getAnsText():
    global AnsText
    global current_word

    AnsText = df.iloc[current_word,2]
    current_word += 1
    return AnsText

def getRandomText():
    randomNum = random.randrange(0,len(df))
    RandomText = df.iloc[randomNum,2]
    while RandomText == AnsText:
        randomNum = random.randrange(0,len(df))
        RandomText = df.iloc[randomNum,2]
    return RandomText

def Retrieve_Random_Column_Number():
    column = random.randrange(0,3)
    if column in column_list:
        while(column in column_list):
            column = random.randrange(0,3)
        column_list.append(column)
        return column
    else:
        column_list.append(column)
        return column

window = Tk()
window.wm_title("Active Session")

window.geometry("820x420+0+100")

l1 = Label(window,text=getText(),width=15,height=5,font=("Helvetica", 32))
l1.grid(row=0, column=1)
l2 = Label(window,text="Right: {}".format(right),width=15,height=5,font=("Helvetica", 32))
l2.grid(row=0, column=0)
l3 = Label(window,text="Wrong: {}".format(wrong),width=15,height=5,font=("Helvetica", 32))
l3.grid(row=0, column=2)

b2 = Button(window,text=getAnsText(),command=inc_r,width=12,height=3,font=("Helvetica", 32))
b2.grid(column=Retrieve_Random_Column_Number(),row=1)
b1 = Button(window,text=getRandomText(),command=inc_w,width=12,height=3,font=("Helvetica", 32))
b1.grid(column=Retrieve_Random_Column_Number(),row=1)
b3 = Button(window,text=getRandomText(),command=inc_w,width=12,height=3,font=("Helvetica", 32))
b3.grid(column=Retrieve_Random_Column_Number(),row=1)

lower_label_1 = Label(window,text=" ",width=15,height=5)
lower_label_1.grid(row=2,column=0)
lower_label_2 = Label(window,text=" ",width=15,height=5)
lower_label_2.grid(row=2,column=2)
lower_button_end = Button(window,text="Finish",command=exit,width=12,height=3,font=("Helvetica", 32))
lower_button_end.grid(row=2,column=1)
window.mainloop()
