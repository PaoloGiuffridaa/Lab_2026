from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static",StaticFiles(directory="static"), name="aaaaa")  #per poter servire i file statici (css, js, immagini) dalla cartella static
templates = Jinja2Templates(directory="./templates")  #dove sono contenuti i templates

collegiali_list = [
    {"name": "Mario Rossi", "age": 20, "course": "Ingegneria Informatica"},
    {"name": "Giulia Bianchi", "age": 22, "course": "Medicina"},
    {"name": "Luca Verdi", "age": 21, "course": "Economia"},
    {"name": "Sara Neri", "age": 19, "course": "Architettura"}
]

@app.get("/", response_class=HTMLResponse)  #di default FastAPI restituisce JSON, ma con response_class=HTMLResponse restituisce HTML
def home(request : Request):  #request conterrà la richiesta HTTP Get che riceve l'app
    """ Renders the home page.
    """

    return templates.TemplateResponse(  #restituisce la pagina web home.html con i dati di context
        request=request,
        name = "home.html",
        context = {"text": "Welcome to College Sant'Efisio"}
    )

@app.get("/collegiali", response_class=HTMLResponse)
def collegiali_page(request : Request):
    """ Renders the collegiali page.
    """

    return templates.TemplateResponse(
        request=request,
        name = "collegiali.html",
        context = {"collegiali_list": collegiali_list}
    )