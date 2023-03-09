import os
import webbrowser as wb

mode = input(
    "Select Subject:\n\t[1] Pure 1\n\t[2] Information Technology\n\t[3] Computer Science\n\n> ")

if mode == "1":
    wb.open("file:///D:/Documents/education/A%20Level/Maths/Pure%201/Resources/Pure%20Maths%201%20Worked%20Solution.pdf")
    wb.open_new_tab(
        "file:///D:/Documents/education/A%20Level/Maths/Pure%201/Resources/Pure%20Maths%20Coursebook.pdf")
    wb.open_new_tab(
        "file:///D:/Documents/education/A%20Level/Maths/Pure%201/Resources/Pure%20Maths%20Coursebook.pdf")

elif mode == "2":
    wb.open("file:///D:/Documents/education/A%20Level/Information%20Technology/Information%20Technology.pdf")
    wb.open_new_tab(
        "https://docs.google.com/document/d/1roP3jHgoRlDFK6GnRzNLtVaCjFZbN0edxrA5rCiJhR8/edit")

elif mode == "3":
    wb.open(
        "file:///D:/Documents/education/A%20Level/Computer%20Science/CIE%20Computer%20Science%20[new].pdf")

else:
    input("Exitting Study Mode\n\nPress [Enter] to exit.")
