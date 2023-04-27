import unittest
from unittest.mock import MagicMock
from Calculator import Calculator
from CalculatorPresenter import CalculatorPresenter
from CalculatorView import CalculatorView


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls._view = CalculatorView()
        cls._calculator = Calculator()
        cls._presenter = CalculatorPresenter(cls._view, cls._calculator)
        cls._view.window.read(timeout=0.00001, timeout_key='Exit')

    def test_press_plus_minus_check_call(self, ):
        self._view.plus_minus_clicked = MagicMock()
        self._presenter.read_event('±')
        self.assertEqual(1, self._view.plus_minus_clicked.call_count)

    def test_press_plus_minus(self, ):
        expected_result = '1'
        self._view.text.update('-1')
        self._presenter.read_event('±')
        self.assertEqual(expected_result, self._view.text.get())

    def test_press_percent_check_call(self, ):
        self._presenter.percent_clicked = MagicMock()
        self._presenter.read_event('%')
        self.assertEqual(1, self._presenter.percent_clicked.call_count)

    def test_press_percent(self, ):
        expected_result = '12.34'
        self._view.text.update('1234')
        self._presenter.read_event('%')
        self.assertEqual(expected_result, self._view.text.get())

    def test_press_point_check_call(self, ):
        self._view.update_text = MagicMock()
        self._presenter.read_event('.')
        self.assertEqual(1, self._view.update_text.call_count)

    def test_press_point(self, ):
        expected_result = '12.'
        self._view.text.update('12')
        self._view.update_text('.')
        self.assertEqual(expected_result, self._view.text.get())

    def test_press_cansel_check_call(self, ):
        self._view.cansel = MagicMock()
        self._presenter.read_event('C')
        self.assertEqual(1, self._view.cansel.call_count)

    def test_press_cansel(self, ):
        expected_result = '0'
        self._view.text.update('123.678')
        self._view.cansel()
        self.assertEqual(expected_result, self._view.text.get())

    def test_press_delete_check_call(self, ):
        self._view.delete = MagicMock()
        self._presenter.read_event('⌫')
        self.assertEqual(1, self._view.delete.call_count)

    def test_press_delete(self, ):
        expected_result = '0'
        self._view.text.update('1')
        self._view.delete()
        self.assertEqual(expected_result, self._view.text.get())

    def test_press_numpad_check_call(self, ):
        for i in range(10):
            self.setUp()
            self._view.numpad = MagicMock()
            self._presenter.read_event(str(i))
            with self.subTest(i=i):
                self.assertEqual(1, self._view.numpad.call_count)

    def test_press_numpad(self, ):
        for i in range(10):
            expected_result = str(i)
            self.setUp()
            self._presenter.read_event(str(i))
            with self.subTest(i=i):
                self.assertEqual(expected_result, self._view.text.get())

    def test_press_operator_check_call(self, ):
        for op in ['+', '-', '÷', '×']:
            self.setUp()
            self._view.operator = MagicMock()
            self._presenter.read_event(op)
            with self.subTest(i=op):
                self.assertEqual(1, self._view.operator.call_count)

    def test_press_operator(self, ):
        for op in ['+', '-', '÷', '×']:
            expected_result = op
            self.setUp()
            self._presenter.read_event(op)
            with self.subTest(i=op):
                self.assertEqual(expected_result, self._view.text.get())

    def test_display_result(self, ):
        expected_result = 0
        self._view.display_result(expected_result)
        self.assertEqual(str(expected_result), self._view.text.get())

    def test_display_error(self, ):
        expected_result = 'error'
        self._view.display_error(expected_result)
        self.assertEqual(str(expected_result), self._view.text.get())

    def test_press_equally_plus(self, ):
        expected_result = 0
        self._calculator.sum = MagicMock(return_value=expected_result)
        self._presenter.read_event('2')
        self._presenter.read_event('+')
        self._presenter.read_event('3')
        self._presenter.read_event('=')
        self.assertEqual(str(expected_result), self._view.text.get())

    def test_press_equally_minus(self, ):
        expected_result = 0
        self._calculator.subtract = MagicMock(return_value=expected_result)
        self._presenter.read_event('2')
        self._presenter.read_event('-')
        self._presenter.read_event('3')
        self._presenter.read_event('=')
        self.assertEqual(str(expected_result), self._view.text.get())

    def test_press_equally_multiply(self, ):
        expected_result = 0
        self._calculator.multiply = MagicMock(return_value=expected_result)
        self._presenter.read_event('2')
        self._presenter.read_event('*')
        self._presenter.read_event('3')
        self._presenter.read_event('=')
        self.assertEqual(str(expected_result), self._view.text.get())

    def test_press_equally_divide(self, ):
        expected_result = 0
        self._calculator.divide = MagicMock(return_value=expected_result)
        self._presenter.read_event('2')
        self._presenter.read_event('/')
        self._presenter.read_event('3')
        self._presenter.read_event('=')
        self.assertEqual(str(expected_result), self._view.text.get())


if __name__ == 'main':
    unittest.main()
