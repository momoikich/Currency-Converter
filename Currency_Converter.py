import requests
from gooey import Gooey, GooeyParser

@Gooey
def currency_converter_gui():
    parser = GooeyParser(description="Currency Converter")

    parser.add_argument("amount", type=float, help="Amount to convert")
    parser.add_argument(
        "from_currency", choices=list_currency_codes(), help="From Currency"
    )
    parser.add_argument("to_currency", choices=list_currency_codes(), help="To Currency")

    args = parser.parse_args()

    result = convert_currency(args.amount, args.from_currency, args.to_currency)

    print(f"{args.amount} {args.from_currency} is equal to {result:.2f} {args.to_currency}")

def list_currency_codes():
    api_key = "d0a24575846f6c64de9b32ba"  # Replace with your actual API key
    base_url = "https://open.er-api.com/v6/latest"

    response = requests.get(base_url, params={"apikey": api_key})

    if response.status_code == 200:
        data = response.json()
        currencies = list(data["rates"].keys())
        return sorted(currencies)
    else:
        print(f"Error: Unable to fetch currency codes. Status Code: {response.status_code}")
        return []

def convert_currency(amount, from_currency, to_currency):
    api_key = "d0a24575846f6c64de9b32ba"  # Replace with your actual API key
    base_url = "https://open.er-api.com/v6/latest"

    params = {"apikey": api_key}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"].get(to_currency)
        if rate is not None:
            result = amount * rate
            return result
        else:
            print(f"Error: Unable to find exchange rate for {to_currency}")
    else:
        print(f"Error: Unable to fetch exchange rates. Status Code: {response.status_code}")

if __name__ == "__main__":
    currency_converter_gui()

