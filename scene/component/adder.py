class Adder:
    def __init__(self, x: int, y: int, bits: int = 4) -> None:
        self.x = x
        self.y = y
        self.bits = bits

    def get_binary(self, decimal: int):
        
        return format(decimal, 'b').zfill(self.bits)
    

    

adder = Adder(-3, 4)
print(adder.get_binary(-2))