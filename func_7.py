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
            print(req_id)

            # 存在確認（指定されたidのレコードがDBに存在するか確認）
            SQL = "SELECT * FROM users WHERE id = %s"

            cur.execute(SQL, (req_id,))
            cur_res = cur.fetchall()

            if len(cur_res) == 0:
                raise Exception

            # レコード削除
            SQL = "DELETE FROM users WHERE id = %s;"

            cur.execute(SQL, (req_id,))
            conn.commit()

            # レスポンス生成
            responce = {
                "isBase64Encoded": True,
                "statusCode": 200,
                "headers": {"MyHeader": "MyHeaderVal"},
                "body": '{"message": "Recipe successfully removed!"}',
            }

            print(responce)

        return responce

    # エラー処理
    except Exception as e:
        cur.close()

        responce = {
            "isBase64Encoded": True,
            "statusCode": 500,
            "headers": {"MyHeader": "MyHeaderVal"},
            "body": '{"message": "No Recipe found"}',
        }

        return responce
