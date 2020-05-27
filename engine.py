"""
Módulo contendo todos os elementos necessários para realizar as operações
matemáticas possíveis na calculadora.
"""

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

    def receive_event(self, event:dict):
        """
        Processa eventos, retornando o resultado ou o erro causado.
        Chaves esperadas:
        >- 'operation': simbolo da operação matemática [str]
        >- 'operands': par de operandos envolvidos na operação [iterable]
        """
        op = event.get('operation')
        if op:
            x, y = event['operands']
            try:
                return self.resolve(op, x, y)
            except Exception as e:
                return e
        
        return None