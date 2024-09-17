from mathsFormula.percentage import percentOf
from mathsFormula.percentage import percentChange


def testPercentageOfNumber():
    originalNum1 = 1200000
    percentage = 20.00
    test = percentOf.PercentageOfNumber(originalNum1, percentage)
    test.input_original_number()
    test.input_percentage
    test.total_after_perc_increase()
    test.total_after_perc_decrease()

def test_percent_change():
    originalNum1 = 1.2
    originalNum2 = 0.96
    test = percentChange.PercentChange(originalNum1, originalNum2)
    print(f"Change between {originalNum1} and {originalNum2} is: {test.input_difference()}%")

if __name__ == "__main__":
    testPercentageOfNumber()
    print("########")
    test_percent_change()