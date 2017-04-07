class galois_field:
    def __init__(self, m = 4, alpha = 2):
        self.m = m
        self.alpha = alpha

    def info_field(self):
        elements = 2**self.m
        n = elements - 1
        print 'Galois Field GF(%d) N ='  % elements, n



if __name__ == '__main__':

    gfield = galois_field(4,2)
    gfield.info_field()




