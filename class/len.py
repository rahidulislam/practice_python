class Payroll:
    def __init__(self, length):
        self.length = length

    def __len__(self):
        print('len was called')
        return self.length
    
if __name__ == '__main__':
    payroll = Payroll(0)
    print(bool(payroll))
    payroll.length = 10
    print(bool(payroll))