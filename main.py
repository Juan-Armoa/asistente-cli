import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    while True:
        menu = (
            "[bold cyan]1.[/bold cyan] Usar el Bot de IA (Gemini)\n"
            "[bold cyan]2.[/bold cyan] Abrir Gestor de Notas\n"
            "[bold cyan]3.[/bold cyan] Salir"
        )
        console.print(Panel(menu, title="🚀 MI ASISTENTE CLI", border_style="bold green"))
        
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            os.system("python test_bot.py")
        elif opcion == "2":
            os.system("python notas.py")
        elif opcion == "3":
            console.print("[bold blue]¡Nos vemos![/bold blue]")
            break
        else:
            console.print("[bold red]Opción no válida.[/bold red]")

if __name__ == "__main__":
    main()