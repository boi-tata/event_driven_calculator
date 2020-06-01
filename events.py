"""
Módulo que contém todos os elementos relacionados a eventos.
"""

class Event:
    """
    Classe base para todos os eventos da aplicação.
    """

    pass


class InputEvent(Event):
    """
    Input de usuário.
    """

    __slots__ = ('key',)

    def __init__(self, key):
        self.key = key


class OperationEvent(Event):
    """
    Operação a ser realizada.
    """

    __slots__ = ('operator', 'operands')

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands


class ResultEvent(Event):
    """
    Resultado de uma operação realizada.
    """

    __slots__ = ('value',)

    def __init__(self, value):
        self.value = value


class ErrorEvent(Event):
    """
    Erro ocorrido durante processamento de um evento.
    """

    __slots__ = ('source', 'error', 'type', 'description')

    def __init__(self, source_event:Event, error:Exception):
        if not isinstance(source_event, Event):
            raise TypeError("'source_event' needs to be a Event instance.")

        if not isinstance(error, Exception):
            raise TypeError("'error' needs to be a Exception instance.")

        self.source = source_event
        self.error = error
        self.type = error.__class__.__name__
        self.description = str(error)


