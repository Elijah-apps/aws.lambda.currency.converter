# AWS Lambda Currency Converter

## Overview
The **AWS Lambda Currency Converter** is a serverless application that provides real-time currency conversion functionality. Built on AWS Lambda, it uses a public currency exchange rate API to fetch live rates and performs conversions between currencies. The service is exposed as an HTTP endpoint via AWS API Gateway.

---

## Features
- **Real-Time Exchange Rates**: Fetches the latest rates from a public API.
- **Scalable and Serverless**: Uses AWS Lambda for seamless scaling.
- **Simple JSON API**: Accepts input for base currency, target currency, and amount, and returns the conversion result.
- **Secure**: Designed with API keys and environment variables for safe operation.

---

## API Details

### Endpoint
Replace `{API_URL}` with your deployed API Gateway URL:

