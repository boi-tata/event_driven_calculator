"""
Ponto de entrada da aplicação, que define como os elementos irão se conectar.
"""

from interface import Visual
from engine import Processor

cpu = Processor()
app = Visual()
app.subscribe(cpu.receive_event)
app.run()