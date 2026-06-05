import json
import os
import boto3
import requests
from datetime import datetime, timezone

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("weather_data")

API_KEY = os.environ["OPENWEATHER_API_KEY"]
CITY = os.environ.get("CITY", "Kochi")

def lambda_handler(event, context):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={CITY}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    weather = response.json()

    item = {
        "city": CITY,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "temperature": str(weather["main"]["temp"]),
        "humidity": str(weather["main"]["humidity"]),
        "weather": weather["weather"][0]["description"]
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }