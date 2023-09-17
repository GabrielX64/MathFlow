from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from spinbox import *
import random as r
import networkx as nx
import matplotlib.pyplot as plt
import tkinter.messagebox as tkMessageBox
from networkx.algorithms.flow import maximum_flow

complete = ctk.CTk()
check_var = customtkinter.StringVar(value="off")
G = None
complete.config()
customtkinter.set_appearance_mode("light")
usuario = None

def pruebadelcheckbox():
        customtkinter.set_appearance_mode("dark")
        if check_var.get() == "off":
            customtkinter.set_appearance_mode("light")

def dimensiones():
    complete.geometry("1280x720")
    complete.title("Matemática Computacional")
    complete.iconbitmap("Kuromi.ico")

def Creditos():
    ventana_principal.place_forget()
    ventana2.place_forget()
    creditos = ctk.CTkFrame(complete,border_width=5)
    ventana1.place(relx=0, rely=0, relwidth=1, relheight=1)
    creditos.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.3)
    titulo = ctk.CTkLabel(creditos, text="Créditos", font=("Display", 20, "bold"))
    titulo.place(x=50, y=10)
    titulo = ctk.CTkLabel(creditos, text=("\u2022 "+"Aranguri Dominguez, Neera Celine"+"\n\u2022 "+"Cajas Lara, Gabriel Alfonso"+"\n\u2022 "+"Jara Torres, Franco Renatto"+"\n\u2022 "+"Razzeto Dávila, Ángel Ramon"+"\n\u2022 "+"Tenorio Castillo, Sebastián Miguel"), font=("Arial", 12, "normal"))
    titulo.place(x=10, y=40)
    cambio(creditos, Pantallaventana1, "Cerrar ventana","red", 200, 30, 0.5, 0.8, "center")

def cambio(frame, num, texto,color,ancho, alto, x, y, posicion):
    button = ctk.CTkButton(frame,text=texto,width = ancho, height= alto, corner_radius=50,
                                     command= num, fg_color=color)

    button.place(relx=x, rely=y, anchor= posicion)

def calculate_max_flow(source, sink):
    if G is None:
        tkMessageBox.showerror("Error", "Debes generar un grafo primero")
        return

    try:
        max_flow_value, max_flow_dict = maximum_flow(G, source, sink)
        max_flow_message = f"Flujo máximo: {max_flow_value}\nFlujo en aristas: {max_flow_dict}"
        tkMessageBox.showinfo("Flujo Máximo", max_flow_message)
    except nx.NetworkXUnbounded:
        tkMessageBox.showerror("Error", "El grafo tiene capacidades infinitas en algún camino")

def create_graph(matrix_size, matrix_data):
    global G
    G = nx.Graph()

    for i in range(matrix_size):
        G.add_node(i)

    for i in range(matrix_size):
        for j in range(matrix_size):
            entry_value = matrix_data[i][j].get()

            try:
                entry_value = int(entry_value)
            except ValueError:
                entry_value = 0

            if entry_value != 0:
                G.add_edge(i, j, capacity=entry_value)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    plt.axis('off')
    plt.title("Graph from Matrix")
    plt.show()

def matrix():
    def update_matrix(n: int):
        matrix_size = spinbox_1.get()

        if matrix_size > 15:
            spinbox_1.set(15)
            show_error()
        elif matrix_size < 5:
            show_error()
            spinbox_1.set(5)

        entry: ctk.CTk = None
        for row in matriz:
            for entry in row:
                entry.destroy()

        matriz.clear()
        if n == 1:
            for i in range(matrix_size):
                row = []
                for j in range(matrix_size):
                    entry = ctk.CTkEntry(complete, width=35)
                    entry.place(relx=0.1 + (i / 30), rely=0.2 + (j / 25), anchor=tk.CENTER)
                    row.append(entry)
                matriz.append(row)
        elif n == 2:
            for i in range(matrix_size):
                row = []
                for j in range(matrix_size):
                    num = str(r.randint(1, 100))
                    entry = ctk.CTkEntry(complete, width=35)
                    entry.place(relx=0.1 + (i / 30), rely=0.2 + (j / 25), anchor=tk.CENTER)
                    row.append(entry)
                    entry.insert(0, num)
                matriz.append(row)

    update_button = ctk.CTkButton(complete, text="Actualizar matriz", command=lambda: update_matrix(1))
    update_button.place(relx = 0.82, rely= 0.3, anchor=tk.CENTER)

    random_button = ctk.CTkButton(complete, text="Generar Matrix Aleatoria", fg_color="#DC143C", corner_radius=50,
                                  command=lambda: update_matrix(2))
    random_button.place(relx=0.7, rely=0.2, anchor=tk.CENTER)

    global matriz  # Declare matrix as a global variable
    matriz = []
    matrix_size = spinbox_1.get()

    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            entry = ctk.CTkEntry(complete, width=35)
            entry.place(relx=0.1 + (i / 30), rely=0.2 + (j / 25), anchor=tk.CENTER)
            row.append(entry)

        matriz.append(row)

    return matriz

