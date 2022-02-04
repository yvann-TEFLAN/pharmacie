from cgitb import text
from tkinter import*
from tkinter import font
# from PIL import ImageTk, Image
import fonction


pharmacy = Tk()
pharmacy.geometry("1000x700")
pharmacy.title("PHARMACIE SAINT YVANN")
pharmacy.configure(bg="#cce7e8")
titre= Label(pharmacy,text="PHARMACIE SAINT YVANN",relief=SUNKEN, bg="#c9c916", font=("Arial",30),highlightthickness=10)
titre.place(x=120,y=30, width=700, height=100)
# img= ImageTk.PhotoImage(Image.open("acceuil-png.jpeg"))
# imglabel=Label(pharmacy, image=img,width=300, height=200).pack()
Frame= LabelFrame(pharmacy, bg="#2596be",highlightthickness=10)
Frame.place(x=150,y=200,width=600)

btn1 = Button(Frame, text="approvisionnements", width=10, command=fonction.approvisonnement)
btn2= Button(Frame, text="achats de médicaments",width=10, command=fonction.achat_medicament)
btn3= Button(Frame, text="etats des stocks et crédits",width=10, command=fonction.stocks_credits)
btn4= Button(Frame,text="quitter", command=pharmacy.quit)

btn1.pack(ipadx=75, ipady=15,pady=10)
btn2.pack(ipadx=75, ipady=15,pady=10)
btn3.pack(ipadx=75, ipady=15,pady=10)
btn4.pack(ipadx=75, ipady=15,pady=10)

#Frame.pack(i0, pady=10)

pharmacy.mainloop()