from http import client
import json
import os
from textwrap import indent
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

DATA ={
    ('Atropine sulfate','Injectable','200','1 mg/ ml','9500'),
    ('Diazépam','Injectable','500','10 mg/ ml','10500'),
    ('Midazolam','Injectable','100','5 mg/ ml','7460'),
    ('Diclofenac','Injectable','75 mg/ ml','421','2460'),
    ('Ibuprofène','Comprimé','520','400 mg','5620'),
}        


def approvisonnement():
    pharmacy = Tk()
    pharmacy.geometry("900x900")
    pharmacy.title("PHARMACIE SAINT YVANN")
    pharmacy.configure(bg="grey")
    titre= Label(pharmacy,text="PHARMACIE SAINT YVANN", bg="orange")
    titre.pack(padx=70, ipady=15)   
    
    ajout= Label(pharmacy, text="veuillez entrez le nom du médicament").pack(ipadx=20,pady=10)
    entre=Entry(pharmacy)
    entre.pack(ipadx=30, pady=20, ipady=5)
    forme= Label(pharmacy, text="forme du médicament").pack(ipadx=20, pady=10)
    fort=Entry(pharmacy)
    fort.pack(ipadx=30, pady=20,ipady=5)
    qte= Label(pharmacy, text="veuillez entrez la quantité").pack(ipadx=20, pady=10)
    enter=Entry(pharmacy)
    enter.pack(ipadx=30, pady=20,ipady=5)
    dosage= Label(pharmacy, text="dosage").pack(ipadx=20, pady=10)
    dos= Entry(pharmacy)
    dos.pack(ipadx=30, pady=20,ipady=5)
    prix= Label(pharmacy,text="prix du médicament").pack(ipadx=20, pady=10)
    prixx= Entry(pharmacy)
    prixx.pack(ipadx=30, pady=20,ipady=5)

    
    def ter():
        teflan =[]
        donnees = {
        "medicament": entre.get(),
        "forme": fort.get(),
        "quantite": enter.get(),
        "Dosage": dos.get(),
        "prix": prixx.get()
        }
        
        teflan.append(donnees)
        print(teflan)

        
        try:
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/luck.json", "r") as f:
                json.load(f)
        except json.decoder.JSONDecodeError:
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/luck.json", "w") as f:
                json.dump(teflan, f, indent=4)
        
        else:
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/luck.json", "r") as f:
                test = json.load(f)
            test.append(donnees)
            
                
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/luck.json", "w") as f:
                    json.dump(test, f, indent=4)
        if entre.get()=="" or fort.get()=="" or enter.get()=="" or dos.get()=="" or prixx.get()=="":
            messagebox.showerror("error","tout les champs sont requis!")

            
        entre.delete(0, END)
        fort.delete(0, END)
        enter.delete(0, END)
        dos.delete(0, END)
        prixx.delete(0, END)
    
    buttone=Button(pharmacy,text="validé",command=ter,highlightthickness=10)
    buttone.pack(ipadx=25,pady=40, ipady=30)
    
    pharmacy.mainloop()

   

def achat_medicament():
    pharmacy = Tk()
    pharmacy.geometry("500x500")
    pharmacy.title("PHARMACIE SAINT YVANN")
    pharmacy.configure(bg="grey")
    titre= Label(pharmacy,text="PHARMACIE SAINT YVANN", bg="orange")
    titre.pack(padx=70, ipady=15)

    nom= Label(pharmacy, text="nom du client:")
    nom.pack(padx=35, pady=5)
    e1= Entry(pharmacy)
    e1.pack()
    moi= e1.get()

    médoc= Label(pharmacy, text="nom du médicament:")
    médoc.pack(padx=35, pady=5)
    e2= Entry(pharmacy)
    e2.pack()
    lol= e2.get()

    résidence= Label(pharmacy, text="adresse:")
    résidence.pack(padx=35, pady=5)
    e3= Entry(pharmacy)
    e3.pack()
    cool=e3.get()
    
    def save_informations():
        pardon=[]
        
        richard={
            "client": moi,
            "medoc":lol,
            "adresse": cool,
        }
        pardon.append(richard)
        print(pardon)
        try:
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/test.json", "r") as f:
                json.load(f)
        except json.decoder.JSONDecodeError:
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/test.json", "w") as f:
                json.dump(pardon, f, indent=4)
        
        
        else:
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/pharmacie-SAINT-YVANN/test.json", "r") as f:
                merci=json.load(f)
            pardon.append(richard)
        
            with open("/Users/imac_29/Desktop/PHARMACIE SAINT YVANN/test.json", "w") as f:
                json.dump(merci, f, indent=4)
        if client.get()=="" or médoc.get()=="" or résidence.get()=="":
            messagebox.showwarning("attention","tout les champs sont requis")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END) 

    
         
    valide= Button(pharmacy,text="validé",command=save_informations)
    valide.pack(padx=10,pady=20)

    pharmacy.mainloop()

def stocks_credits():
    pharmacy = Tk()
    pharmacy.geometry("500x500")
    pharmacy.title("PHARMACIE SAINT YVANN")
    pharmacy.configure(bg="grey")
    titre= Label(pharmacy,text="PHARMACIE SAINT YVANN", bg="orange")
    titre.pack(padx=70, ipady=15)
    my_tree = ttk.Treeview(pharmacy)

    treeframe = LabelFrame(pharmacy,width=1200,height=1000)
    treeframe.configure(bg="red")
    treeframe.pack(pady=10,padx=10)

    column = ["Nom du médicament","forme","Qte_livrée","dosage","Prix unitaire"]



    myTree = ttk.Treeview(treeframe,height=200,column=column)
    myTree.pack(fill="both")
    myTree['show']='headings'
    for each in column:
      myTree.column(each,width=90)
      myTree.heading(each,text=each.capitalize())
    for each in DATA:
      myTree.insert("",END,values=each)
    
    pharmacy.mainloop()

def quitter():
    messagebox.showinfo("congratulations", "fin du programme")

def formsend():
    messagebox.showinfo("statut de l'enregistrement ",'validé')