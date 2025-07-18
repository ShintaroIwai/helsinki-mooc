# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        if self._cents >= 10:
            return f"{self._euros}.{self._cents} eur"
        elif self._cents < 10:
            return f"{self._euros}.0{self._cents} eur"
    
    def __eq__(self, another):
        if self._euros == another._euros and self._cents == another._cents:
            return True
        else:
            return False
    
    def __gt__(self, another):
        if self._euros > another._euros:
            return True
        elif self._euros == another._euros:
            if self._cents > another._cents:
                return True
            else:
                return False
        else:
            return False
    
    def __lt__(self, another):
        if self._euros < another._euros:
            return True
        elif self._euros == another._euros:
            if self._cents < another._cents:
                return True
            else:
                return False
        else:
            return False
        
    def __ne__(self, another):
        if self._euros == another._euros and self._cents == another._cents:
            return False
        else:
            return True
    
    def __add__(self, another):
        sum = Money(0, 0)
        sum._euros = self._euros + another._euros
        sum._cents = self._cents + another._cents
        if sum._cents >= 100:
            sum._euros += 1
            sum._cents -= 100
        return sum
    
    def __sub__(self, another):
        diff = Money(0, 0)
        diff._euros = self._euros - another._euros
        diff._cents = self._cents - another._cents
        if diff._cents < 0:
            diff._euros -= 1
            diff._cents += 100
        # I only have to worry about euros being negative because by virtue of the previous block, cents is never negative
        if diff._euros < 0:
            raise ValueError("a negative result is not allowed")
        else:
            return diff

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1