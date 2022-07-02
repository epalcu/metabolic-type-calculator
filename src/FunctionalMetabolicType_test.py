import json
import pytest_check as check
from FunctionalMetabolicType import FunctionalMetabolicType

def test_calculate_multipleCases():
    cases = json.load(open('functionalTestCases.json'))

    for case in cases:
        # Arrange
        functionalMetabolicType = FunctionalMetabolicType(False)
        testMsg = 'Test case id: {0}'.format(case['id'])
        
        # Act
        metabolicType = functionalMetabolicType.calculate(case['columns'])
        subType = functionalMetabolicType.calculateSubType(metabolicType)

        # Assert
        check.equal(functionalMetabolicType.groupTotals, case['groups'], testMsg)
        check.equal(metabolicType, case['type'], testMsg)
        check.equal(subType, case['subType'], testMsg)
        