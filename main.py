from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import Field, BaseModel  #per aggiungere vincoli ai campi di un modello Pydantic


class Collegiali(BaseModel):
    name: Annotated[str, Field(min_length = 3, max_length = 30), Form()]
    age: Annotated[int, Field(ge = 18, le = 100), Form()]
    course: Annotated[str, Field(min_length = 3, max_length = 50), Form()]

collegiali = Collegiali.model_validate(
    {"name": "Mario Rossi", "age": 20, "course": "Ingegneria Informatica"})


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

@app.get("/add_collegiale", response_class=HTMLResponse)
def add_collegiale(request : Request):
    """ Renders the add collegiale page.
    """    
    
    return templates.TemplateResponse(
        request=request,
        name = "add_collegiale.html",
        context = {}
    )


#USIAMO METODO POST PER PASSARE DATI
@app.post("/insert_collegiale")  #serve per separare le responsabilità, qui accettiamo input del form superiore
def insert_collegiale(
    name: Annotated[str, Field(min_length = 3, max_length = 30), Form()],  #vincoli sul campo name, deve essere una stringa con lunghezza minima 3 e massima 30
    age: Annotated[int, Field(ge = 18, le = 100), Form()],  #vincoli sul campo age, deve essere un intero maggiore o uguale a 18 e minore o uguale a 100
    course: Annotated[str, Field(min_length = 3, max_length = 50), Form()]
    ):
    """ Inserts a new collegiale into the list.
    """
    collegiale = {"name": name, "age": age, "course": course}
    collegiali_list.append(collegiale)

    return "Collegiale added successfully"

@app.post("/insert_collegiale")  #serve per separare le responsabilità, qui accettiamo input del form superiore
def insert_collegiale(
    collegiale: Annotated[Collegiali, Form()]
    ):
    """ Inserts a new collegiale into the list.
    """
    collegiali_list.append(collegiale)

    return "Collegiale added successfully"

@app.post("/insert_collegiali_json")
def insert_collegiale_json(
    collegiale: Collegiali
    ):
    """ Inserts collegiale into the list using a JSON to receive data
    """
    collegiali_list.append(collegiale)
@app.get("/collegiali_json")
def collegiali_json():
    """ Returns the list of collegiali in JSON format.
    """
    
    return collegiali_list  
