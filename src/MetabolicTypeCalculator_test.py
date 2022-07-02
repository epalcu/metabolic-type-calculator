import json
import pytest_check as check
from MetabolicTypeCalculator import MetabolicTypeCalculator

def test_calculate_multipleCases():
    cases = json.load(open('metabolicTestCases.json'))
    testTypes = [
        'functional', 
        'developmental'
    ]

    for case in cases:
        for testType in testTypes:
            # Arrange
            metabolicTypeCalculator = MetabolicTypeCalculator(testType, False)
            testMsg = 'Test case id: {0}; test type: {1}'.format(case['id'], testType)
            
            # Act
            metabolicType = metabolicTypeCalculator.calculate(case[testType]['columns'])
            subType = metabolicTypeCalculator.calculateSubType(metabolicType)

            # Assert
            check.equal(metabolicTypeCalculator.groupTotals, case[testType]['groups'], testMsg)
            check.equal(metabolicType, case[testType]['type'], testMsg)
            check.equal(subType, case[testType]['subType'], testMsg)
        