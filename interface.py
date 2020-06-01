"""
Módulo contendo todos os elementos que fazem interface com o usuário.
"""

import PySimpleGUI as sg
from events import (
    OperationEvent,
    ErrorEvent,
    ResultEvent,
    InputEvent,
)

class Visual:
    """
    Classe para gerar interface gráfica.
    """
    
    def __init__(self): # Método construtor da classe
        self.display = sg.Text(
            '',
            relief='solid',
            border_width=2,
            background_color='white',
            text_color='black',
            size=(11, 1),
            justification='right',
        )
        first_line = [
            sg.Button('7'),
            sg.Button('8'),
            sg.Button('9'),
            sg.Button('+'),
        ]
        second_line = [
            sg.Button('4'),
            sg.Button('5'),
            sg.Button('6'),
            sg.Button('-'),
        ]
        third_line = [
            sg.Button('1'),
            sg.Button('2'),
            sg.Button('3'),
            sg.Button('*'),
        ]
        fourth_line = [
            sg.Button('0'),
            sg.Button('C'),
            sg.Button('='),
            sg.Button('/'),
        ]
        layout = [
            [self.display],
            first_line,
            second_line,
            third_line,
            fourth_line,
        ]
        self.window = sg.Window('Calculadora', layout, size=(50, 170))
        self.observers = []


    def run(self):
        """
        Inicia a execução da interface gráfica (leitura e processamento de
        eventos)
        """
        clear_display = False
        operand = None
        operation = None
        
        while True:
            event, _ = self.window.read() # Esperando um evento acontecer

            if event is None:	# Caso a janela seja fechada
                break
            
            # Daqui pra baixo, estamos filtrando que tipo de evento
            # ocorreu, e determinamos o que faremos em cada caso
            
            if event == 'c': # Botão CLEAR
                clear_display = self.update_display('')
                operand = None
                operation = None
            elif event == '=': # Resposta da operação solicitada
                value_of_display = int(self.display.Get())
                # Notificando todos os observers sobre o evento, e guardando
                # o resultado do primeiro que responder com um `ResultEvent`
                op = OperationEvent(operation, (operand, value_of_display))
                response = self.notifyAll(op)
                if isinstance(response, ErrorEvent):
                    # Caso a resposta seja um erro qualquer
                    clear_display = self.update_display('DEU RUIM AQUI')
                elif isinstance(response, ResultEvent):
                    # Caso a resposta seja um resultado
                    clear_display = self.update_display(str(response.value))
            elif event.isdigit(): # Um dígito foi pressionado
                # Verificando se precisa apagar o display antes de concatenar
                # os dígitos
                if clear_display:
                    clear_display = self.update_display('')
                # Concatenando os dígitos
                new_value = self.display.Get() + event
                self.update_display(new_value)
                # Na operação de cima, não salvamos o retorno do método pq não
                # queremos alterar o estado da variável `clear_display`
            else: # Uma operação foi inclusa
                operand = int(self.display.Get())
                operation = event
                clear_display = True
        
        self.window.close()
    
    def notifyAll(self, event):
        """
        Notifica todos os observadores sobre um evento ocorrido, e retorna
        a primeira resposta do tipo `ResultError` ou `ErrorEvent`. Caso nenhum
        observador responda, retorna `None`.
        """

        for obs in self.observers:
            response = obs(event)
            if isinstance(response, (ResultEvent, ErrorEvent)):
                return response
    
    def subscribe(self, observer):
        """
        Habilita um observador a receber eventos.
        """

        self.observers.append(observer)

    def update_display(self, value:str) -> bool:
        """
        Atualiza o display com o valor informado, e retorna se é necessario
        apagar o display no próximo evento, conforme o novo valor no display.
        """

        self.display.Update(value=value)
        return bool(value)