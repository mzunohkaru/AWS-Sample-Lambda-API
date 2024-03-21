import boto3
import json

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("users")


def post_users(requestJSON):
    table.update_item(
        # id: 更新対象のアイテムを一意に識別するキー
        Key={"id": requestJSON["id"]},
        
        # DynamoDBでは、update_itemメソッドを使用してアイテムを更新する際に、
        # UpdateExpressionで指定する属性名がDynamoDBの予約語と衝突する可能性があります。
        # このような衝突を避けるために、属性名の代わりにプレースホルダー（この場合は#name）を使用し、
        # ExpressionAttributeNamesでそのプレースホルダーが実際にどの属性名を指すのかをマッピングします。
        UpdateExpression="SET #name = :newName, age = :newAge, address = :newAddress, tel = :newTel",
        ExpressionAttributeNames={"#name": "name"},

        # 各プレースホルダーの新しい値を指定
        ExpressionAttributeValues={
            ":newName": requestJSON["name"],
            ":newAge": requestJSON["age"],
            ":newAddress": requestJSON["address"],
            ":newTel": requestJSON["tel"],
        },
    )


def lambda_handler(event, context):
    requestJSON = json.loads(event["body"])
    post_users(requestJSON)
