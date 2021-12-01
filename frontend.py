import backend
from tkinter import *
from tkinter import messagebox
import re

window = Tk()

## Functions ##
def select_row(event):
    global selected_tuple
    selection = result_list.curselection()
    if len(selection) > 0:
        index = selection[0]
        selected_tuple = result_list.get(index)
    title_insertBox.delete(0, END)
    author_insertBox.delete(0, END)
    year_insertBox.delete(0, END)
    isbn_insertBox.delete(0, END)
    title_insertBox.insert(END, selected_tuple[1])
    author_insertBox.insert(END, selected_tuple[2])
    year_insertBox.insert(END, selected_tuple[3])
    isbn_insertBox.insert(END, selected_tuple[4])


def view_command():
    result_list.delete(0, END)
    for row in backend.view():
        result_list.insert(END, row)


def search_command():
    if not validate_entries():
        return
    result_list.delete(0, END)
    rows = backend.search(
        title_value.get(), author_value.get(), year_value.get(), isbn_value.get()
    )
    for row in rows:
        result_list.insert(END, row)


def add_command():
    if not validate_entries():
        return
    backend.insert(
        title_value.get(), author_value.get(), year_value.get(), isbn_value.get()
    )
    view_command()


def update_command():
    if not validate_entries():
        return
    backend.update(
        selected_tuple[0],
        title_value.get(),
        author_value.get(),
        year_value.get(),
        isbn_value.get(),
    )
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


def validate_entries():
    def isbn_check(isbn):
        check_digit = int(isbn[-1])
        match = re.search(r"(\d)-(\d{3})-(\d{5})", isbn[:-1])
        if not match:
            return False
        digits = match.group(1) + match.group(2) + match.group(3)
        result = 0
        for i, digit in enumerate(digits):
            result += (i + 1) * int(digit)
        return True if (result % 11) == check_digit else False

    title_flag = (title_value.get().isalnum()) or (title_value.get() == "")
    if not title_flag:
        messagebox.showerror("error", "invalid title")
    author_flag = author_value.get().isalnum() or author_value.get() == ""
    if not author_flag:
        messagebox.showerror("error", "invalid author name")
    year_flag = year_value.get().isdigit() or year_value.get() == ""
    if not year_flag:
        messagebox.showerror("error", "invalid year")
    isbn_flag = isbn_check(isbn_value.get()) or isbn_value.get() == ""
    if not isbn_flag:
        messagebox.showerror("error", "invalid isbn")
    return title_flag and author_flag and year_flag and isbn_flag


## Labels ##
title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_value = Label(window, text="ISBN")
isbn_value.grid(row=1, column=2)

## Entry boxes ##
title_value = StringVar()
title_insertBox = Entry(window, textvariable=title_value)
title_insertBox.grid(row=0, column=1)

year_value = StringVar()
year_insertBox = Entry(window, textvariable=year_value)
year_insertBox.grid(row=1, column=1)

author_value = StringVar()
author_insertBox = Entry(window, textvariable=author_value)
author_insertBox.grid(row=0, column=3)

isbn_value = StringVar()
isbn_insertBox = Entry(window, textvariable=isbn_value)
isbn_insertBox.grid(row=1, column=3)

## Buttons ##
viewAll_button = Button(window, text="View All", width=12, command=view_command)
viewAll_button.grid(row=2, column=3)

searchEntry_button = Button(
    window, text="Search Entry", width=12, command=search_command
)
searchEntry_button.grid(row=3, column=3)

addEntry_button = Button(window, text="Add Entry", width=12, command=add_command)
addEntry_button.grid(row=4, column=3)

update_button = Button(window, text="Update Selected", width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete Selected", width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12, command=window.destroy)
close_button.grid(row=7, column=3)

## ListBox ##
result_list = Listbox(window, height=6, width=35)
result_list.grid(row=2, column=0, rowspan=6, columnspan=2)

## scroll_bar ##
scroll_bar = Scrollbar(window, orient="vertical")
scroll_bar.grid(row=2, column=2, rowspan=6)

result_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=result_list.yview)

result_list.bind("<<ListboxSelect>>", select_row)

window.mainloop()
