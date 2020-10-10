class CPF:
    def __init__(self, num):
        self.num = str(num)
        self.length = len(self.num)
        self.weights = '123456789'
        
    def check_phase0(self):
        if self.num in ['11111111111', '22222222222',
                        '33333333333', '44444444444',
                        '55555555555', '66666666666',
                        '77777777777', '88888888888',
                        '99999999999']:
            return False
        else:
            return True
    
    def check_phase1(self, start_idx=0):
        result = 0
        for idx, n in enumerate(self.num[start_idx:]):
            a = eval(n)
            try:
                b = eval(self.weights[idx])
            except:
                break
            result += a * b
        return result

    def check_phase2(self, result, compare_idx=9):
        if result % 11 == eval(self.num[compare_idx]):
            return True
        else:
            return False
    
    def check(self):
        if self.check_phase0() and self.length == 11:
            result = self.check_phase1()
            if self.check_phase2(result):
                result = self.check_phase1(1)
                if self.check_phase2(result, 10):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False