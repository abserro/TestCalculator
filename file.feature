Feature: Calculator test

  Scenario: Calculator interface simple test
    Given start
    When I wanna press '123' buttons
    Then I should have '123'

  Scenario: Calculator interface with point test
    Given start
    When I wanna press '1.23' buttons
    Then I should have '1.23'

  Scenario: Calculator plus test
    Given start
    When I wanna press '3+1=' buttons
    Then I should have '4.0'

  Scenario: Calculator double plus test
    Given start
    When I wanna press '3.4+1.5=' buttons
    Then I should have '4.9'

  Scenario: Calculator minus test
    Given start
    When I wanna press '1-3=' buttons
    Then I should have '-2.0'

  Scenario: Calculator double minus test
    Given start
    When I wanna press '1.3-3.1=' buttons
    Then I should have '-1.8'

  Scenario: Calculator divide test
    Given start
    When I wanna press '2÷2=' buttons
    Then I should have '1.0'

  Scenario: Calculator double divide test
    Given start
    When I wanna press '3.2÷0.4=' buttons
    Then I should have '8.0'

  Scenario: Calculator divide by zero test
    Given start
    When I wanna press '3÷0=' buttons
    Then I should have '/ by zero'

  Scenario: Calculator multyply test
    Given start
    When I wanna press '3×3=' buttons
    Then I should have '9.0'

  Scenario: Calculator multyply with 0 test
    Given start
    When I wanna press '3×0=' buttons
    Then I should have '0.0'

  Scenario: Calculator double multyply with 0 test
    Given start
    When I wanna press '0.35×5.0=' buttons
    Then I should have '1.75'

  Scenario: Calculator plus with big num
    Given start
    When I wanna press '100000000+100000000=' buttons
    Then I should have '200000000.0'

  Scenario: Calculator plus with small num
    Given start
    When I wanna press '0.00000001+0.00000001=' buttons
    Then I should have '2e-08'

  Scenario: Calculator percent test
    Given start
    When I wanna press '1%' buttons
    Then I should have '0.01'

  Scenario: Calculator plus_minus test
    Given start
    When I wanna press '1±' buttons
    Then I should have '-1'

  Scenario: Calculator plus_minus in ex test
    Given start
    When I wanna press '1±÷2=' buttons
    Then I should have '-0.5'

  Scenario: Calculator input wrong test
    Given start
    When I wanna press '+-2=÷2=' buttons
    Then I should have '-1.0'

  Scenario: Calculator input three agrs test
    Given start
    When I wanna press '1-2.0+5.1=' buttons
    Then I should have '7.1'

  Scenario: Calculator input try broke sum test
    Given start
    When I wanna press '+.3+2.=' buttons
    Then I should have '2.3'

  Scenario: Calculator mix operators test
    Given start
    When I wanna press '2+-×÷±%' buttons
    Then I should have 'error'

