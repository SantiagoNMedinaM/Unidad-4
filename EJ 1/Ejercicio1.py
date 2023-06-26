from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
class Aplicacion(object):
    __ventana=None
    __cantA=None
    __cantV=None
    __cantE=None
    __baseA=None
    __baseV=None
    __baseE=None
    __actualA=None
    __actualV=None
    __actualE=None
    __resultado=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("400x250")
        self.__ventana.title("Calculadora IPC")
        mainframe = ttk.Frame(self.__ventana, padding="5 10 5 10")
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe.rowconfigure(0,weight=1)
        mainframe['borderwidth'] = 1
        mainframe['relief'] = 'flat'
        self.__cantA = StringVar()
        self.__cantV = StringVar()
        self.__cantE = StringVar()
        self.__baseA = StringVar()
        self.__baseV = StringVar()
        self.__baseE = StringVar()
        self.__actualA = StringVar()
        self.__actualV = StringVar()
        self.__actualE = StringVar()
        self.__resultado = StringVar()
        ttk.Label(mainframe,text="Item").grid(column=1,row=1,sticky=(W))
        ttk.Label(mainframe,text="Cantidad").grid(column=2,row=1,sticky=(W))
        ttk.Label(mainframe,text="Precio Año Base").grid(column=3,row=1,sticky=(W))
        ttk.Label(mainframe,text="Precio año actual").grid(column=4,row=1,sticky=(W))
        ttk.Label(mainframe,text="Vestimenta").grid(column=1,row=2,sticky=(W))
        ttk.Label(mainframe,text="Alimentos").grid(column=1,row=3,sticky=(W))
        ttk.Label(mainframe,text="Educacion").grid(column=1,row=4,sticky=(W))
        ttk.Label(mainframe,text="IPC %").grid(column=1,row=7,sticky=(W))
        ttk.Label(mainframe,text="%").grid(column=2,row=7,sticky=(W))
        self.cantVEntry = ttk.Entry(mainframe,width=12,textvariable=self.__cantV)
        self.cantVEntry.grid(column=2,row=2,sticky=(W))    
        self.cantAEntry = ttk.Entry(mainframe,width=12,textvariable=self.__cantA)   
        self.cantAEntry.grid(column=2,row=3,sticky=(W))      
        self.cantEEntry = ttk.Entry(mainframe,width=12,textvariable=self.__cantE)
        self.cantEEntry.grid(column=2,row=4,sticky=(W))    
        self.baseVEntry = ttk.Entry(mainframe,width=12,textvariable=self.__baseV)
        self.baseVEntry.grid(column=3,row=2,sticky=(W))   
        self.baseAEntry = ttk.Entry(mainframe,width=12,textvariable=self.__baseA)
        self.baseAEntry.grid(column=3,row=3,sticky=(W))    
        self.baseEEntry = ttk.Entry(mainframe,width=12,textvariable=self.__baseE)
        self.baseEEntry.grid(column=3,row=4,sticky=(W))   
        self.actualVEntry = ttk.Entry(mainframe,width=12,textvariable=self.__actualV)
        self.actualVEntry.grid(column=4,row=2,sticky=(W))   
        self.actualAEntry = ttk.Entry(mainframe,width=12,textvariable=self.__actualA)
        self.actualAEntry.grid(column=4,row=3,sticky=(W))   
        self.actualEEntry = ttk.Entry(mainframe,width=12,textvariable=self.__actualE)
        self.actualEEntry.grid(column=4,row=4,sticky=(W))   
        ttk.Button(mainframe,text="Calcular IPC",command=self.calcular).grid(column=2,row=6,sticky=(W))
        ttk.Button(mainframe,text="Salir",command=self.__ventana.destroy).grid(column=4,row=6,sticky=(W))
        ttk.Label(mainframe,textvariable=str(self.__resultado)).grid(column=1,row=7,sticky=(E))
        for child in mainframe.winfo_children():
            child.grid_configure(padx=8,pady=8)
        self.cantVEntry.focus()
        self.__ventana.mainloop()
    def calcular(self):
        try:
            cantv=int(self.cantVEntry.get())
            canta=int(self.cantAEntry.get())
            cante=int(self.cantEEntry.get())
            basev=float(self.baseVEntry.get())
            basea=float(self.baseAEntry.get())
            basee=float(self.baseEEntry.get())
            actualv=float(self.actualVEntry.get())
            actuala=float(self.actualAEntry.get())
            actuale=float(self.actualEEntry.get())
        except ValueError:
            messagebox.showerror(title='Error de tipo', message='Debe ingresar un valor numérico')
        
        costo_base = (canta * basea) + (cantv * basev) + (cante * basee)
        costo_actual = (canta * actuala) + (cantv * actualv) + (cante * actuale)

        ipc = (costo_actual / costo_base)
        ipc = ipc - int(ipc)  # Quitar la parte entera
        ipc=ipc*100
        self.__resultado.set(round(ipc, 2))
              
def testAPP():
        mi_app = Aplicacion()
if __name__ == "__main__":
        testAPP()
        



