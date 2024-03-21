// ユーザーを削除

import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DeleteCommand } from "@aws-sdk/lib-dynamodb";

export const handler = async (event) => {
  // pathParameters : URLパス内のパラメータを含むオブジェクト
  const pathParameters = event.pathParameters;
  const client = new DynamoDBClient({ region: "ap-northeast-1" });

  const deleteParams = {
    TableName: "Users",
    Key: {
      UserId: pathParameters.UserId,
    },
  };
  const deleteCommand = new DeleteCommand(deleteParams);
  await client.send(deleteCommand);

  const response = {
    statusCode: 200,
    body: JSON.stringify({ UserId: pathParameters.UserId }),
  };
  return response;
};

// リクエスト
/*
{
  "pathParameters": {"UserId":"1"}
}
*/
