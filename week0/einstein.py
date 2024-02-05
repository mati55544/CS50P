def main():
    mass = input("please type a mass:")
    mass = mma(mass) 
    print(mass)


def mma(mass):
    c = 300000000.0
    energy = c **2 * int(mass)
    return energy 
 



main()


