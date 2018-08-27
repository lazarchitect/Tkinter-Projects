from requests import get
from bs4 import BeautifulSoup
from tkinter import Tk, Label
from PIL import ImageTk, Image
from os import remove

#GATHER DATA

cardName = input("Name a card: >>")
if cardName == "quit": exit() #cuz im lazy

cardPageHTML = get("http://magiccards.info/query?q=" +  cardName  + "&v=card&s=cname").content
bsObject = BeautifulSoup(cardPageHTML, "html.parser")
mainTable = bsObject.find("table", {"style":"margin: 0 0 0.5em 0;"})
try:
	imageRow = mainTable.find("tr")
	imageData = imageRow.find("td",{"width":"312"})
	image = imageData.find("img")
	imageURL = image.get("src")
	imageEncoding = get("https://magiccards.info"+ imageURL).content #the final product
except AttributeError:
	print("No card found by that name.")
	exit()

#################################################################################################
#GET THE IMAGE, SAVE TO FILE

path = cardName +".jpg"
f = open(path,"wb")
f.write(imageEncoding)#Find the image online and save it to f
f.close()

#################################################################################################
#INSTANTIATE WINDOW, POPULATE IT, THEN DELETE THE FILE AFTER

window = Tk()
image = ImageTk.PhotoImage(Image.open(path))
Label(window, image = image).pack()
window.mainloop()
remove(path)