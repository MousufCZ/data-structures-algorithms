import random
"""
This script will generate random integers in a file
"""
# Create a new file
class FileManupilation:
    def __init__(self):
        return
        #self = self

    def createNewFile(self):
        # use f = open x
        #f = open("database/randInt.txt", "w")
        f = open("database/randInt/randInt.txt", "x")

    def generate_rand_no_to_file(self):
        f = open("database//randInt/randInt.txt", "w")
        for i in range(100):
            f.write(f"{int(random.randint(1,100))} \n")
        f.close()


if __name__ == "__main__":
    randInstance = FileManupilation()
    randInstance.generate_rand_no_to_file()
