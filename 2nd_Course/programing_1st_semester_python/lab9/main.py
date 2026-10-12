from ascii_magic import from_url
from alive_progress import alive_bar
from time import sleep

my_art = from_url(
    "https://picsum.photos/300"
)
my_art.to_terminal()

with alive_bar(50) as bar:
    for i in range(50):
        sleep(0.05)
        bar()
