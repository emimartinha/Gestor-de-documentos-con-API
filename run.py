# Módulo principal para iniciar la aplicación
import ui
import sys
import menu

if __name__ == "__main__":
    # Comprueba los argumentos de línea de comando para determinar el modo de ejecución
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        # Modo terminal
        menu.iniciar()
    else:
        # Modo gráfico (interfaz de usuario con tkinter)
        app = ui.MainWindow()
        app.mainloop()