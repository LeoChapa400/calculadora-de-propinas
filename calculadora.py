import tkinter as tk 
from tkinter import messagebox

def calcular_propina():
    try:
        total_cuenta = float(entry_total_cuenta.get())
        porcentaje_propina = float(entry_porcentaje_propina.get())
        propina = (total_cuenta * porcentaje_propina) / 100
        total_con_propina = total_cuenta + propina
        label_resultado.config(text=f"Propina: ${propina:.2f}\nTotal con Propina: ${total_con_propina:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por Favor ingrese valores Numericos validos")   

ventana = tk.Tk()
ventana.title("Calculadora de propinas")

label_total_cuenta = tk.Label(ventana, text="Total de la Cuenta")
label_total_cuenta.grid(row=0, column=0, padx=10, pady=10)

entry_total_cuenta = tk.Entry(ventana)
entry_total_cuenta.grid(row=0, column=0, padx=10, pady=10)

label_porcentaje_propina = tk.Label(ventana, text="Porcentaje de propinas")
label_porcentaje_propina.grid(row=1, column=0, padx=10, pady=10)

entry_porcentaje_propina = tk.Entry(ventana)
entry_porcentaje_propina.grid(row=1, column=0, padx=10, pady=10)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_propina)
boton_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=2, column=0, padx=10, pady=10)

ventana.mainloop
