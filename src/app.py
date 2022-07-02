from FunctionalMetabolicType import FunctionalMetabolicType

if (__name__ == '__main__'):
    functionalMetabolicType = FunctionalMetabolicType(True)
    
    metabolicType = functionalMetabolicType.calculate([103, 44, 37, 133, 97, 89, 57, 137, 108, 171, 109, 64])
    groups = functionalMetabolicType.groupTotals
    subtype = functionalMetabolicType.calculateSubType(metabolicType)
    
    print('\r\nFunctional Test A{0}{1}{2}{3}'.format(
        '\r\nGroup A: {0}'.format(groups['A']),
        '\r\nGroup B: {0}'.format(groups['B']),
        '\r\nGroup C: {0}'.format(groups['C']),
        '\r\nGroup D: {0}'.format(groups['D'])))
    print('\r\nFunctional Metabolic Type: {0}'.format(metabolicType))
    print('Sub Type: {0}'.format(subtype))