def playgifImage():
    global img_frames, img_index, img_label

    img_frame = img_frames[img_index]
    img_frame = img_frame.resize((350, 300), Image.LANCZOS)
    img = ctk.CTkImage(img_frame, size=(350,300))
    img_label.configure(image=img)
    img_label.image = img

    img_index += 1
    if img_index >= len(img_frames):
        img_index = 0
    
    ventana_principal.after(1000, playgifImage)

def gifImage(frame, imagen, x, y):
    global img_frames, img_index, img_label
    img = Image.open(imagen)
    img_frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
    img_index = 0

    img_label = ctk.CTkLabel(frame, text = None)
    img_label.place(relx=x, rely=y, anchor = tk.CENTER)
    playgifImage()
    
def PantallaPrincipal():
    ventana1.place_forget()
    ventana2.place_forget()
    creditos.place_forget()
    ventana_principal = ctk.CTkFrame(complete, fg_color=complete._fg_color)
    ventana_principal.place(relx=0, rely=0, relwidth=1, relheight=1)
    
    text2 = ctk.CTkLabel(ventana_principal, text="MathFlow", font=("League Spartan", 100, "bold"), text_color="purple")
    text2.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    gifImage(ventana_principal, "Cinnamon.gif", 0.5, 0.5)

    checkbox = ctk.CTkSwitch(complete, text="Modo Nocturno", command=pruebadelcheckbox,
                                        variable=check_var, onvalue="on", offvalue="off")
    
    checkbox.place(relx = 0.5, rely= 0.9, anchor=tk.CENTER)

    cambio(ventana_principal, Pantallaventana1, "Púlsame", "purple", 200, 30, 0.5, 0.8, "center")
    

def Pantallaventana1():
    ventana_principal.place_forget()
    ventana2.place_forget()
    creditos.place_forget()
    
    ventana1 = ctk.CTkFrame(complete,fg_color=complete._fg_color)
    ventana1.place(relx=0, rely=0, relwidth=1, relheight=1)


    titulo = ctk.CTkLabel(ventana1, text="Algoritmo de Ford Fulkerson", font=("Display", 20, "bold"))
    titulo.place(relx=0.3, rely=0.08, anchor = tk.CENTER)
    text1= ctk.CTkLabel(ventana1, text="Fue desarrollado por Delbert Fulkerson y Lester Ford en 1956. El algoritmo Ford-Fulkerson es un \nalgoritmo utilizado para encontrar el flujo máximo en una red de flujo. El problema de flujo máximo \nse utiliza en conjunto en aplicaciones de transporte y asignación.",font=("Arial", 15, "normal"),compound=["left"])
    text1.place(relx=0.3, rely=0.18, anchor = tk.CENTER)
    
    
    cambio(ventana1, Creditos, "Creditos", "purple", 200, 30, 0.8, 0.2, "center")

    text2= ctk.CTkLabel(ventana1, text="Ingrese su nombre:", font=("Display", 18, "bold"))
    text2.place(relx=0.1,rely=0.7, anchor = tk.CENTER)
    texto = ctk.CTkEntry(ventana1,width=187)
    texto.place(relx=0.25, rely=0.7, anchor = tk.CENTER)
    def guardar():
            global usuario
            usuario=texto.get()
            if(usuario==''):
                aviso = ctk.CTkLabel(ventana1, text="No se puede dejar en blanco", font=("Arial", 10, "bold"))    
                aviso.place(relx=0.05, rely =0.72)

            elif(usuario!=''):
                aviss = ctk.CTkLabel(ventana1, text="Usuario guardado                     ", font=("Arial", 10, "bold"))    
                aviss.place(relx=0.05, rely =0.72) 
                print(usuario)

    guarda=ctk.CTkButton(ventana1,text=("Guardar"), command=guardar)
    guarda.place(relx=0.39, rely=0.7, ancho="center")
    def borrar():
        texto.delete(0,"end")

    borra=ctk.CTkButton(ventana1,text=("Borrar"), command=borrar)
    borra.place(relx=0.5, rely=0.7, ancho="center")
    
    my_image = customtkinter.CTkImage(light_image=Image.open("digrafo_dirigido_ponderado_luz.png"),
                                  dark_image=Image.open("digrafo_dirigido_ponderado_nocturno.png"),
                                  size=(375, 200))

    image_label = customtkinter.CTkLabel(complete, image=my_image, text="")
    image_label.place(relx=0.3, rely= 0.4, anchor=tk.CENTER)
    cambio(ventana1, Pantallaventana2, "¡Comencemos!", "purple", 200, 30, 0.8, 0.9, "center")
    cambio(ventana1, PantallaPrincipal, "Back", "purple", 200, 30, 0.2, 0.9, "center")

