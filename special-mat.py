class SpecialMat:
    def __init__(self, n):
        self.n = n
        self.dst = [0] * n**2
        self.push_counter = 0
    def get(self, i, j):
        return self.dst[self.n * i + j - self.push_counter]
    def push(self, bit):
        self.push_counter += 1
        self.push_counter %= (self.n**2)
        self.dst[-self.push_counter] = bit
