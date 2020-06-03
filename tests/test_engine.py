import unittest
from components.engine import Processor

class TestProcessor(unittest.TestCase):
    
    def setUp(self):
        self.processor = Processor()


    def test_add(self):
        add = self.processor.add
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(1, 0), 1)
        self.assertEqual(add(0, -1), -1)
        self.assertEqual(add(-1, 0), -1)
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(add(1, -1), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)


    def test_sub(self):
        sub = self.processor.sub
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(0, 1), -1)
        self.assertEqual(sub(1, 0), 1)
        self.assertEqual(sub(0, -1), 1)
        self.assertEqual(sub(-1, 0), -1)
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(1, -1), 2)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)

    
    def test_multiply(self):
        multiply = self.processor.multiply
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(0, -1), 0)
        self.assertEqual(multiply(-1, 0), 0)
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(1, -1), -1)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    
    def test_divide(self):
        divide = self.processor.divide
        self.assertRaises(ZeroDivisionError, divide, 0, 0)
        self.assertEqual(divide(0, 1), 0)
        self.assertRaises(ZeroDivisionError, divide, 1, 0)
        self.assertEqual(divide(0, -1), 0)
        self.assertRaises(ZeroDivisionError, divide, -1, 0)
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(divide(1, -1), -1)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)

    
    def test_translate(self):
        translate = self.processor.translate
        self.assertRaises(NotImplementedError, translate, '')
        self.assertEqual(translate('+'), self.processor.add)
        self.assertEqual(translate('-'), self.processor.sub)
        self.assertEqual(translate('*'), self.processor.multiply)
        self.assertEqual(translate('/'), self.processor.divide)

    
    def test_receive_event(self):
        from components.events import (
            OperationEvent,
            Event,
            ErrorEvent,
            ResultEvent,
        )

        process = self.processor.receive_event

        # Evento diferente de `OperationEvent` é ignorado
        empty_event = Event()
        resp_empty_event = process(empty_event)
        self.assertIsNone(resp_empty_event)

        # `OperationEvent` válido é processado e devolvido um `ResultEvent`
        # com valor correto
        sum_event = OperationEvent('+', (1, 1))
        resp_sum_event = process(sum_event)
        self.assertIsInstance(resp_sum_event, ResultEvent)
        self.assertEqual(resp_sum_event.value, 2)

        # `OperationEvent` inválido é processado e devolvido um `ErrorEvent`
        wrong_event = OperationEvent('', None)
        resp_wrong_event = process(wrong_event)
        self.assertIsInstance(resp_wrong_event, ErrorEvent)
        self.assertIsInstance(resp_wrong_event.error, NotImplementedError)
        self.assertEqual(resp_wrong_event.type, 'NotImplementedError')
        self.assertEqual(resp_wrong_event.description, "Unknow operator ''")
        self.assertEqual(resp_wrong_event.source, wrong_event)
        
        wrong_event = OperationEvent('/', (1, 0))
        resp_wrong_event = process(wrong_event)
        self.assertIsInstance(resp_wrong_event, ErrorEvent)
        self.assertIsInstance(resp_wrong_event.error, ZeroDivisionError)
        self.assertEqual(resp_wrong_event.source, wrong_event)