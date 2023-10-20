from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import qrcode
import qrcode.image.svg
from qrcode.image.pure import PyPNGImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

root = Tk()
root.title("QR Generator")
root.geometry('355x550+600+100')
root.resizable(False, False)

data = StringVar()
style = StringVar()

def showQR():
	openqr = Image.open(f"untitled.png")
	resize_image = openqr.resize((290,290))
	test = ImageTk.PhotoImage(resize_image)
	l1 = Label(myframe,image=test)
	l1.image = test
	l1.place(x=0,y=0)

def createQR():
	if len(e1.get()) < 1:
		messagebox.showerror("Error", "Please enter a text!")
	else:
		qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,
        border=4,)
		qr.add_data(e1.get())
		qrStyle = e2.get()
		if qrStyle == 'Radial':
			image = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
			image.save(f"untitled.png")
			showQR()
		elif qrStyle == 'Round':
			image = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
			image.save(f"untitled.png")
			showQR()
		elif qrStyle == 'Custom Color':
			newWindow = Toplevel(root)
			newWindow.geometry("350x150+1000+100")
			newWindow.title("Custom Color")

			back = StringVar()
			fill = StringVar()

			Label(newWindow, text="Background Color: ", font="Helvetica 13").place(x=5,y=5)
			Label(newWindow, text="Fill Color: ", font="Helvetica 13").place(x=5,y=35)
			e3 = Entry(newWindow, textvariable=back, font="Helvetica 13")
			e3.place(x=150,y=5)
			e4 = Entry(newWindow, textvariable=fill, font="Helvetica 13")
			e4.place(x=150,y=35)

			def create_QR():
				if len(e3.get()) < 1:
					messagebox.showerror("error", "Please enter a background color!")
				elif len(e4.get()) < 1:
					messagebox.showerror("error", "Please enter a fill color!")
				else:
					qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10, border=4,)
					qr.add_data(e1.get())
					image = qr.make_image(back_color=(e3.get()), fill_color=(e4.get()))
					image.save(f"untitled.png")
					showQR()
					newWindow.destroy()

			Button(newWindow, text="Create QR", font="helvetica 11", width=10, relief="groove", command=create_QR).place(x=150,y=80)

			# image = qr.make_image(back_color=(e3.get()), fill_color=(e4.get()))
			# image.save(f"{e1.get()}.png")
		elif qrStyle == '' or qrStyle == 'None':
			image = qrcode.make(e1.get(), image_factory=PyPNGImage)
			image.save(f"untitled.png")
			showQR()

def deleteQR():
	os.remove(f"untitled.png")
	e1.delete(0, 'end')

myframe = Frame(root, bg='white', width=290, height=290)
myframe.place(x=35,y=230)

# img = ImageTk.PhotoImage(Image.open("qr.png"))
# panel = Label(myframe, image = img)
# panel.place(x=0, y=0)

e1 = Entry(root, textvariable=data, width=30, font="helvetica 13")
# e1.insert(0, 'try')
e1.place(x=40, y=40)
e2 = ttk.Combobox(root, width=28, textvariable=style, font="helvetica 13", values=('Radial', 'Round', 'Custom Color'))
e2.set('None')
e2.place(x=40, y=100)
Label(root, text="Text here:", font="helvetica 15").place(x=130, y=70)
Label(root, text="QR Style:", font="helvetica 15").place(x=130, y=130)
Label(myframe, text="QR will display here", font="helvetica 15", bg='white').place(x=50, y=120)
Button(root, text="Generate QR", font="helvetica 13", width=12, relief="groove", command=createQR).place(x=40, y=170)
Button(root, text="Delete QR", font="helvetica 13", width=12, relief="groove", command=deleteQR).place(x=200, y=170)

# createQR()
mainloop()