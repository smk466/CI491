from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Python - Search CSV")
fram = Frame(root)
width = 900
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

Searchbar = Entry(root)
Searchbar.pack()
SearchString = StringVar(Searchbar, "")
Searchbar.config(textvariable = SearchString)

SearchResultBar = Label(root)
SearchResultBar.pack()

butt = Button(fram, text='Find') 
butt.pack(side=RIGHT)
fram.pack(side=TOP)

def DisplaySearchResult(event):
    Keyword = SearchString.get()
    # write some code to search your csv data and get a string to describe the search result, which we'll call SearchResult

    NewTableMargin = Frame(root, width=100)
    NewTableMargin.pack(side=TOP)
    newscrollbarx = Scrollbar(NewTableMargin, orient=HORIZONTAL)
    newscrollbary = Scrollbar(NewTableMargin, orient=VERTICAL)
    resultTree = ttk.Treeview(NewTableMargin, columns=("Link", "Name", "Email", "Specialty"), height=400, selectmode="extended", yscrollcommand=newscrollbary.set, xscrollcommand=newscrollbarx.set)
    newscrollbary.config(command=resultTree.yview)
    newscrollbary.pack(side=RIGHT, fill=Y)
    newscrollbarx.config(command=resultTree.xview)
    newscrollbarx.pack(side=BOTTOM, fill=X)
    resultTree.heading('Link', text="Link", anchor=W)
    resultTree.heading('Name', text="Name", anchor=W)
    resultTree.heading('Email', text="Email", anchor=W)
    resultTree.heading('Specialty', text="Specialty", anchor=W)
    resultTree.column('#0', stretch=NO, minwidth=0, width=0)
    resultTree.column('#1', stretch=NO, minwidth=0, width=200)
    resultTree.column('#2', stretch=NO, minwidth=0, width=200)
    resultTree.column('#3', stretch=NO, minwidth=0, width=300)
    resultTree.pack()

    with open('output.csv') as f:
        # reader = csv.DictReader(f, delimiter=',')
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if len(row) == 0:
                continue
            if row[0] == Keyword or row[1] == Keyword or row[2] == Keyword or row[3] == Keyword:
                link: str = row[0]
                name: str = row[1]
                email: str = row[2]
                specialty: str = row[3]
                resultTree.insert("", 0, values=(link, name, email, specialty))

    SearchString.set(resultTree)

    # Step 1: Search through tree with getter and Keyword
    # Step 2: Set SearchResult into a new treeview
    # Step 3: Display it

    # print(tree.get_children)

    # for child in tree.get_children():
    #     if Keyword.lower() in tree.item(child)['values'].lower():
    #         resultTree.insert("", 0, values=(link, name, email, specialty))

Searchbar.bind('<Return>', DisplaySearchResult, add = '+')
Searchbar.bind('<FocusOut>', DisplaySearchResult, add = '+')
print(SearchString)

if __name__ == '__main__':
    root.mainloop()