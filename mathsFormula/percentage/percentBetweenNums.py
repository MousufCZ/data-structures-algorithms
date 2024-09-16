import percentOf

class PercentChange:

    def __init__(self, orig_num_input_1, orig_num_input_2):
        self.orig_num_input_1 = orig_num_input_1
        self.orig_num_input_2 = orig_num_input_2

    def test_class_import(self):
        orig_num_input1 = self.orig_num_input_1
        percent_input = self.orig_num_input_2
        test = percentOf.PercentageOfNumber(orig_num_input1, percent_input)
        test.input_original_number()
        test.input_percentage
        test.total_after_perc_increase()
        test.total_after_perc_decrease()

    def test(self):
        x = self.orig_num_input_1
        y = self.orig_num_input_2
        print(x, y)

def testPercentageChange():
    originalNum1 = 23.00
    originalNum2 = 20.00
    test = PercentChange(originalNum1, originalNum2)
    test.test()

if __name__ == "__main__":
    originalNum1 = 23.00
    originalNum2 = 20.00    
    test = PercentChange(originalNum1, originalNum2)
    #testPercentageBetweenNumbers()

    #Importing function from another folder
    #test.test_class_import()