// ユーザーを登録する

import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { ScanCommand, UpdateCommand } from "@aws-sdk/lib-dynamodb";

export const handler = async (event) => {
  const body = JSON.parse(event.body);
  const client = new DynamoDBClient({ region: "ap-northeast-1" });

  const scanParams = {
    TableName: "Users",
  };
  // Usersテーブルの全項目をスキャン
  const scanCommand = new ScanCommand(scanParams);
  const scanResult = await client.send(scanCommand);
  //   スキャン結果から新しいユーザーIDを生成
  const newUserId = getNewUserId(scanResult);

  // データ登録
  const updateParams = {
    TableName: "Users",
    Key: {
      UserId: `${newUserId}`,
    },
    UpdateExpression: "set UserName = :UserName, Age = :Age",
    ExpressionAttributeValues: {
      ":UserName": body.UserName,
      ":Age": body.Age,
    },
    ReturnValues: "ALL_NEW",
  };
  const updateCommand = new UpdateCommand(updateParams);
  const updateResult = await client.send(updateCommand);

  const response = {
    statusCode: 200,
    body: JSON.stringify(updateResult.Attributes),
  };
  return response;
};

const getNewUserId = (scanResult) => {
  let newUserId = 1;
  // スキャン結果が空の場合
  if (scanResult.Count === 0) {
    // 新しいユーザーIDとして1を返します
    return newUserId;
  }

  // スキャン結果に項目が存在する場合
  for (const item of scanResult.Items) {
    // 全項目をループして最大のユーザーIDを探す
    if (newUserId < item.UserId) {
      newUserId = item.UserId;
    }
  }
  // そのIDに1を加えた値を新しいユーザーIDとして返します
  return Number(newUserId) + 1;
};

// リクエスト
/*
{
    "body": "{\"UserName\":\"Tanaka Taro\",\"Age\":30}"
}
*/
