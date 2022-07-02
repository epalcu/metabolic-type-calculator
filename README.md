# metabolic-type-calculator

Python program that, based on the column input, determines what functional and developmental types and sub types a person is.

## Depenendencies
- Python 3

## Setting up locally (only done once)
Run the following command in your console/terminal:
- `pip install -r requirements.txt`

## Running the calculator
Update `testColumns.json` file with the list of functional and developmental column values and run the following command in your console/terminal:
- `python3 app.py`
- Example run: 

```
elliass-MacBook-Pro-2:src epalcu$ python3 app.py

functional Test 
Group A: 369
Group B: 420
Group C: 302
Group D: 249

functional Metabolic Type: 5
Sub Type: 8

developmental Test 
Group A: 50
Group B: 46
Group C: 28
Group D: 19

developmental Metabolic Type: 4
Sub Type: 1
```

## Running tests
Update `metabolicTestCases.json` file with another test case and run the following command in your console/terminal:
- `python -m pytest`
