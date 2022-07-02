from FunctionalMetabolicType import FunctionalMetabolicType

if (__name__ == '__main__'):
    testType = 'developmental'
    functionalMetabolicType = FunctionalMetabolicType(testType, True)
    
    metabolicType = functionalMetabolicType.calculate([13, 13, 1, 14, 2, 3, 0, 25, 12, 16, 4, 12])
    groups = functionalMetabolicType.groupTotals
    subtype = functionalMetabolicType.calculateSubType(metabolicType)
    
    print('\r\n{0} Test {1}{2}{3}{4}'.format(
        testType,
        '\r\nGroup A: {0}'.format(groups['A']),
        '\r\nGroup B: {0}'.format(groups['B']),
        '\r\nGroup C: {0}'.format(groups['C']),
        '\r\nGroup D: {0}'.format(groups['D'])))
    print('\r\n{0} Metabolic Type: {1}'.format(testType, metabolicType))
    print('Sub Type: {0}'.format(subtype))
