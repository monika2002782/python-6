from tkinter import*
root=Tk()
Scrollbar=Scrollbar(root)
Scrollbar.pack(side=RIGHT,fill=Y)
m=Listbox(root,yscrollcommand=Scrollbar.set)
for line in range(100):
    m.insert(END,"livewire"+str(line))
m.pack(side=LEFT,fill=BOTH)
Scrollbar.config(command=m.yview)
root.mainloop() 