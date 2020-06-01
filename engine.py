"""
Módulo contendo todos os elementos necessários para realizar as operações
matemáticas possíveis na calculadora.
"""

from events import ErrorEvent, OperationEvent, ResultEvent

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

    def resolve(self, operation:str, x:int, y:int) -> int:
        """
        Mapeia as operações conhecidas com seus símbolos.
        """

        mapped_operations = {
            '+': self.add,
            '-': self.sub,
            '*': self.multiply,
            '/': self.divide,
        }
        func = mapped_operations[operation]
        return func(x, y)

    def receive_event(self, event):
        """
        Processa eventos do tipo `OperationEvent`.
        Se o cálculo for realizado, retorna uma instância de `ResultEvent`.
        Se houver erro, retorna uma instância de `ErrorEvent`.
        """
        if isinstance(event, OperationEvent):
            op = event.operator
            x, y = event.operands
            try:
                response = ResultEvent(self.resolve(op, x, y))
            except Exception as e:
                response = ErrorEvent(event, e)
            return response

        return None