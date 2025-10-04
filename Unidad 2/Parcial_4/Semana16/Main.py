import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
import atexit


class Gestionar:
    """
    Clase principal para la gestión de la lista de tareas con interfaz gráfica.
    Incluye persistencia de datos y manejo de atajos de teclado.
    """

    def __init__(self, master):
        self.master = master
        master.title("📝 Listado de Tareas")
        master.geometry("450x450")

        # Definir el nombre del archivo donde se guardara la lista
        self.filename = "Lista_archivo.txt"

        # Fuente para la lista de tareas
        self.task_font = tkfont.Font(family="Arial", size=12)

        # Cargar todas las tareas guardadas en el archivo
        self.tasks = self.load_tasks()

        # Configurar la función de guardado al cerrar la aplicación
        atexit.register(self.save_tasks)

        # Configuración de Atajos de Teclado Globales
        # 1. Cerrar la aplicación con 'Escape' (Global)
        self.master.bind('<Escape>', lambda event: self.master.quit())

        # Widgets de Entrada y Botón Añadir
        input_frame = tk.Frame(master)
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        self.task_entry = tk.Entry(input_frame, width=40, font=self.task_font)
        self.task_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        self.add_button = tk.Button(input_frame, text="➕ Añadir", command=self.add_task, bg="#4CAF50", fg="white",
                                    font=self.task_font)
        self.add_button.pack(side=tk.RIGHT)

        # 2. Añadir tarea al presionar 'Enter' en el campo de entrada
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Listbox para mostrar tareas
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

        # Atajos de Teclado CONDICIONALES
        # Marcar/Desmarcar con 'c' minuscula
        self.task_list.bind('<Key-C>' , lambda event: self.complete_task())
        # Marcar/Desmarcar con 'c' mayuscula
        self.task_list.bind('<c>', lambda event: self.complete_task())
        # Eliminar con 'd'
        self.task_list.bind('<Key-D>' , lambda event: self.delete_task())
        # Eliminar con 'd'
        self.task_list.bind('<d>', lambda event: self.delete_task())
        # 5. Eliminar con 'Delete'
        self.task_list.bind('<Delete>', lambda event: self.delete_task())

        # Botones de Acción
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10, padx=10, fill=tk.X)

        self.complete_button = tk.Button(
            button_frame,
            text="✅ Marcar Tarea (C)",
            command=self.complete_task,
            bg="#2196F3",
            fg="white",
            font=self.task_font
        )
        self.complete_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))

        self.delete_button = tk.Button(
            button_frame,
            text="❌ Eliminar Tarea (D/Del)",
            command=self.delete_task,
            bg="#F44336",
            fg="white",
            font=self.task_font
        )
        self.delete_button.pack(side=tk.RIGHT, expand=True, fill=tk.X, padx=(5, 0))

        # Cargar la vista de la Listbox después de cargar las tareas
        self.load_tasks_to_listbox()
        # Dar foco al campo de entrada al iniciar la aplicación
        self.task_entry.focus_set()

    # --- Métodos de Persistencia y CRUD ---

    def save_tasks(self):
        """Guarda la lista de tareas en el archivo de texto."""
        with open(self.filename, 'w', encoding='utf-8') as f:
            for task_text, is_completed in self.tasks:
                # Usar el prefijo completo para consistencia
                status = "X" if is_completed else " "
                f.write(f"[{status}]{task_text}\n")

    def load_tasks(self):
        """Carga las tareas desde el archivo de texto al iniciar la aplicación."""
        tasks = []
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('[X]'):
                        task_text = line[3:]
                        tasks.append((task_text, True))
                    elif line.startswith('[ ]'):
                        task_text = line[3:]
                        tasks.append((task_text, False))
            return tasks
        except FileNotFoundError:
            return []

    def load_tasks_to_listbox(self):
        """Actualiza la vista del Listbox con el contenido de self.tasks."""
        self.task_list.delete(0, tk.END)

        for index, (task, is_completed) in enumerate(self.tasks):
            # Insertar la tarea en la Listbox
            self.task_list.insert(tk.END, task)

            # Proporcionar feedback visual (color gris para completadas)
            if is_completed:
                self.task_list.itemconfig(index, fg="gray", selectforeground="gray")
            else:
                self.task_list.itemconfig(index, fg="black", selectforeground="black")

    def add_task(self):
        """Añade una nueva tarea y guarda la lista."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append((task, False))
            self.task_entry.delete(0, tk.END)
            self.load_tasks_to_listbox()
            self.save_tasks()
            # Mover el foco al Listbox tras añadir, permitiendo usar atajos
            self.task_list.focus_set()
        else:
            messagebox.showwarning("Advertencia", "El campo de tarea no puede estar vacío.")

    def complete_task(self):
        """Marca/desmarca la tarea seleccionada y guarda la lista."""
        try:
            selected_index = self.task_list.curselection()[0]
            task_text, is_completed = self.tasks[selected_index]

            # Invertir el estado de completado
            new_state = not is_completed
            self.tasks[selected_index] = (task_text, new_state)

            self.load_tasks_to_listbox()
            self.task_list.selection_set(selected_index)  # Mantener la selección
            self.save_tasks()

        except IndexError:
            # Esto se muestra solo si se presiona el botón sin selección.
            # Los atajos de teclado ligados al Listbox ya fallarán en su evento si no hay foco.
            # Mantengo la advertencia para el clic del botón.
            messagebox.showwarning("Advertencia", "Debe seleccionar una tarea.")

    def delete_task(self):
        """Elimina la tarea seleccionada y guarda la lista."""
        try:
            selected_index = self.task_list.curselection()[0]

            del self.tasks[selected_index]
            # La línea self.task_list.delete(selected_index) ya no es necesaria
            # porque load_tasks_to_listbox() reconstruye la lista.
            self.load_tasks_to_listbox()
            self.save_tasks()

        except IndexError:
            messagebox.showwarning("Advertencia", "Debe seleccionar una tarea.")


# Ejecución de la Aplicación

if __name__ == "__main__":
    root = tk.Tk()
    app = Gestionar(root)
    root.mainloop()