import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { GetCommand } from "@aws-sdk/lib-dynamodb";

export const handler = async (event) => {
  const client = new DynamoDBClient({ region: "us-west-2" });

  const params = {
    TableName: 'Users',
    Key: {
      'UserId': '1',
    },
  };
  // DynamoDBテーブルから特定のアイテムを取得するためのコマンドを作
  const command = new GetCommand(params);
  const data = await client.send(command);
  console.log(data);

  return data;
};