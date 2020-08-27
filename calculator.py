import tkinter as tk
import math

def backspace():
    if label_in2["text"]=='' and label_op["text"]=='':
        label_in1["text"]=label_in1["text"][0:-1]
    elif label_in2["text"]=='':
        label_op["text"]=''
    else:
        label_in2["text"]=label_in2["text"][0:-1]

def clearall():
    label_ans["text"]=''
    label_in1["text"]=''
    label_in2["text"]=''
    label_op["text"]=''
    label_approx["text"]=''

def num_clicked(num):
        
    if label_ans["text"]!='' or (num == "3.14159265" and label_op["text"]=='') or (num == "2.71828182" and label_op["text"]==''):
        clearall()

    if len(label_in1["text"])==1 and label_in1["text"][0]=="0" and label_op["text"]=="":
        label_in1["text"]=label_in1["text"][1:-1]
    if len(label_in2["text"])==1 and label_in2["text"][0]=="0" and label_op["text"]=="":
        label_in2["text"]=label_in2["text"][1:-1]
        

    if label_in1["text"]!="" and len(label_in2["text"])<10 and label_op["text"]!="":
        label_in2["text"]+=num
    elif len(label_in1["text"])<10 and label_in2["text"]=="":
        label_in1["text"]+=num

def change_signal():
    if label_ans["text"]=='' and label_op["text"]!='':
        try:
            if label_in2["text"][0]!="-":
                label_in2["text"]= '-' + label_in2["text"]
            elif label_in2["text"][0]=="-":
                label_in2["text"]= label_in2["text"][1:]
        except:
            label_in2["text"]= '-'
    elif (label_in2["text"]=='' or label_in1["text"]==''):
        try:
            if label_in1["text"][0]!="-":
                label_in1["text"]= '-' + label_in1["text"]
            elif label_in1["text"][0]=="-":
                label_in1["text"]= label_in1["text"][1:]
        except:
            label_in1["text"]= '-' + label_in1["text"]
        


def special_op():
    if label_op["text"] == 'x'+u'\u00B2':  #x^2
        try:
            in1 = int(label_in1["text"])
        except ValueError:
            in1 = float(label_in1["text"])
        except:
            return "ERROR"
        finally:
            return str(in1**2)
        
    if label_op["text"] == u'\u221A'+"x": #sqrt
        try:
            in1 = int(label_in1["text"])
        except ValueError:
            in1 = float(label_in1["text"])
        except:
            return "ERROR"
        finally:
            return str(in1**0.5)
    
    if label_op["text"] == 'log': #log
        try:
            in1 = int(label_in1["text"])
        except ValueError:
            in1 = float(label_in1["text"])
        except:
            return "ERROR"
        finally:
            try:
                return str(math.log10(in1))
            except:
                return "ERROR"
    
def answer():
    if len(label_in1["text"])>0 and len(label_in2["text"])>0:
        if not("," in label_in1["text"] and label_in2["text"]): #not float
            try:
                in1 = int(label_in1["text"])
                in2 = int(label_in2["text"])
            except ValueError:
                in1 = float(label_in1["text"])
                in2 = float(label_in2["text"])
            if label_op["text"] == "+":
                ans = str(in1+in2)
            elif label_op["text"] == "-":
                ans = str(in1-in2)
            elif label_op["text"] == "X":
                ans = str(in1*in2)
            elif label_op["text"] == u'\u00F7': #division
                try:
                    ans = str(in1/in2)
                except:
                    ans = "ERROR"
            elif label_op["text"] == 'x'+u'\u207F': #x^n:
                ans = str(in1**in2)
    else:
        ans = special_op()
    ans = checkoverflow(ans)

    label_ans["text"] = ans
    
def checkoverflow(ans):
    try:
        if float(ans) >=100000000000:
            return "Overflow"
        elif len(ans)>13:
            label_approx["text"]="~"
            return ans[0:12]
        else:
            return ans
    except:
        return "ERROR"

def op(op):
    if label_ans["text"]=='' and label_in1["text"]!='':
        label_op["text"]=op
    elif label_ans["text"]!='' and label_in1["text"]!='':
        aux = label_ans["text"]
        clearall()
        if  aux !="Overflow":
            label_in1["text"]='0'
            label_in1["text"] = aux
            label_op["text"]=op
    else:
        pass
    
    if op=='x'+u'\u00B2' or op==u'\u221A'+"x"  or op=="log":
        answer()
        

root = tk.Tk()

canvas = tk.Canvas(root,height=600, width=420)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1,relheight=1)

