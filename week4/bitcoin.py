import sys 
import requests


if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("command line argument is not a number")
        
        sys.exit(1)

else:
    print("missing command-line argument")
    sys.exit(1)


try:
    r = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    bit= float(response['bpi']['USD']['rate_float'])
    sum = value * bit
    print("$",sum)
except requests.RequestException:
    print("Requestexception")
    sys.exit(1)

