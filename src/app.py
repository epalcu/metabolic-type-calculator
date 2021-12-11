from FunctionalMetabolicType import FunctionalMetabolicType

if (__name__ == '__main__'):
    functionalMetabolicType = FunctionalMetabolicType()
    metabolicType = functionalMetabolicType.calculate([
        12,
        11,
        10,
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        2,
        1
    ])
    subtype = functionalMetabolicType.calculateSubtype(metabolicType)

    print('Your functional metabolic type: {0}'.format(metabolicType))
    print('Your functional metabolic subtype: {0}'.format(subtype))
