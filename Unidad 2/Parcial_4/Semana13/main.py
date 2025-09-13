import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, master):
        """
        Primero se le dara un nombre a la ventada para luego ejecutarlo
        """
        self.master = master
        master.title("Aplicación de Gestión de Tareas")
        master.geometry("400x300")  # Se define cual sera el tamaño de la ventana
        master.config(bg="#f0f0f0")  # Se le coloca un color de fondo

        # Se le coloca un nombre principal
        self.label_title = tk.Label(
            master,
            text="Listado de Tareas",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.label_title.pack(pady=10)

        # Frame para los controles de entrada (etiqueta y campo de texto)
        self.input_frame = tk.Frame(master, bg="#f0f0f0")
        self.input_frame.pack(pady=5)

        # se dara una indicacion a seguri por el usuario
        self.label_entry = tk.Label(
            self.input_frame,
            text="Ingresa una nueva tarea:",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#555555"
        )
        self.label_entry.pack(side=tk.LEFT, padx=5)

        # se le añade un frame de texto, en donde el usuario podra escribir una tarea
        self.entry_task = tk.Entry(self.input_frame, width=30)
        self.entry_task.pack(side=tk.LEFT, padx=5)
        self.entry_task.bind("<Return>", self.add_task_on_enter)  # Permite agregar con la tecla Enter

        # se inicializa los bototnes
        self.button_frame = tk.Frame(master, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # Se configura el nombre y la accion que hara el boton agregar
        self.button_add = tk.Button(
            self.button_frame,
            text="Añadir Tarea",
            command=self.add_task,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED  # Efecto 3D
        )
        self.button_add.pack(side=tk.LEFT, padx=5)

        # Se configura el nombre y la accion que hara el boton limpiar
        self.button_clear = tk.Button(
            self.button_frame,
            text="Limpiar",
            command=self.clear_all,
            bg="#f44336",
            fg="white",
            font=("Arial", 10, "bold"),
            relief=tk.RAISED
        )
        self.button_clear.pack(side=tk.LEFT, padx=5)

        # Se inicializa el frame en donde se vera la lista de las tareas ingresadas
        self.listbox_tasks = tk.Listbox(
            master,
            width=50,
            height=10,
            bg="white",
            fg="#333333",
            selectbackground="#a6a6a6",  # este color se vera cuando se haya seleccionado un elemento
            selectforeground="black",
            font=("Arial", 10)
        )
        self.listbox_tasks.pack(pady=10)

    def add_task(self):
        """
        Cuando se presiona el btoton añadir se ejecuta la siguiente funcion y luego agregarlo
        a la lista que se presenta
        """
        task = self.entry_task.get().strip()  # Obtiene el texto y elimina espacios en blanco
        if task:  # Verifica que el campo no esté vacío
            self.listbox_tasks.insert(tk.END, task)  # Añade la tarea al final de la lista
            self.entry_task.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            #En caso que no se ingrese nada en el campo se mostrara este mensaje de advertencia
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def add_task_on_enter(self, event):
        """
        si al momento de escribir se presiona la tecla enter de ustiliza el siguiente comando para
        agregarlo a la lista.
        """
        self.add_task()

    def clear_all(self):
        """
        Al presionar el boton limpiar se elimina toda la lista y lo que se tenga escrito en el
        frame de ingreso
        """
        self.listbox_tasks.delete(0, tk.END)  # Borra todos los elementos de la lista
        self.entry_task.delete(0, tk.END)  # Limpia el campo de entrada
        messagebox.showinfo("Información", "La lista y el campo han sido limpiados.")


# Creación de la ventana principal y ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()