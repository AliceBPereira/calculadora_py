from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    '''
    - Um numero é dividido em 3 partes iguais. x
    - A primeira parte é dividida por 4 e seu resultado somado a 7. 
      Após isso, o resultado é elevado ao quadrado e multiplicado por um valor de 0.257.
    A segunda parte é elevada a potencia de 2.121, dividido por 5 e somando a 1
    Por fim, é somado esses 3 valores e entregue o resultado
    '''
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_part_resulte = self.__calculate_first_part(splited_number)
        second_part_result = (splited_number ** 2.121) / 5 + 1
        
    
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("body mal formatado")
        
        input_data = body[ "number"]
        return input_data
    
    def __calculate_first_part(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        first_part = first_part ** 2
        first_part *= 0.257
        return first_part