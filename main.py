from Calculator import Calculator
from CalculatorPresenter import CalculatorPresenter
from CalculatorView import CalculatorView

if __name__ == '__main__':
    presenter = CalculatorPresenter(CalculatorView(), Calculator())
    presenter.start()
