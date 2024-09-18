class NumericLoop:
    def __init__(self, total=0, product=1):
        self.__total = total
        self.__product = product

    def lets_loop(self):
        while (True):
            char = input("Enter your character: ")
            if (not char.isnumeric()):
                print("Oops, an alphabet! Goodbye!\n")
                break
            self.__total += float(char)
            self.__product *= float(char)
        print("Sum of numbers entered:", self.__total)
        print("Product of numbers entered:", self.__product)


sample = NumericLoop()
sample.lets_loop()
