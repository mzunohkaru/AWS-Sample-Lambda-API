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
    req = event["queryStringParameters"]

    try:
        with conn.cursor() as cur:
            # レコード登録
            SQL = """
                    INSERT INTO users (name)
                    VALUES (%s);
                """
            cur.execute(
                SQL,
                (req["name"],),
            )
            conn.commit()

            # レコード取得（登録したレコードを取得）
            cur.execute("select * from users order by id DESC LIMIT 1;")
            cur_res = cur.fetchall()

            data_list = list()
            for id, name in cur_res:
                data = dict()
                data = {"id": id, "name": name}

                data_list.append(data)

            cur.close()

            # レスポンス生成
            res = dict()
            res = {"message": "Data successfully created!", "Data": data_list}

        return res

    # エラー処理
    except Exception as e:
        cur.close()

        err_res = dict()
        err_res = {
            "message": "Data creation failed!",
        }

        return err_res
