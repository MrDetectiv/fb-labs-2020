class Reverse:
    def ensd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            nsd, x, y = self.ensd(b % a, a)
            return (nsd, y - (b//a) * x,x)

    def reverse(self, b, n):
        self.nsd, x, y = self.ensd(b, n)
        #print(g,x,y)
        if self.nsd == 1:
            return x % n