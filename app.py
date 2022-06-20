from tkinter import *
import tkinter
import db

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.database = db.Database()
        self.album_list = Listbox(self, height=8, width=50, border=0, exportselection=False)

    def add(self):
        if artist_text.get()!="" and album_text.get()!="" and year_text.get()!="" and genre_text.get()!="":
            self.database.add_album(artist_text.get(),album_text.get(),year_text.get(), genre_text.get())
            self.populate_albums()

    def remove(self):
        self.remove(selected_album)
        self.populate_albums()
        self.clear()

    def update(self):
        self.database.update(selected_album, artist_text.get(), album_text.get(), year_text.get(), genre_text.get())
        self.populate_albums()

    def clear(self):
        artist_text.set("")
        album_text.set("")
        year_text.set("")
        genre_text.set("")
        artist_entry.focus_set()

    def populate_albums(self):
        self.album_list.delete(0,END)
        for row in self.database.fetch_albums():
            self.album_list.insert(END,row)
    
    def select_album(self, event):        
        update_btn["state"] = "normal"
        global selected_album       
        index = self.album_list.curselection()[0]   
        
        selected_album = self.album_list.get(index)     
        selected_album = selected_album.split('-')
        
        artist_entry.delete(0,END)
        artist_entry.insert(END, selected_album[0])
        album_entry.delete(0,END)
        album_entry.insert(END, selected_album[1])
        year_entry.delete(0,END)
        year_entry.insert(END, selected_album[2])
        genre_entry.delete(0,END)
        genre_entry.insert(END, selected_album[3])

    def update_app(self):
        if artist_text.get()!="" and album_text.get()!="" and year_text.get()!="" and genre_text.get()!="":
            add_btn["state"] = "normal"
        else:
            add_btn["state"] = "disabled"
        is_selected = self.album_list.curselection()   
        if is_selected:
            remove_btn["state"] = "normal"
        else:
            remove_btn["state"] = "disabled"
        app.after(100, self.update_app)

app = App()
artist_text = StringVar()
artist_label = Label(app, text='Artist', font=('bold',14), pady=20)
artist_label.grid(row=0,column=0, sticky=W)
artist_entry = Entry(app, textvariable=artist_text)
artist_entry.grid(row=0, column=1)
artist_entry.focus_set()

album_text = StringVar()
album_label = Label(app, text='Album', font=('bold',14))
album_label.grid(row=0,column=2, sticky=W)
album_entry = Entry(app, textvariable=album_text)
album_entry.grid(row=0, column=3)

year_text = StringVar()
year_label = Label(app, text='Year', font=('bold',14))
year_label.grid(row=1,column=0, sticky=W)
year_entry = Entry(app, textvariable=year_text)
year_entry.grid(row=1, column=1)

genre_text = StringVar()
genre_label = Label(app, text='Genre', font=('bold',14))
genre_label.grid(row=1,column=2, sticky=W)
genre_entry = Entry(app, textvariable=genre_text)
genre_entry.grid(row=1, column=3)

#Listbox
app.album_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

#Scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3,column=3)
app.album_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=app.album_list.yview)

#Bind select
app.album_list.bind('<<ListboxSelect>>', app.select_album)

#Buttons
add_btn = Button(app, text='Add Album', width=12, command=app.add)
add_btn.grid(row=2,column=0, pady=20)
add_btn["state"] = "disabled"

remove_btn = Button(app, text='Remove Album', width=12, command=app.remove)
remove_btn.grid(row=2,column=1)
remove_btn["state"] = "disabled"

update_btn = Button(app, text='Update Album', width=12, command=app.update)
update_btn.grid(row=2,column=2)
update_btn["state"] = "disabled"

clear_btn = Button(app, text='Clear', width=12, command=app.clear)
clear_btn.grid(row=2,column=3)

app.title("Album DB")
app.geometry("700x350")

app.populate_albums()
app.update_app()

app.mainloop()
