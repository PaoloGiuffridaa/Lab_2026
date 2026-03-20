from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")   #app.<metodoHTTP>(<path>)
def hello_world(
        q: str,
        sort: bool = False):   #fastAPI ti da validazione dell'input
    return {"q": q, "sort": sort}

@app.get("/home")   #l'ordine è importante, se deve sovrascrivere qualcosa va messo prima (es. @app.get("/{username}"))
def homepage() -> str:
    return f"THIS IS THE HOMEPAGE"

@app.get("/{username}") #URL PARAMETRICO
def username_webpage(username) -> str:
    return f"this is the webpage of {username}"

@app.get("/{username}/orders/{order_id}") #URL PARAMETRICO
def repository_webpage(
        username: str,
        order_id: int,
        sort: bool = False) -> str:
    return f"this is the order with ID:{order_id} of {username}. Sorted: {sort}."
