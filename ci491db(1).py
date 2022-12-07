from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 900
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Link", "Name", "Email"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Link', text="Link", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Email', text="Email", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('output.csv') as f:
    # reader = csv.DictReader(f, delimiter=',')
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if len(row) == 0:
            continue
        link: str = row[0]
        name: str = row[1]
        email: str = row[2]
        # specialty: str = row[3]
        tree.insert("", 0, values=(link, name, email))
        
root = Tk()
Searchbar = Entry(root)
Searchbar.pack()
SearchString = StringVar(Searchbar, "")
Searchbar.config(textvariable = SearchString)

SearchResultBar = Label(root)
SearchResultBar.pack()

def DisplaySearchResult(event):
  Keyword = SearchString.get()
  # write some code to search your csv data and get a string to describe the search result, which we'll call SearchResult
  SearchString.set(SearchResult)

Searchbar.bind('<Return>', DisplaySearchResult, add = '+')
Searchbar.bind('<FocusOut>', DisplaySearchResult, add = '+')

def generatecode(self):
    pass  # Do stuff here


#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()
