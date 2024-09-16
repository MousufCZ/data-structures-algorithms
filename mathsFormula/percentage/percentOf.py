class PercentageOfNumber:
    def __init__(self, orig_num_input, perc_input):
        self.orig_num_input = orig_num_input
        self.perc_input = perc_input

    def input_original_number(self):
        orig_num_input = self.orig_num_input
        return print(f"From this number:  {orig_num_input}")

    def input_percentage(self):
        perc_input = self.perc_input
        return print(f"I want: {perc_input}%")

    def input_perc_to_dec(self):
        toDec = float(self.perc_input)/100
        return toDec
    
    def total_of_perc_to_orig_num(self):
        perc_to_dec = self.input_perc_to_dec()
        originalNum = self.orig_num_input
        perc_per_section = originalNum * perc_to_dec
        #print(f"Total of the percentage {self.perc_input}% of {self.orig_num_input} is: {perc_per_section}")
        return perc_per_section
    
    def total_after_perc_increase(self):
        originalNum = self.orig_num_input
        perc_input = self.perc_input
        total_of_perc_to_orig_num = self.total_of_perc_to_orig_num()
        total_after_perc_increase = originalNum + total_of_perc_to_orig_num
        print(f"{perc_input}% increase to {originalNum} is: {total_after_perc_increase}")
        return total_after_perc_increase
    
    def total_after_perc_decrease(self):
        originalNum = self.orig_num_input
        perc_input = self.perc_input
        total_of_perc_to_orig_num = self.total_of_perc_to_orig_num()
        total_after_perc_decrease = originalNum - total_of_perc_to_orig_num
        print(f"{perc_input}% decrease of {originalNum} is: {total_after_perc_decrease}")
        return total_after_perc_decrease

def testPercentageOfNumber():
    originalNum1 = 1200000
    percentage = 20.00
    test = PercentageOfNumber(originalNum1, percentage)
    test.input_original_number()
    test.input_percentage
    test.total_after_perc_increase()
    test.total_after_perc_decrease()
    

if __name__ == "__main__":
    testPercentageOfNumber()