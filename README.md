## func 1

![architecture_1](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/a177b1d0-060b-4a10-aed0-bf8ca8520bec)

① パスパラメータにテキストを持たせて、APIを叩く
② Lambda関数を実行
③ パスパラメータから受け取ったテキストを翻訳サービスに送る
④ 翻訳サービスで翻訳したテキストを返す
⑤ パスパラメータのテキスト、翻訳したテキスト、時間をDynamoDBに保存する
⑥ DynamoDBから取得したデータを返す
⑦ 加工したデータをJSON形式で返す


## func 2

![architecture_2](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/394b1f35-72cb-44b6-95e4-9f160a026790)

① パスパラメータにidを持たせて、APIを叩く
② Lambda関数を実行
③ パスパラメータから受け取ったidでDynamoDBのデータを検索
④ DynamoDBから検索結果を返す
⑤,⑥ 検索結果をJSON形式で返す


## func 3

![architecture_3](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/cd1ac291-dd40-4d03-a329-92141ed5ad6d)

① GETメソッドでAPIを叩く
② Lambda関数を実行
③ RDBのデータを全て返すように要求
④ RDBのデータを全て返す
⑤,⑥ RDBから取得したデータをJSON形式で返す 
⑦ EC2へアクセス
⑧ コンソールでデータの操作を行う


## func 4

![architecture_3](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/cd1ac291-dd40-4d03-a329-92141ed5ad6d)


## func 5

![architecture_5](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/96240896-ba15-4590-bb49-4d34026dc1e0)


## func 7

![architecture_5](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/96240896-ba15-4590-bb49-4d34026dc1e0)


## func 8

![architecture_8](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/a67a47db-d602-4ce7-9806-85bff1063c9d)


## func 9

![architecture_9](https://github.com/mzunohkaru/AWS-Sample-Lambda-API/assets/99012157/1b18bad7-8174-49f1-9d4b-2f86b4b5699f)


## 構成図イメージ作成ツール
https://qiita.com/marcio/items/fe86c0c8749edfd52399

