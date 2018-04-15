
from pyfiglet import Figlet
import wypozyczaj

figlet = Figlet(font="slant")

def application(environ, start_response):
#    yield figlet.renderText("borysion").encode("utf-8")

    wypozyczaj.transaction()
    
    start_response("200 OK", [("Content-Type", "text/plain"),
                              ("Content-Encoding", "utf-8")])
    for k, v in environ.items():
        yield f"{k:>20} => {v}".encode("utf-8")


