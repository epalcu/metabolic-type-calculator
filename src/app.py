import json
from MetabolicTypeCalculator import MetabolicTypeCalculator

if (__name__ == '__main__'):
    testColumns = json.load(open('testColumns.json'))
    testTypes = [
        'functional',
        'developmental'
    ]

    for testType in testTypes:
        metabolicTypeCalculator = MetabolicTypeCalculator(testType, False)
        
        metabolicType = metabolicTypeCalculator.calculate(testColumns[testType])
        groups = metabolicTypeCalculator.groupTotals
        subtype = metabolicTypeCalculator.calculateSubType(metabolicType)
        
        print('\r\n{0} Test {1}{2}{3}{4}'.format(
            testType,
            '\r\nGroup A: {0}'.format(groups['A']),
            '\r\nGroup B: {0}'.format(groups['B']),
            '\r\nGroup C: {0}'.format(groups['C']),
            '\r\nGroup D: {0}'.format(groups['D'])))
        print('\r\n{0} Metabolic Type: {1}'.format(testType, metabolicType))
        print('Sub Type: {0}'.format(subtype))
