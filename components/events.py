"""
Módulo que contém todos os elementos relacionados a eventos.
"""

from queue import Queue

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


class EventBus:
    """
    Classe responsável por distribuir os eventos entre todas as conexões
    habilitadas.
    """

    connections = {}

    def _subscribe(self, connection):
        """
        Habilita uma conexão a receber eventos.
        """
        
        EventBus.connections[connection] = Queue()

    
    def _unsubscribe(self, connection):
        """
        Desabilita uma conexão a receber eventos
        """

        del EventBus.connections[connection]        

    
    def connect(self):
        """
        Cria e retorna uma conexão ao `EventBus`.
        """
        
        return EventBus._get_connection(self)


    def _notify_all(self, event:Event, source):
        """
        Distribui um evento a todas as conexões habilitadas.
        """

        if not isinstance(event, Event):
            raise TypeError("'event' needs to be a Event instance.")

        for connection in self.connections:
            if connection is source:
                continue

            self._notify(connection, event)
        

    def _notify(self, connection, event:Event):
        """
        Insere um evento na fila de eventos a serem consumidos por uma conexão.
        """

        self.connections[connection].put(event)


    def _get_event_queue_size(self, connection):
        """
        Retorna a quantidade de eventos pendentes de serem consumidos por uma
        conexão.
        """

        queue = self.connections[connection]
        return queue.qsize()


    def _get_event(self, connection):
        """
        Retorna o próximo evento pendente a ser consumido por uma conexão.
        Caso não haja evento pendente, retorna `None`.
        """

        queue = self.connections[connection]
        if queue.qsize():
            return queue.get()

        return None


    @classmethod
    def _get_connection(cls, bus):
        """
        Retorna uma conexão ao `EventBus`, já habilitada a receber eventos.
        """

        class EventBusConnection:
                
            def send_event(self, event:Event):
                """
                Envia um evento ao `EventBus`.
                """

                bus._notify_all(event, self)
            
            
            def receive_event(self):
                """
                Recebe um evento do `EventBus`. Caso não tenha evento pendente,
                retorna `None`.
                """
                return bus._get_event(self)


            def close(self):
                """
                Desabilita a conexão a receber eventos do `EventBus`. Após a
                chamada deste método, a fila de eventos desta conexão será
                excluída.
                """

                bus._unsubscribe(self)

            
            def __len__(self):
                return bus._get_event_queue_size(self)

        cnx = EventBusConnection()
        bus._subscribe(cnx)
        return cnx