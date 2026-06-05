import json
import os
import boto3
from datetime import datetime

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):

    for record in event["Records"]:

        if record["eventName"] != "INSERT":
            continue

        new_image = record["dynamodb"]["NewImage"]

        item = {
            "city": new_image["city"]["S"],
            "timestamp": new_image["timestamp"]["S"],
            "temperature": new_image["temperature"]["S"],
            "humidity": new_image["humidity"]["S"],
            "weather": new_image["weather"]["S"]
        }

        key = (
            f"weather/"
            f"{item['city']}/"
            f"{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json"
        )

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=key,
            Body=json.dumps(item),
            ContentType="application/json"
        )

    return {
        "statusCode": 200
    }