num0_button = tk.Button(frame, text='0',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="0"))
num0_button.place(relx=0.4,rely=0.86,relwidth=0.2,relheight=0.14)
num1_button = tk.Button(frame, text='1',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="1"))
num1_button.place(relx=0.2,rely=0.72,relwidth=0.2,relheight=0.14)
num2_button = tk.Button(frame, text='2',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="2"))
num2_button.place(relx=0.4,rely=0.72,relwidth=0.2,relheight=0.14)
num3_button = tk.Button(frame, text='3',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="3"))
num3_button.place(relx=0.6,rely=0.72,relwidth=0.2,relheight=0.14)
num4_button = tk.Button(frame, text='4',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="4"))
num4_button.place(relx=0.2,rely=0.58,relwidth=0.2,relheight=0.14)
num5_button = tk.Button(frame, text='5',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="5"))
num5_button.place(relx=0.4,rely=0.58,relwidth=0.2,relheight=0.14)
num6_button = tk.Button(frame, text='6',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="6"))
num6_button.place(relx=0.6,rely=0.58,relwidth=0.2,relheight=0.14)
num7_button = tk.Button(frame, text='7',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="7"))
num7_button.place(relx=0.2,rely=0.44,relwidth=0.2,relheight=0.14)
num8_button = tk.Button(frame, text='8',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="8"))
num8_button.place(relx=0.4,rely=0.44,relwidth=0.2,relheight=0.14)
num9_button = tk.Button(frame, text='9',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="9"))
num9_button.place(relx=0.6,rely=0.44,relwidth=0.2,relheight=0.14)

pi_button = tk.Button(frame, text=u'\u213c',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="3.14159265"))
pi_button.place(relx=0.2,rely=0.3,relwidth=0.2,relheight=0.14)
e_button = tk.Button(frame, text='e',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="2.71828182"))
e_button.place(relx=0,rely=0.3,relwidth=0.2,relheight=0.14)

back_button = tk.Button(frame, text='<=',font="Courier",  fg = 'red',bd=4,command=lambda : backspace())
back_button.place(relx=0.6,rely=0.3,relwidth=0.2,relheight=0.14)
clear_button = tk.Button(frame, text='C',font="Courier",  fg = 'red',bd=4,command=lambda : clearall())
clear_button.place(relx=0.4,rely=0.3,relwidth=0.2,relheight=0.14)

sum_button = tk.Button(frame, text='+',font="Courier",  fg = 'red',bd=4,command=lambda:op(op="+"))
sum_button.place(relx=0.8,rely=0.72,relwidth=0.2,relheight=0.14)
sub_button = tk.Button(frame, text='-',font="Courier",  fg = 'red',bd=4,command=lambda:op(op="-"))
sub_button.place(relx=0.8,rely=0.58,relwidth=0.2,relheight=0.14)
mul_button = tk.Button(frame, text='X',font="Courier",  fg = 'red',bd=4,command=lambda:op(op="X"))
mul_button.place(relx=0.8,rely=0.44,relwidth=0.2,relheight=0.14)
div_button = tk.Button(frame, text=u'\u00F7',font="Courier",  fg = 'red',bd=4,command=lambda:op(op=u'\u00F7'))
div_button.place(relx=0.8,rely=0.3,relwidth=0.2,relheight=0.14)

singal_button = tk.Button(frame, text='+/-',font="Courier",  fg = 'red',bd=4, command=lambda:change_signal())
singal_button.place(relx=0.2,rely=0.86,relwidth=0.2,relheight=0.14)
coma_button = tk.Button(frame, text=',',font="Courier",  fg = 'red',bd=4,command=lambda:num_clicked(num="."))
coma_button.place(relx=0.6,rely=0.86,relwidth=0.2,relheight=0.14)
eq_button = tk.Button(frame, text='=',font="Courier",  fg = 'red',bd=4,command=lambda:answer())
eq_button.place(relx=0.8,rely=0.86,relwidth=0.2,relheight=0.14)


x2_button = tk.Button(frame, text='x'+u'\u00B2',font="Courier",  fg = 'red',bd=4,command=lambda:op(op='x'+u'\u00B2'))
x2_button.place(relx=0,rely=0.44,relwidth=0.2,relheight=0.14)
xsqrt_button = tk.Button(frame, text=u'\u221A'+"x",font="Courier",  fg = 'red',bd=4,command=lambda:op(op=u'\u221A'+"x"))
xsqrt_button.place(relx=0,rely=0.58,relwidth=0.2,relheight=0.14)
xn_button = tk.Button(frame, text='x'+u'\u207F',font="Courier",  fg = 'red',bd=4,command=lambda:op(op='x'+u'\u207F'))
xn_button.place(relx=0,rely=0.72,relwidth=0.2,relheight=0.14)
log_button = tk.Button(frame, text='log',font="Courier",  fg = 'red',bd=4,command=lambda:op(op='log'))
log_button.place(relx=0,rely=0.86,relwidth=0.2,relheight=0.14)


label_in1 = tk.Label(frame,text="",font=("Courier",30),fg='black')
label_in1.place(relx=0.2,rely=0,relwidth=0.9,relheight=0.1)
label_in2 = tk.Label(frame,text="",font=("Courier",30),fg='black')
label_in2.place(relx=0.2,rely=0.1,relwidth=0.9,relheight=0.1)
label_ans = tk.Label(frame,text="",font=("Courier",30),fg='red')
label_ans.place(relx=0.075,rely=0.2,relwidth=1,relheight=0.1)
label_approx = tk.Label(frame,text="",font=("Courier",30),fg='red')
label_approx.place(relx=0.075,rely=0.225,relwidth=0.05,relheight=0.05)
label_op = tk.Label(frame,text="",font=("Courier",30),fg='black')
label_op.place(relx=0,rely=0.1,relwidth=0.2,relheight=0.1)



root.mainloop()