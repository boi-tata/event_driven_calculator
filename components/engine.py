"""
Módulo contendo todos os elementos necessários para realizar as operações
matemáticas possíveis na calculadora.
"""

from components.events import ErrorEvent, OperationEvent, ResultEvent

class Processor:
    """
    Classe para realizar operações matemáticas.
    """
    
    def add(self, x:int, y:int) -> int:
        """
        Adiciona `y` em `x`.
        """

        return x + y

    def sub(self, x:int, y:int) -> int:
        """
        Subtrai `y` de `x`.
        """

        return x - y

    def multiply(self, x:int, y:int) -> int:
        """
        Multiplica `x` por `y`.
        """

        return x * y

    def divide(self, x:int, y:int) -> int:
        """
        Divide `x` por `y`.
        """

        return x // y

    def translate(self, operator:str):
        """
        Mapeia as operações conhecidas com suas representações.
        """

        mapped_operations = {
            '+': self.add,
            '-': self.sub,
            '*': self.multiply,
            '/': self.divide,
        }
        operation = mapped_operations.get(operator)
        if operation is None:
            raise NotImplementedError(f"Unknow operator '{ operator }'")

        return operation

    def receive_event(self, event):
        """
        Processa eventos do tipo `OperationEvent`, retornando um `ResultEvent`
        com o resultado da operação. Se houver erro na execução da operação,
        retorna um `ErrorEvent`.
        
        Caso o evento recebido não seja um `OperationEvent`, retorna `None`.
        """
        if isinstance(event, OperationEvent):
            operator = event.operator
            operands = event.operands
            try:
                operation = self.translate(operator)
                response = ResultEvent(operation(*operands))
            except Exception as e:
                response = ErrorEvent(event, e)
            return response

        return None