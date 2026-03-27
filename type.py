from typing import Annotated

def compute_sum(
        x: float, 
        y: float, 
        z:float, 
        round: int | None = None) -> float: #funzione che accetta x,y,z float; opzionale un round intero e restituisce un float
    return x + y

s: str = compute_sum(1,"poba", 3.3)
print(s)

a: list[int]    #lista di interi
b: dict[str, int]   #dizionario con la struttura stringa:int
c: list | tuple | None  #c può essere una lista o tupla o None

x: Annotated[int, ...,...,...]  #primo campo = tipo, gli altri campi sono metadati, 