from tkinter import *


window = Tk()

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
viewAll_button = Button(window, text="View All", width=12)
viewAll_button.grid(row=2, column=3)

searchEntry_button = Button(window, text="Search Entry", width=12)
searchEntry_button.grid(row=3, column=3)

addEntry_button = Button(window, text="Add Entry", width=12)
addEntry_button.grid(row=4, column=3)

update_button = Button(window, text="Update", width=12)
update_button.grid(row=5, column=3)

delete_button = Button(window, text="Delete", width=12)
delete_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=12)
close_button.grid(row=7, column=3)

## ListBox ##
resultList = Listbox(window, height=6, width=35)
resultList.grid(row=2, column=0, rowspan=6, columnspan=2)

## Scrollbar ##
scrollbar = Scrollbar(window, orient="vertical")
scrollbar.grid(row=2, column=2, rowspan=6)

resultList.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=resultList.yview)

window.mainloop()
