"""
Ponto de entrada da aplicação, que define como os elementos irão se conectar.
"""

from components.interface import Visual
from components.engine import Processor

cpu = Processor()
app = Visual()
app.subscribe(cpu.receive_event)
app.run()