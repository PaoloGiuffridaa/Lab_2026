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
    context = {     #dizionario con i dati da passare al template nelle variabili jinja2
        "text" : "<a href='https://www.google.com'>Google</a>"  #vengono interpretati come stringhe (sanitizzazione input)
    }

    return templates.TemplateResponse(  #restituisce la pagina web home.html con i dati di context
        request=request, name = "home.html", context=context
    )