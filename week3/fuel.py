def main():
    amount = convert_pre()
    print(f"{amount:.0%}")




def convert_pre():
    while True:
        try:
            return float(input("Enter your amount: "))
            
        except ValueError:
            
            
            pass

if __name__ == "__main__":
    main()
