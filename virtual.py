import random
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def main():
    game_history = []
    round_number = 1
    
    while True:
        menu_text = "[1] Почати гру\n[2] Історія ігор\n[3] Вихід"
        console.print(Panel(menu_text, title="Головне меню", expand=False, border_style="cyan"))
        
        choice = Prompt.ask("Оберіть дію", choices=["1", "2", "3"])
        
        if choice == "1":
            user_choice = Prompt.ask(
                "Ваш вибір", 
                choices=["Камінь", "Ножиці", "Папір"],
                default="Камінь"
            )
            
            computer_choice = random.choice(["Камінь", "Ножиці", "Папір"])
            console.print(f"Комп'ютер обрав: [cyan]{computer_choice}[/cyan]")
            
            if user_choice == computer_choice:
                result = "Нічия"
                color = "yellow"
            elif (user_choice == "Камінь" and computer_choice == "Ножиці") or \
                 (user_choice == "Ножиці" and computer_choice == "Папір") or \
                 (user_choice == "Папір" and computer_choice == "Камінь"):
                result = "Перемога"
                color = "green"
            else:
                result = "Поразка"
                color = "red"
            
            console.print(f"Результат: [{color} bold]{result}![/]\n")
            
            game_history.append({
                "round": round_number,
                "player": user_choice,
                "computer": computer_choice,
                "result": result,
                "color": color
            })
            round_number += 1
            
        elif choice == "2":
            if not game_history:
                console.print("[yellow]Ви ще не зіграли жодного раунду.[/]\n")
                continue
                
            table = Table(title="Історія матчів")
            table.add_column("Раунд", justify="center", style="cyan")
            table.add_column("Гравець", justify="center")
            table.add_column("Комп'ютер", justify="center")
            table.add_column("Результат", justify="center")
            
            wins = 0
            for game in game_history:
                table.add_row(
                    str(game["round"]),
                    game["player"],
                    game["computer"],
                    f"[{game['color']}]{game['result']}[/]"
                )
                if game["result"] == "Перемога":
                    wins += 1
            
            console.print(table)
            
            console.print(Panel(
                f"Всього ігор: {len(game_history)} | Перемог: {wins}",
                style="magenta",
                expand=False
            ))
            print("\n")
            
        elif choice == "3":
            console.print("[bold red]Вихід з гри. Бувай![/]")
            break

if __name__ == "__main__":
    main()