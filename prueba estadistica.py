from tkinter import*
raiz = Tk ()
raiz.title("estadistica 2")#titulo 
raiz.resizable()#modificacion de la ventana
raiz.iconbitmap(r"C:\Users\ANDRES\Desktop\DOC Andres\Estadistica 2 2025\programa estadistica\icono estapro2 3.ico")
#raiz.geometry("600x350")
raiz.config(bg="black")


miFrame=Frame()
miFrame.pack()#pocicion del cuadro 
miFrame.config(bg="sky blue")#color del cuadro
miFrame.config(width="800",height="600")
miFrame.config(bd="5")#tamaño del borde 
miFrame.config(relief="ridge")#estilo de borde
miFrame.config(cursor="hand2")#tipo de corsor

miLabe=Label(miFrame, text="grafica lineal ")
miLabe.place(x="200",y="200")


raiz.mainloop()