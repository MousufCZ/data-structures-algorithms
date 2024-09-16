"""
This class takes two @paras to calculate the given percentage of a given number.
@args 1 = orig_num_input
@args 2 = perc_input

orig_num_input is the given number
perc_input is the given percentage

Formula
Step 1: value of percentage change = (given percentage / 100) * given number
Step 2: increase of percentage = given number + value of percentage change
Step 3: decrease of percentage = given number - value of pe rcentage change

"""
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

    # Function convers the given percentage to decimal
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