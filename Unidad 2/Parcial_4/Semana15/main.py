import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import atexit  # Módulo para asegurar que las tareas se guarden al cerrar la app


class Gestionar:
    """
    En esta clase se determina cuales seran los botones que se utilizaran.
    """

    def __init__(self, master):
        self.master = master
        master.title(" Listado de tareas")
        master.geometry("450x450")

        # Definir el nombre del archivo donde se guardara la lista
        self.filename = "Lista_archivo.txt"

        # Fuente para la lista de tareas
        self.task_font = tkfont.Font(family="Arial", size=12)

        # Cargar todas las tareas guardadas en el archivo
        self.tasks = self.load_tasks()

        # Configurar la función de guardado al cerrar la aplicación
        atexit.register(self.save_tasks)

        # Widgets de Entrada y Botón Añadir
        self.task_entry = tk.Entry(master, width=40, font=self.task_font)
        self.task_entry.pack(pady=10, padx=10, fill=tk.X)

        self.add_button = tk.Button(master, text="➕ Añadir Tarea", command=self.add_task, bg="#4CAF50", fg="white",
                                    font=self.task_font)
        self.add_button.pack(pady=5, padx=10, fill=tk.X)

        self.task_entry.bind("<Return>", lambda event: self.add_task())

        #Listbox para mostrar tareas
        list_frame = tk.Frame(master)
        list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.task_list = tk.Listbox(
            list_frame,
            height=15,
            width=50,
            borderwidth=0,
            font=self.task_font,
            selectmode=tk.SINGLE
        )
        self.task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_list.yview)

        # Configurar evento Doble Clic para marcar como completada
        self.task_list.bind("<Double-1>", lambda event: self.complete_task())

        #Botones de Acción
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10, padx=10, fill=tk.X)

        self.complete_button = tk.Button(
            button_frame,
            text="✅ Marcar tarea",
            command=self.complete_task,
            bg="#2196F3",
            fg="white",
            font=self.task_font
        )
        self.complete_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.delete_button = tk.Button(
            button_frame,
            text="❌ Eliminar Tarea",
            command=self.delete_task,
            bg="#F44336",
            fg="white",
            font=self.task_font
        )
        self.delete_button.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))

        # Cargar la vista de la Listbox después de cargar las tareas
        self.load_tasks_to_listbox()

    def save_tasks(self):
        """
        Guarda la lista de tareas en el archivo de texto.
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            for task_text, is_completed in self.tasks:
                status = "X" if is_completed else " "
                f.write(f"[{status}]{task_text}\n")

    def load_tasks(self):
        """
        Carga las tareas desde el archivo de texto al iniciar la aplicación.
        """
        tasks = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('[X]'):
                        # Tarea completada
                        task_text = line[3:]
                        tasks.append((task_text, True))
                    elif line.startswith('[ ]'):
                        # Tarea pendiente
                        task_text = line[3:]
                        tasks.append((task_text, False))
            return tasks
        except FileNotFoundError:
            # Si el archivo no existe, devuelve una lista vacía
            return []

    def add_task(self):
        """
        Añade una nueva tarea y guarda la lista.
        """
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append((task, False))
            self.task_entry.delete(0, tk.END)
            self.load_tasks_to_listbox()
            self.task_entry.focus_set()
            self.save_tasks()  # ¡Guardar después de añadir!
        else:
            messagebox.showwarning("Advertencia", "El campo de tarea no puede estar vacío.")

    def load_tasks_to_listbox(self):

        self.task_list.delete(0, tk.END)

        for index, (task, is_completed) in enumerate(self.tasks):
            # Insertar la tarea en la Listbox
            self.task_list.insert(tk.END, task)

            if is_completed:
                self.task_list.itemconfig(index, fg="gray")
            else:
                self.task_list.itemconfig(index, fg="black")

    def complete_task(self):
        """
        Marca la tarea seleccionada como completada y guarda la lista.
        """
        try:
            selected_index = self.task_list.curselection()[0]
            task_text, is_completed = self.tasks[selected_index]

            # Invertir el estado de completado
            new_state = not is_completed
            self.tasks[selected_index] = (task_text, new_state)

            self.load_tasks_to_listbox()
            self.task_list.selection_set(selected_index)
            self.save_tasks()  # ¡Guardar después de completar!

        except IndexError:
            messagebox.showwarning("Advertencia", "Debe seleccionar una tarea.")

    def delete_task(self):
        """
        Elimina la tarea seleccionada y guarda la lista.
        """
        try:
            selected_index = self.task_list.curselection()[0]

            del self.tasks[selected_index]
            self.task_list.delete(selected_index)
            self.save_tasks()  # ¡Guardar después de eliminar!

        except IndexError:
            messagebox.showwarning("Advertencia", "Debe seleccionar una tarea.")


#Ejecución de la Aplicación

if __name__ == "__main__":
    root = tk.Tk()
    app = Gestionar(root)
    root.mainloop()