def Pantallaventana2():
    if usuario == None or usuario == '':
        CTkMessagebox(title="Error", message='Debes escribir tu nombre de usuario antes de ingresar', icon="cancel", topmost=False)
        return
    ventana_principal.place_forget()
    ventana1.place_forget()
    creditos.place_forget()
    ventana2 = ctk.CTkFrame(complete, fg_color=complete._fg_color)
    ventana2.place(relx=0, rely=0, relwidth=1, relheight=1)

    def printnum():
        print(spinbox_1.get())

    global spinbox_1
    spinbox_1 = IntSpinbox(complete, width=150, step_size=1, command=printnum)
    spinbox_1.place(relx = 0.7, rely= 0.3, anchor=tk.CENTER)
    spinbox_1.set(5)

    usuario_label = ctk.CTkLabel(complete, text=f"Bienvenido: {usuario}")
    usuario_label.place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    
    matrix()

    generate_graph_button = ctk.CTkButton(complete, text="Generar Grafo", fg_color="#DC143C", corner_radius=50,
                                          command=lambda: create_graph(spinbox_1.get(), matriz))
    generate_graph_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)

    max_flow_button = ctk.CTkButton(complete, text="Calcular Flujo Máximo", fg_color="#DC143C", corner_radius=50,
                                    command=lambda: calculate_max_flow(int(source_entry.get()), int(sink_entry.get())))
    max_flow_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

    global source_entry, sink_entry
    source_label = ctk.CTkLabel(complete, text="Nodo de Origen:")
    source_label.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
    source_entry = ctk.CTkEntry(complete, width=10)
    source_entry.place(relx=0.78, rely=0.4, anchor=tk.CENTER)

    sink_label = ctk.CTkLabel(complete, text="Nodo de Destino:")
    sink_label.place(relx=0.7, rely=0.44, anchor=tk.CENTER)
    sink_entry = ctk.CTkEntry(complete, width=10)
    sink_entry.place(relx=0.78, rely=0.44, anchor=tk.CENTER)

    cambio(ventana2, Pantallaventana1, "Back","purple",20,25,0.1,0.1, tk.CENTER)


if __name__ == "__main__":
    dimensiones()
    ventana_principal = ctk.CTkFrame(complete, fg_color=complete._fg_color)
    ventana_principal.place(relx=0, rely=0, relwidth=1, relheight=1)
    ventana1 = ctk.CTkFrame(complete,fg_color=complete._fg_color)
    ventana2 = ctk.CTkFrame(complete,fg_color=complete._fg_color)
    creditos = ctk.CTkFrame(complete,border_width=5,bg_color="white",fg_color="blue")

    PantallaPrincipal()

    complete.mainloop()