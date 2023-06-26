from  tkinter import *
from tkinter import ttk, messagebox
import requests 
import json
class  Conversor():
    __ventana: None
    __entry: None
    __resultado: None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("300x150")
        self.__ventana.title("Conversor de moneda")
        mainframe = ttk.Frame(self.__ventana,padding="1 1 2 1")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S)) 
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)
        mainframe["borderwidth"] = 1
        mainframe["relief"] = "flat"
        self.__entry = StringVar()
        self.__resultado = StringVar()
        self.__entry.trace("w",self.calcular)
        self.entryEntry = ttk.Entry(mainframe,width=8, textvariable=self.__entry)
        self.entryEntry.grid(column=2,row=1,sticky=(W))
        ttk.Label(mainframe,textvariable=str(self.__resultado)).grid(column=2,row=2,sticky=(W))
        ttk.Label(mainframe,text="Dolares").grid(column=3,row=1,sticky=(W))
        ttk.Label(mainframe, text="Es equivalente a").grid(row=2,column=1,sticky=(W))
        ttk.Label(mainframe,text="Pesos").grid(row=2,column=3,sticky=(W))
        ttk.Button(mainframe,text="Salir",command=self.__ventana.destroy).grid(column=3,row=3,sticky=(W))
        for child in mainframe.winfo_children():
            child.grid_configure(padx=2,pady=2)
        self.entryEntry.focus()
        self.__ventana.mainloop()
    def convertir(self):
        dolarventa = None
        complete_URL = "https://www.dolarsi.com/api/api.php?type=dolar"
        response = requests.get(complete_URL)
        data = response.json()
        dolarventa = data[0]['casa']['venta']
        dolarventa = dolarventa.replace(',','.')
        """for i in range(len(data)):
            if data[i]['casa']['nombre']=='Oficial':
                dolarventa = data[i]['casa']['venta']
                dolarventa = dolarventa.replace(',','.')"""#SERIA PARA BUSCAR EL DATO DENTRO DEL DICCIONARIO(DEBERIA SER CON WHILE)
        return float(dolarventa)
    def calcular(self,*args):
        try:    
            precio = self.convertir()
            dolar_cant = float(self.__entry.get())
            peso_cant = dolar_cant * precio
        except ValueError:
            messagebox.showerror(tittle="Error de tipo",message="Debe ingresar un Numero")
        return self.__resultado.set(round(peso_cant,2))
def testAPP():
    mi_app = Conversor()
if __name__ == "__main__":
    testAPP()



        
