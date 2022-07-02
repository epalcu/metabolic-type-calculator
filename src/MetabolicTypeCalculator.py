import operator

class MetabolicTypeCalculator():
    #
    # Constructor
    #
    def __init__(self, testType, verbose=True):
        self.metabolicType = 0
        self.columns = {}
        self.sortedColumns = []
        self.groupTotals = {}
        self.groupColumns = {}
        self.sortedGroups = []
        self.verbose = verbose
        self.testType = testType

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
        
        if (len(self.sortedGroups) > 0 and self.metabolicType == 0):
            if (self.sortedGroups[0][0] == 'A'):
                self._step4('A')
            elif (self.sortedGroups[0][0] == 'B'):
                self._step5('B')
            elif (self.sortedGroups[0][0] == 'C'):
                self._step6('C')
            elif (self.sortedGroups[0][0] == 'D'):
                self._step7('D')

        return self.metabolicType

    def calculateSubType(self, metabolicType):
        del self.columns[str(metabolicType)]
        return int(sorted(self.columns.items(), key=operator.itemgetter(1), reverse=True)[0][0])

    #
    # Private Methods
    # 
    def _step7(self, group, step=7):
        sortedColumns = sorted(self.groupColumns[group]['dict'].items(), key=operator.itemgetter(1), reverse=True)
        highestColumn = sortedColumns[0]
        
        self._handleColumnsWithSameValue(group, step, highestColumn)
        self._setMetabolicType(highestColumn[0])

    def _step6(self, group, step=6):
        sortedColumns = sorted(self.groupColumns[group]['dict'].items(), key=operator.itemgetter(1), reverse=True)
        highestColumn = sortedColumns[0]
        
        self._handleColumnsWithSameValue(group, step, highestColumn)
        self._setMetabolicType(highestColumn[0])
        
    def _step5(self, group, step=5):
        sortedColumns = sorted(self.groupColumns[group]['dict'].items(), key=operator.itemgetter(1), reverse=True)
        highestColumn = sortedColumns[0]
        
        self._handleColumnsWithSameValue(group, step, highestColumn)
        self._setMetabolicType(highestColumn[0])

    def _step4(self, group, step=4):
        # part f
        sortedColumns = sorted(self.groupColumns[group]['dict'].items(), key=operator.itemgetter(1), reverse=True)
        highestColumn = sortedColumns[0]
        highestColumnValue = highestColumn[0]
        
        self._handleColumnsWithSameValue(group, step, highestColumn)
        if (highestColumnValue == 6):
            value = 4 if self.testType == 'functional' else 6
            self._setMetabolicType(value)
        else:
            self._setMetabolicType(highestColumnValue)
        
    def _handleColumnsWithSameValue(self, group, step, highestColumn=('0', 0)):
        groupColumnsSet = set(self.groupColumns[group]['values'])
        columnsWithSameTotals = self._getGroupsWithSameTotals(self.groupColumns[group]['dict'], toInt=True)
        if (len(groupColumnsSet) == 1 and (step == 4 or step == 5)  and list(groupColumnsSet)[0] > highestColumn[1]):
            self._printOutput('Step {0}: All columns within Group {1} are the same value: {2}'.format(step, group, list(groupColumnsSet)[0]))
            if (step == 4):
                self._setMetabolicType(1)
            elif (step == 5):
                self._setMetabolicType(2)
        elif (len(columnsWithSameTotals) == 3 and sorted(list(groupColumnsSet), reverse=True)[0] > highestColumn[1]):
            self._printOutput('Step {0}: Three columns within Group {1} are the same value: {2}'.format(step, group, columnsWithSameTotals))
            if (step == 6):
                self._setMetabolicType(8)
            elif (step == 7):
                self._setMetabolicType(3)
            else:
                self._setMetabolicType(sorted(columnsWithSameTotals)[0])
        elif (len(columnsWithSameTotals) == 2 and sorted(list(groupColumnsSet), reverse=True)[0] > highestColumn[1]):
            self._printOutput('Step {0}: Two columns within Group {1} are the same value: {2}'.format(step, group, columnsWithSameTotals))
            if (step == 7):
                self._setMetabolicType(3)
            else:
                self._setMetabolicType(sorted(columnsWithSameTotals)[0])

    def _step10(self):
        groupsWithSameTotals = self._getGroupsWithSameTotals(self.groupTotals)
        
        if (len(groupsWithSameTotals) > 0 and self.sortedGroups[0][1] > self.groupTotals[groupsWithSameTotals[0]]):
            self._printOutput(
                'Step 10: The two groups with the same value ({0}) are less than the highest group value ({1})'.format(
                  self.groupTotals[groupsWithSameTotals[0]],
                  self.sortedGroups[0][1]  
                ))
            return

        if (len(groupsWithSameTotals) == 2):
            self._printOutput('Step 10: Two groups are the same value: {0}'.format(groupsWithSameTotals))
            
            twoOrMore = 0
            columnsForFirstGroup = self.groupColumns[groupsWithSameTotals[0]]['columns']
            columnsForSecondGroup = self.groupColumns[groupsWithSameTotals[1]]['columns']
            firstSortedColumnValue = self.sortedColumns[0][1]
            secondSortedColumnValue = self.sortedColumns[1][1]
            for column in sum([columnsForFirstGroup, columnsForSecondGroup], []):
                columnValue = self.columns[str(column)]
                if (columnValue == firstSortedColumnValue and firstSortedColumnValue > secondSortedColumnValue):
                    self._printOutput('Step 10: Column has higher value than any other column: {0}'.format(column))
                    self._setMetabolicType(column)
                    break
                elif (columnValue == firstSortedColumnValue):
                    twoOrMore += 1

            self._checkIfColumnsSameHighestTotal(twoOrMore, firstSortedColumnValue)

    def _checkIfColumnsSameHighestTotal(self, twoOrMore, firstSortedColumnValue):
        if (twoOrMore > 2 or (self.columns['1'] == firstSortedColumnValue and self.columns['4'] == firstSortedColumnValue)):
            self._printOutput('Step 10: Columns 1 and 4 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(1)
        elif (self.columns['4'] == firstSortedColumnValue and self.columns['6'] == firstSortedColumnValue):
            self._printOutput('Step 10: Columns 4 and 6 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(4)
        elif (self.columns['2'] == firstSortedColumnValue and self.columns['5'] == firstSortedColumnValue):
            self._printOutput('Step 10: Columns 2 and 5 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(2)
        elif (self.columns['5'] == firstSortedColumnValue and self.columns['7'] == firstSortedColumnValue):
            self._printOutput('Step 10: Columns 5 and 7 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(5)
        elif (self.columns['3'] == firstSortedColumnValue and self.columns['6'] == firstSortedColumnValue):
            self._printOutput('Step 10: Columns 3 and 6 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(3)
        elif (self.columns['3'] == firstSortedColumnValue and self.columns['7'] == firstSortedColumnValue):
            self._printOutput('Step 10: Columns 3 and 7 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(3)
        elif (self.columns['11'] == firstSortedColumnValue and self.columns['12'] == firstSortedColumnValue and self.testType == 'functional'):
            self._printOutput('Step 10: Columns 11 and 12 have higher values than any other column: {0}'.format(firstSortedColumnValue))
            self._setMetabolicType(10)
        else:
            self._printOutput('Step 10: No two or more columns have higher values than any other column.')
            self._setMetabolicType(8)


    def _getGroupsWithSameTotals(self, d, toInt=False):
        totals = {}
        sameTotals = []
        for key in d:
            keyValue = str(key) if (not toInt) else int(key)
            if d[key] in totals:
                totals[d[key]].append(keyValue)
                sameTotals = totals[d[key]][:]
            else:
                totals[d[key]] = [keyValue]

        return sameTotals
        

    def _step9(self):
        groupsWithSameTotals = self._getGroupsWithSameTotals(self.groupTotals)
        
        if (len(groupsWithSameTotals) > 0 and self.sortedGroups[0][1] > self.groupTotals[groupsWithSameTotals[0]]):
            self._printOutput(
                'Step 9: The three groups with the same value ({0}) are less than the highest group value ({1})'.format(
                  self.groupTotals[groupsWithSameTotals[0]],
                  self.sortedGroups[0][1]  
                ))
            return

        if (len(groupsWithSameTotals) == 3):
            self._printOutput('Step 9: Three groups are the same value: {0}'.format(groupsWithSameTotals))
            self._setMetabolicType(8)

    def _step8(self):
        groupsSet = set(self.groupTotals.values())
        if (len(groupsSet) == 1):
            self._printOutput('Step 8: All groups are the same value: {0}'.format(list(groupsSet)[0]))
            self._setMetabolicType(8)
        
    def _step3(self):
        self.groupTotals = {
            'A': self.columns['1'] + self.columns['4'] + self.columns['6'] + self.columns['11'],
            'B': self.columns['2'] + self.columns['5'] + self.columns['7'] + self.columns['12'],
            'C': self.columns['8'] + self.columns['9'] + self.columns['10'],
            'D': self.columns['3'] + self.columns['6'] + self.columns['7']
        }

        self._printOutput('Step 3: Set groups totals: {0}'.format(self.groupTotals))

        self.groupColumns = {
            'A': {
                'columns': [1, 4, 6, 11],
                'values': [self.columns['1'], self.columns['4'], self.columns['6'], self.columns['11']],
                'dict': {
                    '1': self.columns['1'],
                    '4': self.columns['4'],
                    '6': self.columns['6'],
                    '11': self.columns['11']
                }
            },
            'B': {
                'columns': [2, 5, 7, 12],
                'values': [self.columns['2'], self.columns['5'], self.columns['7'], self.columns['12']],
                'dict': {
                    '2': self.columns['2'],
                    '5': self.columns['5'],
                    '7': self.columns['7'],
                    '12': self.columns['12']
                }
            },
            'C': {
                'columns': [8, 9, 10],
                'values': [self.columns['8'], self.columns['9'], self.columns['10']],
                'dict': {
                    '8': self.columns['8'],
                    '9': self.columns['9'],
                    '10': self.columns['10']
                }
            },
            'D': {
                'columns': [3, 6, 7],
                'values': [self.columns['3'], self.columns['6'], self.columns['7']],
                'dict': {
                    '3': self.columns['3'],
                    '6': self.columns['6'],
                    '7': self.columns['7']
                }
            }
        }
        
        self._printOutput('Step 3: Set groups columns: {0}'.format(self.groupColumns))

        self.sortedGroups = sorted(self.groupTotals.items(), key=operator.itemgetter(1), reverse=True)

    def _step2(self):
        highestColumnValue = self.sortedColumns[0]
        secondHighestColumnValue = self.sortedColumns[1]

        value = 25 if self.testType == 'functional' else 10
        
        if (highestColumnValue[1] >= (secondHighestColumnValue[1]+value)):
            self._printOutput('Step 2: Highest column value {0} is greater than the second highest column ({1}) plus {2} ({3}).'.format(
                highestColumnValue[1], 
                secondHighestColumnValue[1],
                value,
                secondHighestColumnValue[1]+value))
            self._setMetabolicType(int(highestColumnValue[0]))

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
        self._printOutput('Set columns: {0}'.format(self.columns))

        self.sortedColumns = sorted(self.columns.items(), key=operator.itemgetter(1), reverse=True)

    def _setMetabolicType(self, value):
        if (self.metabolicType > 0):
            return
        
        self.metabolicType = int(value)

    def _printOutput(self, output):
        if (self.verbose):
            print(output)