import json
import requests

# Replace with your API key and the URL of your currency rates provider
API_KEY = "your_api_key"
EXCHANGE_RATE_API_URL = "https://v6.exchangerate-api.com/v6/{}/latest/".format(API_KEY)

def lambda_handler(event, context):
    try:
        # Parse input parameters
        body = json.loads(event["body"])
        base_currency = body.get("base_currency")
        target_currency = body.get("target_currency")
        amount = float(body.get("amount", 0))

        if not base_currency or not target_currency or amount <= 0:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Invalid input. Provide 'base_currency', 'target_currency', and a positive 'amount'."
                })
            }

        # Fetch exchange rates
        response = requests.get(EXCHANGE_RATE_API_URL + base_currency)
        if response.status_code != 200:
            return {
                "statusCode": 500,
                "body": json.dumps({
                    "error": "Failed to fetch exchange rates. Please try again later."
                })
            }

        rates = response.json().get("conversion_rates", {})
        if target_currency not in rates:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": f"Target currency '{target_currency}' not supported."
                })
            }

        # Perform conversion
        conversion_rate = rates[target_currency]
        converted_amount = round(amount * conversion_rate, 2)

        # Return response
        return {
            "statusCode": 200,
            "body": json.dumps({
                "base_currency": base_currency,
                "target_currency": target_currency,
                "conversion_rate": conversion_rate,
                "original_amount": amount,
                "converted_amount": converted_amount
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
