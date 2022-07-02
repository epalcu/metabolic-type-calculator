from FunctionalMetabolicType import FunctionalMetabolicType

if (__name__ == '__main__'):
    functionalMetabolicType = FunctionalMetabolicType()
    metabolicType = functionalMetabolicType.calculate([
        115,
        69,
        14,
        88,
        110,
        50,
        40,
        174,
        106,
        214,
        137,
        87
    ])
    groups = functionalMetabolicType.groupTotals
    subtype = functionalMetabolicType.calculateSubtype(metabolicType)
    
    print('\r\nFunctional Test A{0}{1}{2}{3}'.format(
        '\r\nGroup A: {0}'.format(groups['A']),
        '\r\nGroup B: {0}'.format(groups['B']),
        '\r\nGroup C: {0}'.format(groups['C']),
        '\r\nGroup D: {0}'.format(groups['D'])))
    print('\r\nFunctional Metabolic Type: {0}'.format(metabolicType))
    print('Sub Type: {0}'.format(subtype))
