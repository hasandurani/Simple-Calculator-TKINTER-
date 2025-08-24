import tkinter as tk
root=tk.Tk()
root.geometry("320x400")
root.title("Simple Calculator")
root.config(bg="black")
entry= tk.Entry(root,font=("Arial",20),justify="right")
entry.grid(row=0,column=0,columnspan=4,pady=10,padx=9)
buttens=[
        ['7','8','9','+'],
         ['4','5','6','-'],
         ['1','2','3','x'],
         ['0','C','=','÷']
]
editB=[]
for row in range(4):
    for col in range(4):
        btn=tk.Button(root,text=(buttens[row][col]),font=("Arial",14,'bold'),width=5,height=2,command= lambda val = buttens[row][col]:btn_click(val))
        btn.grid(row=row+1,column=col,padx=5,pady=5)
        editB.append(btn)
for btn in editB:
    text=btn['text']
    if text in '0123456789':
        btn.config(fg='white',bg='gray')
    elif text in '÷+-x':
        btn.config(fg='black',bg='yellow')
    elif text in "C":
        btn.config(fg='white',bg='red')
    elif text in '=':
        btn.config(fg='white',bg='green')
def btn_click(value):
    if value=='C':
        entry.delete(0,tk.END)
    elif value== '=':
        try:
            result= eval(entry.get().replace('x','*').replace('÷','/'))
            entry.delete(0,tk.END)
            entry.insert(tk.END,result)
        except:
            entry.delete(0,tk.END)
            entry.insert(tk.END,'ERROR')
            entry.config(fg='red')
    else:
        entry.config(fg='black')
        entry.insert(tk.END,value)
root.mainloop()
