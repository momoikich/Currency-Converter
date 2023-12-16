
# Currency Converter

## Description

The Currency Converter is a Python program designed to facilitate currency conversion using the latest exchange rates. It leverages the ExchangeRate-API to fetch real-time exchange rates and performs conversions based on user input.

## Features

- Fetches the latest exchange rates from ExchangeRate-API.
- Converts currency from one form to another.
- User-friendly command-line interface.

## Requirements

- Python 3.12
- `requests` library (`pip install requests`)
- `Gooey` library (`pip install Gooey`)
- ExchangeRate-API key (Sign up at https://www.exchangerate-api.com/ to obtain a key)

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies using the following command:

   ```bash
   pip install requests
   ```
   ```bash
   pip install Gooey
   ```
3. Replace `"YOUR_EXCHANGE_RATE_API_KEY"` in the code with your actual ExchangeRate-API key.

## Usage

1. Run the program by executing the following command:

   ```bash
   python Currency_Converter.py
   ```

2. Enter the required information as prompted:
   - Amount to convert
   - Source currency code (e.g., USD, EUR)
   - Target currency code (e.g., USD, EUR)

3. The program will fetch the latest exchange rates and display the converted amount.

## Notes

- Make sure to sign up on ExchangeRate-API and replace the placeholder API key with your actual key.
- This program is a basic example and may not handle all edge cases.

## Acknowledgments

This Currency Converter is built using Python and the `requests` library to interact with ExchangeRate-API.

Feel free to customize and extend the functionality based on your requirements!
```

This readme provides instructions on how to install and use the Currency Converter, along with important information about requirements and customization options.
