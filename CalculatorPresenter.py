class CalculatorPresenter:
    def __init__(self, view, calculator):
        self.view = view
        self.calculator = calculator
        self.first_argument = None
        self.second_argument = None
        self.result = '0'
        self.operation = ''

    def set_first_argument(self, argument):
        try:
            self.first_argument = float(argument)
        except ValueError:
            self.view.display_error('Invalid argument')
            self.first_argument = 0.0

    def set_second_argument(self, argument):
        try:
            self.second_argument = float(argument)
        except ValueError:
            self.view.display_error('Invalid argument')
            self.second_argument = 0.0

    def read_event(self, event):
        if event in ['+', '-', '÷', '×', ]:
            self.operator_clicked(event)
        elif event == 'C':
            self.cansel_clicked()
        elif event == '⌫':
            self.view.delete()
        elif event == '.':
            if self.view.text.get().count('.') < 1:
                self.view.update_text(event)
        elif event == '±':
            self.view.plus_minus_clicked()
        elif event == '%':
            self.percent_clicked()
        elif event == '=':
            self.set_second_argument(self.view.text.get())
            self.equally_clicked()
        else:
            self.numpad_clicked(event)

    def start(self):
        while True:
            event, values = self.view.window.read()
            if event in (None,):
                break
            else:
                self.read_event(event)
        self.view.window.close()

    def operator_clicked(self, event):
        self.operation = event
        self.set_first_argument(self.view.text.get())
        self.view.update_text(event)
        self.view.operator(event)

    def numpad_clicked(self, event):
        self.view.numpad(event)

    def percent_clicked(self):
        try:
            self.view.text.update(float(self.view.text.get()) / 100)
        except ValueError:
            self.cansel_clicked()
            self.view.display_error('error')

    def equally_clicked(self, ):
        if self.operation == '+':
            self.plus_clicked()
        elif self.operation == '-':
            self.minus_clicked()
        elif self.operation == '×':
            self.multiply_clicked()
        elif self.operation == '÷':
            if self.second_argument == 0:
                self.cansel_clicked()
                self.view.display_error('/ by zero')
                return
            else:
                self.divide_clicked()
        self.view.display_result(self.result)

    def cansel_clicked(self, ):
        self.view.cansel()
        self.first_argument = None
        self.second_argument = None
        self.operation = ''
        self.result = '0'

    def plus_clicked(self, ):
        self.result = self.calculator.sum(self.first_argument, self.second_argument)

    def minus_clicked(self, ):
        self.result = self.calculator.subtract(self.first_argument, self.second_argument)

    def multiply_clicked(self, ):
        self.result = self.calculator.multiply(self.first_argument, self.second_argument)

    def divide_clicked(self, ):
        self.result = self.calculator.divide(self.first_argument, self.second_argument)
