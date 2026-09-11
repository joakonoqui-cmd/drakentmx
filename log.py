# log.py
from rich.console import Console
from rich.progress import Progress

console = Console()

class NoLog:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass

def get_progress():
    progress = Progress(console=console)
    task = progress.add_task("[cyan]Descargando...[/]", total=100)

    def hook(d):
        if d['status'] == 'downloading':
            try:
                p = d['_percent_str']
                import re
                p = re.sub(r'[^\d.]', '', p)
                percent = float(p)
                progress.update(task, completed=percent)
            except:
                pass
        if d['status'] == 'finished':
            progress.update(task, completed=100)

    return progress, hook

def get_ydl_opts(ruta, hook):
    return {
        'outtmpl': f'{ruta}/%(title)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'logger': NoLog(),
        'progress_hooks': [hook],
        'noprogress': True,
    }
