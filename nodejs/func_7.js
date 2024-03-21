// 認証

export const handler = function (event, context, callback) {
  // 認証トークンを取得する
  var token = event.authorizationToken;
  switch (token) {
    case "allow":
      // callback
      // 最初の引数はエラーを示し（エラーがない場合はnull）
      // 2番目の引数は成功時の結果
      callback(null, generatePolicy("user", "Allow", event.methodArn));
      break;
    case "deny":
      callback(null, generatePolicy("user", "Deny", event.methodArn));
      break;
    case "unauthorized":
      callback("Unauthorized"); // Return a 401 Unauthorized response
      break;
    default:
      callback("Error: Invalid token"); // Return a 500 Invalid token response
  }
};

var generatePolicy = function (principalId, effect, resource) {
  var authResponse = {};

  // principalId: ポリシーが適用されるユーザーまたはロールの識別子
  // effect: アクセス許可の種類を指定
  // resource: アクセス許可または拒否を適用するリソースのARN
  authResponse.principalId = principalId;
  if (effect && resource) {
    // ポリシー文書の生成
    var policyDocument = {};
    policyDocument.Version = "2012-10-17";
    policyDocument.Statement = [];
    var statementOne = {};
    statementOne.Action = "execute-api:Invoke";
    statementOne.Effect = effect;
    statementOne.Resource = resource;
    policyDocument.Statement[0] = statementOne;
    authResponse.policyDocument = policyDocument;
  }
  // 追加の情報（例: 文字列、数値、ブール値）を含め、API Gatewayのバックエンドサービスで使用する
  authResponse.context = {
    stringKey: "stringval",
    numberKey: 123,
    booleanKey: true,
  };
  return authResponse;
};

// リクエスト
/*
{
  "authorizationToken": "allow"
}
*/
