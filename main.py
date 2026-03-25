from email.mime import text

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="./templates")  #dove sono contenuti i templates

@app.get("/", response_class=HTMLResponse)  #di default FastAPI restituisce JSON, ma con response_class=HTMLResponse restituisce HTML
def home(request : Request):  #request conterrà la richiesta HTTP Get che riceve l'app
    """ Renders the home page.
    """

    text = {
        "title" : "Home Page",
        "content" : "Welcome to the home page!",
    }

    context = {     #dizionario con i dati da passare al template nelle variabili jinja2
        "text" : text,  #passaggio parametri al template, in questo caso text è un dizionario con title e content
        "sequence" : ['a', 'b', 'c', 'd', 'e'],  #passaggio di una lista al template
    }

    return templates.TemplateResponse(  #restituisce la pagina web home.html con i dati di context
        request=request, name = "home.html", context=context
    )