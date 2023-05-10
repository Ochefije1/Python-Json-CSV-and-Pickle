
class CheckNum:
    def __init__(self, nums) -> None:
        self.nums = nums

    def checkOdd(self):
            return [x for x in self.nums if x % 2 == 1]

    def checkEven(self):
            return [x for x in self.nums if x % 2 == 0]

if __name__=="__main__":        
    running = True
    nums = [x for x in range(100)]
    check = CheckNum(nums)

    while running:
        option = input('1. Check odd\n2. Check even\n3. Exit\n____')
        if option not in '123':
            print('Invalid option. Choose between 1 - 3')
            continue

        if option == '1':
            odd = check.checkOdd()
            print(odd)

        elif option == '2':
            even = check.checkEven()
            print(even)
        else:
            running = False
            break