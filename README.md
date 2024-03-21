## func 1 (python)

![architecture_1](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/a177b1d0-060b-4a10-aed0-bf8ca8520bec)

① GETメソッドでAPIを叩く。パスパラメータにテキストを持たせる
② Lambda関数を実行
③ パスパラメータから受け取ったテキストを翻訳サービスに送る
④ 翻訳サービスで翻訳したテキストを返す
⑤ パスパラメータのテキスト、翻訳したテキスト、時間をDynamoDBに保存する
⑥ DynamoDBから取得したデータを返す
⑦ 加工したデータをJSON形式で返す


## func 2 (python)

![architecture_2](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/394b1f35-72cb-44b6-95e4-9f160a026790)

① GETメソッドでAPIを叩く。パスパラメータにidを持たせる
② Lambda関数を実行
③ パスパラメータから受け取ったidでDynamoDBのデータを検索
④ DynamoDBから検索結果を返す
⑤,⑥ 検索結果をJSON形式で返す


## func 3 (python)

![architecture_3](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/cd1ac291-dd40-4d03-a329-92141ed5ad6d)

① GETメソッドでAPIを叩く
② Lambda関数を実行
③ RDBのデータを全て返すように要求
④ RDBからデータを全て返す
⑤,⑥ RDBから取得したデータをJSON形式で返す 
⑦ EC2へアクセス
⑧ コンソールでデータの操作を行う


## func 4 (python)

![architecture_3](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/cd1ac291-dd40-4d03-a329-92141ed5ad6d)

① GETメソッドでAPIを叩く。パスパラメータにidを持たせる
② Lambda関数を実行
③ RDBのデータへパスパラメータから受け取ったidのデータを検索し、返すように要求
④ RDBから検索結果のデータを返す
⑤,⑥ RDBから取得したデータをJSON形式で返す 
⑦ EC2へアクセス
⑧ コンソールでデータの操作を行う


## func 5 (python)

![architecture_5](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/96240896-ba15-4590-bb49-4d34026dc1e0)

① GETメソッドでAPIを叩く。パスパラメータにnameを持たせる
② Lambda関数を実行
③ RDBのデータへパスパラメータから受け取ったnameのデータを保存し、保存したデータを返す
④ EC2へアクセス
⑤ コンソールでデータの操作を行う


## func 7 (python)

![architecture_5](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/96240896-ba15-4590-bb49-4d34026dc1e0)

① GETメソッドでAPIを叩く。パスパラメータにidを持たせる
② Lambda関数を実行
③ RDBのデータへパスパラメータから受け取ったidのデータを検索し、削除する
④ EC2へアクセス
⑤ コンソールでデータの操作を行う


## func 8 (python)

![architecture_8](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/a67a47db-d602-4ce7-9806-85bff1063c9d)


## func 9 (python)

![architecture_9](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/a7fc7ded-4a6a-464c-baef-395aa3e233dd)

① POST・GET・PUT・DELETEメソッドでAPIを叩く
②-CREATE DynamoDBにデータを挿入
②-READ DynamoDBからデータ (全データ＆パスパラメータのIDと一致するデータ) を取得
②-PUT  DynamoDBのデータを更新
②-DELETE DynamoDBのデータを削除


## func 3,4,5,6,7 (nodejs)

![architecture_3,4,5,6,7](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/3b8c52fa-ef8a-4214-b1da-d2f9b55e5012)

① APIを叩く
② 認証トークンを検証
CREATE DynamoDBにデータを挿入
READ DynamoDBからデータ (全データ＆パスパラメータのIDと一致するデータ) を取得
PUT  DynamoDBのデータを更新
DELETE DynamoDBのデータを削除


## 構成図イメージ作成ツール
https://qiita.com/marcio/items/fe86c0c8749edfd52399

