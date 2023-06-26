import tkinter as tkinter
from tkinter import ttk, messagebox,font
from tkinter import *

class Iva(tkinter.Tk):
    __ingresado: None
    __iva:None
    __total:None
    def __init__(self):
        super().__init__()
        self.title("Calculadora IVA")
        #self.geometry('170x160')
        self.resizable(0,0)
        #self.config(bg='aquamarine2')
        self.__ingresado = StringVar()
        self.__iva = StringVar()
        self.__total = StringVar()
        self.valor=IntVar()
        tkinter.Label(self,text="Calculo de IVA",bg='light sky blue').grid(column=0,row=0,columnspan=4,sticky=('nsew'))
        tkinter.Label(self,text="Precio sin IVA").grid(column=1,row=2,sticky=(W))
        self.ingresadoEntry = tkinter.Entry(self,width=14,textvariable=self.__ingresado)
        self.ingresadoEntry.grid(column=2,row=2,sticky=(W))
        tkinter.Radiobutton(self,text="IVA 21%",value=0,variable=self.valor,command=self.calculaIva).grid(column=1,row=3,sticky=(W))
        tkinter.Radiobutton(self,text="IVA 10,5%",value=1,variable=self.valor,command=self.calculaIva).grid(column=1,row=4,sticky=(W))
        tkinter.Label(self,text="IVA").grid(column=1,row=5,sticky=(N,W,E,S))
        tkinter.Label(self,text="Precio con IVA").grid(column=1,row=6,sticky=(N,W,E,S))
        tkinter.Label(self,textvariable=self.__iva).grid(column=2,row=5,sticky=((W)))
        tkinter.Label(self,textvariable=self.__total).grid(column=2,row=6,sticky=((W)))
        tkinter.Button(self,text='Calcular',command=self.calcular,bg='SeaGreen1',width='8').grid(column=1,row=7,sticky=(W))
        tkinter.Button(self,text='Salir',command=self.destroy,bg='PaleVioletRed1',width='8').grid(column=2,row=7,sticky=(E))
        self.ingresadoEntry.focus()
        self.mainloop()
    def calculaIva(self):
        if self.ingresadoEntry.get()!=None:
            if self.valor.get()==0:
                porcentaje=float(21/100)*float(self.ingresadoEntry.get()) 
            elif self.valor.get()==1:
                porcentaje=float(10.5/100)*float(self.ingresadoEntry.get())  
            return porcentaje 

    def calcular(self):
        try:
            self.__iva.set(round(self.calculaIva(),2))
            resultado = float(float(self.ingresadoEntry.get())+float(self.calculaIva()))  
            self.__total.set(round(resultado,2))
        except:
             messagebox.showerror(title='Eror de valor',message='Los valores ingresados deben ser numericos')    

def testAPP():
        mi_app = Iva()
if __name__ == "__main__":
     testAPP()
        
        
        
        
        

