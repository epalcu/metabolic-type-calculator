import operator

class FunctionalMetabolicType():
    #
    # Constructor
    #
    def __init__(self):
        self.metabolicType = 0
        self.columns = {}
        self.sortedColumns = []
        self.groupTotals = {}
        self.groupColumns = {}
        self.sortedGroups = []

    #
    # Public Methods
    # 
    def calculate(self, columnsList):
        self._setColumns(columnsList)
        self._step2()
        self._step3()
        self._step8()
        self._step9()
        self._step10()
        
        if (len(self.sortedGroups) > 0):
            if (self.sortedGroups[0][0] == 'A'):
                self._step4()
            elif (self.sortedGroups[0][0] == 'B'):
                self._step5()
            elif (self.sortedGroups[0][0] == 'C'):
                self._step6()
            elif (self.sortedGroups[0][0] == 'D'):
                self._step7()

        print('Your Functional Metabolic Type: {0}'.format(self.metabolicType))
        return self.metabolicType

    #
    # Private Methods
    # 
    def _step7(self):
        if (self.metabolicType > 0):
            return

    def _step6(self):
        if (self.metabolicType > 0):
            return

    def _step5(self):
        if (self.metabolicType > 0):
            return

    def _step4(self):
        if (self.metabolicType > 0):
            return

    def _step10(self):
        if (self.metabolicType > 0):
            return
        
        groupsWithSameTotals = self._getGroupsWithSameTotals()
        if (len(groupsWithSameTotals) == 2):
            print('Step 10: Two groups are the same value: {0}'.format(groupsWithSameTotals))
            
            twoOrMore = 0
            columnsForFirstGroup = self.groupColumns[groupsWithSameTotals[0]]
            columnsForSecondGroup = self.groupColumns[groupsWithSameTotals[1]]
            firstSortedColumnValue = self.sortedColumns[0][1]
            secondSortedColumnValue = self.sortedColumns[1][1]
            for column in sum([columnsForFirstGroup, columnsForSecondGroup], []):
                columnValue = self.columns[str(column)]
                if (columnValue == firstSortedColumnValue and firstSortedColumnValue > secondSortedColumnValue):
                    print('Step 10: Column has higher value than any other column: {0}'.format(column))
                    self.metabolicType = column
                    break
                elif (columnValue == firstSortedColumnValue):
                    twoOrMore += 1

            self._checkIfColumnsSameHighestTotal(twoOrMore, firstSortedColumnValue)

    def _checkIfColumnsSameHighestTotal(self, twoOrMore, firstSortedColumnValue):
        if (self.metabolicType > 0):
            return

        if (twoOrMore > 2 or (self.columns['1'] == firstSortedColumnValue and self.columns['4'] == firstSortedColumnValue)):
            print('Step 10: Columns 1 and 4 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 1
        elif (self.columns['4'] == firstSortedColumnValue and self.columns['6'] == firstSortedColumnValue):
            print('Step 10: Columns 4 and 6 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 4
        elif (self.columns['2'] == firstSortedColumnValue and self.columns['5'] == firstSortedColumnValue):
            print('Step 10: Columns 2 and 5 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 2
        elif (self.columns['5'] == firstSortedColumnValue and self.columns['7'] == firstSortedColumnValue):
            print('Step 10: Columns 2 and 5 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 5
        elif (self.columns['3'] == firstSortedColumnValue and self.columns['6'] == firstSortedColumnValue):
            print('Step 10: Columns 2 and 5 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 3
        elif (self.columns['3'] == firstSortedColumnValue and self.columns['7'] == firstSortedColumnValue):
            print('Step 10: Columns 2 and 5 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 3
        elif (self.columns['11'] == firstSortedColumnValue and self.columns['12'] == firstSortedColumnValue):
            print('Step 10: Columns 2 and 5 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self.metabolicType = 10
        else:
            print('Step 10: No two or more columns have higher values than any other column.')
            self.metabolicType = 8


    def _getGroupsWithSameTotals(self):
        totals = {}
        sameTotals = []
        for key in self.groupTotals:
            if self.groupTotals[key] in totals:
                totals[self.groupTotals[key]].append(key)
                sameTotals = totals[self.groupTotals[key]][:]
            else:
                totals[self.groupTotals[key]] = [key]

        return sameTotals
        

    def _step9(self):
        if (self.metabolicType > 0):
            return
        
        groupsWithSameTotals = self._getGroupsWithSameTotals()
        if (len(groupsWithSameTotals) == 3):
            print('Step 9: Three groups are the same value: {0}'.format(groupsWithSameTotals))
            self.metabolicType = 8

    def _step8(self):
        if (self.metabolicType > 0):
            return
        
        groupsSet = set(self.groupTotals.values())
        if (len(groupsSet) == 1):
            print('Step 8: All groups are the same value: {0}'.format(list(groupsSet)[0]))
            self.metabolicType = 8
        
    def _step3(self):
        if (self.metabolicType > 0):
            return

        self.groupTotals = {
            'A': self.columns['1'] + self.columns['4'] + self.columns['6'] + self.columns['11'],
            'B': self.columns['2'] + self.columns['5'] + self.columns['7'] + self.columns['12'],
            'C': self.columns['8'] + self.columns['9'] + self.columns['10'],
            'D': self.columns['3'] + self.columns['6'] + self.columns['7']
        }

        print('Step 3: Set groups totals: {0}'.format(self.groupTotals))

        self.groupColumns = {
            'A': [1, 4, 6, 11],
            'B': [2, 5, 7, 12],
            'C': [8, 9, 10],
            'D': [3, 6, 7]
        }
        
        print('Step 3: Set groups columns: {0}'.format(self.groupColumns))

        self.sortedGroups = sorted(self.groupTotals.items(), key=operator.itemgetter(1), reverse=True)

    def _step2(self):
        highestColumnValue = self.sortedColumns[0]
        if (highestColumnValue[1] >= 25):
            print('Step 2: Highest column value {0} is greater than or equal to 25.'.format(highestColumnValue[1]))
            self.metabolicType = int(highestColumnValue[0])

    def _setColumns(self, columnsList):
        self.columns = {
            '1': columnsList[0],
            '2': columnsList[1],
            '3': columnsList[2],
            '4': columnsList[3],
            '5': columnsList[4],
            '6': columnsList[5],
            '7': columnsList[6],
            '8': columnsList[7],
            '9': columnsList[8],
            '10': columnsList[9],
            '11': columnsList[10],
            '12': columnsList[11]
        }
        print('Set columns: {0}'.format(self.columns))

        self.sortedColumns = sorted(self.columns.items(), key=operator.itemgetter(1), reverse=True)