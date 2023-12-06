import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://open.er-api.com/v6/latest"

    def get_exchange_rates(self):
        try:
            response = requests.get(f"{self.base_url}?apikey={self.api_key}")
            data = response.json()
            return data["rates"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rates: {e}")
            return None

    def convert_currency(self, amount, from_currency, to_currency):
        rates = self.get_exchange_rates()

        if rates is not None and from_currency in rates and to_currency in rates:
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = amount * conversion_rate
            return converted_amount
        else:
            print("Invalid currency codes or unable to fetch exchange rates.")
            return None

def main():
    api_key = "YOUR_EXCHANGE_RATE_API_KEY"
    converter = CurrencyConverter(api_key)

    if api_key == "2f7639c718063dca1324726b":
        print("Please replace '2f7639c718063dca1324726b' with your actual API key.")
        return

    print("Welcome to the Currency Converter!")
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    converted_amount = converter.convert_currency(amount, from_currency, to_currency)

    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
