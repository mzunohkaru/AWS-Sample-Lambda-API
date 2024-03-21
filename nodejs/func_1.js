import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { UpdateCommand } from "@aws-sdk/lib-dynamodb";

export const handler = async (event) => {
  const client = new DynamoDBClient({ region: "us-west-2" });

  const params = {
    // 更新するデータが格納されているテーブルの名前
    TableName: 'Users',
    // 更新するレコードを一意に識別するキー（この場合はUserIdが'1'のレコード）
    Key: {
      'UserId': '1',
    },
    // 更新を行う属性とその新しいデータ
    UpdateExpression: "set UserName = :UserName, Age = :Age",
    // UserNameとAgeのデータを更新
    ExpressionAttributeValues: {
      ":UserName": "Tanaka Taro",
      ":Age": 20,
    },
    // 更新後のレコードの全属性を返すように指定
    ReturnValues: "ALL_NEW"
  };
  // 更新コマンドを作成
  const command = new UpdateCommand(params);
  // UpdateCommandをDynamoDBに送信
  const data = await client.send(command);
  console.log(data);

  return data;
};
