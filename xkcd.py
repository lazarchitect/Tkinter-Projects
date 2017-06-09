from requests import get
from bs4 import BeautifulSoup
from tkinter import Tk, Label
from PIL import ImageTk, Image
from os import remove

text = BeautifulSoup(get("https://xkcd.com").content, "html.parser").get_text()
substring = "Permanent link to this comic: https://xkcd.com/"
i = text.index(substring) + len(substring)
substring2 = text[i:i+11]
maxComicIndex = int(''.join(x for x in substring2 if x.isdigit())) #wont work forever, but should work for a good number of millenia

while(1):
	try:
		string = input("Enter the index of the comic you would like to read: \n>>")
		if(string == "quit"): exit()
		n = int(string)
		if(n > maxComicIndex or n < 0): raise IndexError
		break
	except IndexError: print("Bad input, not within the number of comics.")
	except ValueError: print("Bad input, not a valid integer.")	

URL = "http://xkcd.com/{number}".format(number = n)
page = BeautifulSoup(get(URL).content, "html.parser")
comic = page.find("div",{"id":"comic"})
img = comic.find("img")
alt = img["alt"]
title = img["title"]
imgURL = "http:" + img['src']
##############################################################################
path = "comic.png"
f = open(path,"wb")
f.write(get(imgURL).content)#Find the image online and save it to f
f.close()
##############################################################################
window = Tk()
image = ImageTk.PhotoImage(Image.open(path))
Label(window, font = ("Arial", 32), text = alt).pack()
Label(window, image = image).pack()
Label(window, text = title, wraplength = 500).pack()
window.mainloop()

remove(path)