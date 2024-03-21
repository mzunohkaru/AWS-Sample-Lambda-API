// ユーザー一覧を取得する

// AWS SDKのDynamoDBClientをインポート
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { ScanCommand } from "@aws-sdk/lib-dynamodb";

export const handler = async (event) => {
  // DynamoDBサービスに接続するためのクライアントを作成
  const client = new DynamoDBClient({ region: "ap-northeast-1" });

  const params = {
    TableName: "Users",
  };
  // 指定されたテーブルの全項目をスキャンするためのコマンド
  const command = new ScanCommand(params);
  const data = await client.send(command);

  const response = {
    statusCode: 200,
    body: JSON.stringify(data.Items),
  };
  return response;
};
