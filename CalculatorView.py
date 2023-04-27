import PySimpleGUI as sg


class CalculatorView:
    def __init__(self):
        self.text = sg.InputText('0', readonly=True, justification='r')
        self.buttons = self.set_buttons()
        self.layout = [[self.text],
                       [self.buttons], ]
        self.window = self.set_window()

    def set_buttons(self, ):
        button_color = ('black', '#d5dce8')
        buttons = [[sg.Button('C'), sg.Button('⌫'), sg.Button('%'), sg.Button('×')],
                   [sg.Button('7', button_color=button_color, enable_events=True),
                    sg.Button('8', button_color=button_color, ),
                    sg.Button('9', button_color=button_color, ), sg.Button('÷')],
                   [sg.Button('4', button_color=button_color, ), sg.Button('5', button_color=button_color, ),
                    sg.Button('6', button_color=button_color, ), sg.Button('+')],
                   [sg.Button('1', button_color=button_color, ), sg.Button('2', button_color=button_color, ),
                    sg.Button('3', button_color=button_color, ), sg.Button('-')],
                   [sg.Button('.', button_color=button_color, ), sg.Button('0', button_color=button_color, ),
                    sg.Button('±', button_color=button_color, ), sg.Button('=')], ]
        return buttons

    def set_window(self, ):
        sg.theme('BlueMono')
        title = 'Calculator.py'
        font = ('Calibri', 16)
        size = (313, 430)
        return sg.Window(title,
                         self.layout,
                         default_button_element_size=(5, 2),
                         auto_size_buttons=False,
                         font=font,
                         size=size)

    def cansel(self, ):
        self.text.update('0')

    def delete(self, ):
        if self.text.get() != '0' and len(self.text.get()) == 1:
            self.text.update('0')
        else:
            self.text.update(self.text.get()[:-1])

    def update_text(self, new_text):
        if self.text.get() == '0' and new_text != '.':
            self.text.update(new_text)
        elif new_text in ['+', '-', '÷', '×', ]:
            self.text.update(new_text)
        elif self.text.get() in ['+', '-', '÷', '×', ]:
            self.text.update(new_text)
        else:
            self.text.update(self.text.get() + new_text)

    def numpad(self, event):
        self.update_text(event)

    def operator(self, event):
        self.update_text(event)

    def plus_minus_clicked(self, ):
        if self.text.get() != '':
            if self.text.get()[0] == '-':
                self.text.update(self.text.get()[1:])
            else:
                self.text.update('-' + self.text.get())

    def display_result(self, result):
        self.text.update(result)

    def display_error(self, error):
        self.text.update(error)
