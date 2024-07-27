from rich.console import Console
from rich.text import Text

console = Console()

def c_warning(*data):
    console.print(*data, style="YELLOW bold")

def c_success(*data):
    console.print(*data, style="GREEN bold")

def c_error(*data):
    console.print(*data, style="RED bold")

def c_input(data):
    return console.input(f"[bold green] {data} [/bold green]")



text = """
██╗  ██╗ ██████╗  █████╗ ███╗   ██╗ ██████╗      █████╗ ███╗   ██╗██╗  ██╗
██║  ██║██╔═══██╗██╔══██╗████╗  ██║██╔════╝     ██╔══██╗████╗  ██║██║  ██║
███████║██║   ██║███████║██╔██╗ ██║██║  ███╗    ███████║██╔██╗ ██║███████║
██╔══██║██║   ██║██╔══██║██║╚██╗██║██║   ██║    ██╔══██║██║╚██╗██║██╔══██║
██║  ██║╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝    ██║  ██║██║ ╚████║██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
[i green]
facebook : https://www.facebook.com/hoanganhvazuta
telegram : @trautv1  / @hoanganhcoder
github   : hoanganhcoder
gmail    : hoanganhfreelancer@gmail.com
[/i green]
[bold green]Netcoin [/bold green]
[bold cyan]
Future:
    * Play game
    * Auto claim
    * Use proxy
    * More ...
[/bold cyan]

---------------------------------------------------------------------------
 """
console.print(text, style="bold red")

