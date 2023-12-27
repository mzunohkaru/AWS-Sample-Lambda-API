import json
import sys
import os
import pymysql

# DB接続情報
DB_USER = "[ユーザー名]"
DB_PASSWORD = "[パスワード]"
DB_HOST = "[RDSエンドポイント]"
DB_NAME = "[データベース名]"


# DB接続
try:
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME)

except Exception as e:
    print("Fail connecting to RDS mysql instance")
    print(e)
    sys.exit()

print("Success connecting to RDS mysql instance")


def lambda_handler(event, context):
    try:
        with conn.cursor() as cur:
            req_id = int(event["queryStringParameters"]["id"])

            # レコード取得（指定されたidのレコードのみを取得）
            SQL = "SELECT * FROM recipes WHERE id = %s"
            cur.execute(SQL, (req_id,))
            cur_res = cur.fetchall()

            if len(cur_res) == 0:
                raise Exception

            data_list = list()
            for id, name in cur_res:
                data = dict()
                data = {"id": id, "name": name}

                data_list.append(data)

            cur.close()

            # レスポンス作成
            res = dict()
            res = {"message": "Recipe details by id", "recipe": data_list}

            responce = {
                "isBase64Encoded": True,
                "statusCode": 200,
                "headers": {"MyHeader": "MyHeaderVal"},
                "body": json.dumps(res),
            }

            print(responce)

        return responce

    # エラー処理
    except Exception as e:
        responce = {
            "isBase64Encoded": True,
            "statusCode": 500,
            "headers": {"MyHeader": "MyHeaderVal"},
            "body": '{"message": "No Recipe found"}',
        }

        print(responce)

        return responce
