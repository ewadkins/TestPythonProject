print "Hello World!"

class Polynomial:
    ## Intialize a polynomial with a list of coefficients.
    ## The coefficient list starts with the highest order term.
    def __init__(self, coeffs):
        self.coeffs = []
        self.order = len(coeffs) - 1
        for coeff in reversed(coeffs):
            self.coeffs.append(coeff)

    ## Return the coefficient of the x**i term
    def coeff(self,i):
        return self.coeffs[i]

    ## Return the value of this Polynomial evaluated at x=v
    def val(self, v):
        value = 0
        for i in range(len(self.coeffs)):
            value = value + self.coeff(i) * (v ** i)
        return value

    ## Return the roots of this Polynomial
    def roots(self):
        if(self.order == 1):
            return [float(-self.coeff(0))/self.coeff(1)]
        if(self.order == 2):
            det = self.coeff(1)**2 -4*self.coeff(2)*self.coeff(0)
            if(det >= 0):
                root1 = (float(-self.coeff(1)) + det**0.5)/(2*self.coeff(2))
                root2 = (float(-self.coeff(1)) - det**0.5)/(2*self.coeff(2))
                return [root1, root2]
            elif(self.order == 2):
                root1 = complex(float(-self.coeff(1))/(2*self.coeff(2)), ((-det)**0.5)/(2*self.coeff(2)))
                root2 = complex(float(-self.coeff(1))/(2*self.coeff(2)), -((-det)**0.5)/(2*self.coeff(2)))
                return [root1, root2]
            else:
                raise Exception("Can't handle a polynomial of this order!")

    ## Add two polynomials, return a new Polynomial
    def add (self, other):
        final = []
        print self.coeffs
        print other.coeffs
        for i in range(len(self.coeffs)):
            while(i >= len(final)):
                final.append(0)
            final[i] = final[i] + self.coeff(i)
        for i in range(len(other.coeffs)):
            while(i >= len(final)):
                final.append(0)
            final[i] = final[i] + other.coeff(i)
        final2 = []
        for coeff in reversed(final):
            final2.append(coeff)
        return Polynomial(final2)

    ## Multiply two polynomials, return a new Polynomial
    def mul(self, other):
        final = []
        print self.coeffs
        print other.coeffs
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                while(i+j >= len(final)):
                    final.append(0)
                final[i+j] = final[i+j] + self.coeff(i)*other.coeff(j)
        final2 = []
        for coeff in reversed(final):
            final2.append(coeff)
        return Polynomial(final2)
        

    def __add__(self, other):
        #override the + operator so we can do things like p1+p2
        return self.add(other)

    def __mul__(self, other):
        #override the * operator so we can do things like p1*p2
        return self.mul(other)

    def __str__(self):
        coeffs = [self.coeff(i) for i in xrange(self.order,-1,-1)]
        return 'Polynomial(%r)' % coeffs
    

#poly = Polynomial([1, 5, 4])
#poly2 = Polynomial([1, 10, 169])
#print poly.add(poly2)




def diffPoly(inp):
    newList = []
    for i in range(1, len(inp.coeffs)):
        newList.append(inp.coeffs[i]*(i))
    return Polynomial(newList[::-1])

def diffPoly2(inp):
    newList = []
    for i in range(len(inp.coeffs)-1):
        newList.append(inp.coeffs[::-1][i]*(inp.order-i))
    return newList

print diffPoly(Polynomial([3, 2, 1])).__str__()

