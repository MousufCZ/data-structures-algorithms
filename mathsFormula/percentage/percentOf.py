class PercentageOf:
    def __self__(self, origNoInput, percInput):
        self.origNoInput = origNoInput
        self.perctInput = percInput

    def inputOriginalNumber(self, origNoInput):
        return print(f"Percentage input of original number:  {origNoInput}")

    def inputPercentage(self, percInput):
        return print(f"Input of %: {percInput}")
    
    def percentageIncrease(self):
        return
    
    def percentageDecrease(self):
        return
    
    def percentagePersector(self):
        return
    
if __name__ == "__main__":
    test = PercentageOf()
    test.inputOriginalNumber(1)
    test.inputPercentage(20)