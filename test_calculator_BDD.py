from pytest_bdd import scenario, given, when, then, parsers, scenarios
from CalculatorPresenter import CalculatorPresenter
from CalculatorView import CalculatorView
from Calculator import Calculator

FEATURE_FILE = 'file.feature'


@scenario(FEATURE_FILE, 'Calculator interface simple test')
@scenario(FEATURE_FILE, 'Calculator interface with point test')
@scenario(FEATURE_FILE, 'Calculator plus test')
@scenario(FEATURE_FILE, 'Calculator double plus test')
@scenario(FEATURE_FILE, 'Calculator minus test')
@scenario(FEATURE_FILE, 'Calculator double minus test')
@scenario(FEATURE_FILE, 'Calculator divide test')
@scenario(FEATURE_FILE, 'Calculator double divide test')
@scenario(FEATURE_FILE, 'Calculator divide by zero test')
@scenario(FEATURE_FILE, 'Calculator multyply test')
@scenario(FEATURE_FILE, 'Calculator multyply with 0 test')
@scenario(FEATURE_FILE, 'Calculator double multyply with 0 test')
@scenario(FEATURE_FILE, 'Calculator plus with big num')
@scenario(FEATURE_FILE, 'Calculator plus with small num')
@scenario(FEATURE_FILE, 'Calculator percent test')
@scenario(FEATURE_FILE, 'Calculator plus_minus test')
@scenario(FEATURE_FILE, 'Calculator plus_minus in ex test')
@scenario(FEATURE_FILE, 'Calculator input wrong test')
@scenario(FEATURE_FILE, 'Calculator input three agrs test')
@scenario(FEATURE_FILE, 'Calculator input try broke sum test')
@scenario(FEATURE_FILE, 'Calculator mix operators test')
def test_calculator():
    pass


@given("start", target_fixture="test")
def start():
    view = CalculatorView()
    calculator = Calculator()
    presenter = CalculatorPresenter(view, calculator)
    presenter.view.window.read(timeout=0.00001, timeout_key='Exit')
    return {"presenter": presenter}


@when(parsers.parse("I wanna press '{buttons:S}' buttons"))
def press_buttons(test, buttons):
    for button in buttons:
        test["presenter"].read_event(button)


@then(parsers.parse("I should have '{result}'"))
def check_result(test, result):
    assert test["presenter"].view.text.get() == result
