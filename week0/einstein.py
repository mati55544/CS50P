def main():
    mass = input("please type a mass:")
    mass = mma(mass) 
    print(mass)


def mma(mass):
    c:float = 300000000.0
    energy = c * c * float(mass)
    return energy 
 



main()


