def add1(elem1:int, elem2:float) -> float:
    return elem1 + elem2

val1 = add1(1,3)
print(val1)

# quando falamos de typing estamos falando sobre:
# int, float, str, bool
# mas se quisermos usar
# outros tipos de dados, como listas, dicionários, etc.
# podemos usar o módulo typing
from typing import List, Dict, Tuple

def add(elem1:int, elem2:float) -> Dict:
    response =  elem1 + elem2
    return {"sum" : response}

val1 = add(1,3.2)
print(val1)

#documentação do typing
# https://docs.python.org/3/library/typing.html