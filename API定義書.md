# API定義
## /hello
接続確認用
### Response
```
{
    "message" : "Hello Challecara!"
}
```

## /api/v1/users/signup (POST)
ユーザーのSingUp用のエンドポイント
### Request
```
{
    "name": "string",
    "email": "user@example.com",
    "password": "string"
}
```
### Response
```
{
    "user_id": "string",
    "email": "user@example.com",
    "name": "string"
}
```

## /api/v1/users/signin (POST)
ユーザーのSignIn用のエンドポイント
### Request
```
{
    "email": "user@example.com",
    "password": "string"
}
```
### Response
```
{
    "jwt" : "string"
}
```

## /api/v1/users/me (GET)
自分自身の情報を取得するエンドポイント
### Request
```
No Parameters
```
### Response
```
{
  "user_id": "string",
  "name": "string",
  "clothes": [
    {
      "clothe_id": "string",
      "image_url": "string",
      "size": "string",
      "color": "string",
      "user_id": "string"
    }
  ],
  "fashions": [
    {
      "fashion_id": "string",
      "user_id": "string",
      "name": "string",
      "clothes": [
        {
          "clothe_id": "string",
          "image_url": "string",
          "size": "string",
          "color": "string",
          "user_id": "string"
        }
      ],
      "date": [
        {
          "date_id": "string",
          "fashion_id": "string",
          "date": "2022-10-05T07:58:46.398Z"
        }
      ]
    }
  ]
}
```

## api/v1/users (DELETE)
ユーザの削除を行うエンドポイント
### Request
```
No Parameters
```
### Response
{
    "detail": "string"
}

## api/v1/clothes/ (POST)
服の登録を行うエンドポイント
### Request
```
(queryParameter) size : "string" (Available values : SS, S, M, L, LL)

{
  "image_url": "string",
  "color": "string"
}
```
### Response
```
{
  "clothe_id": "string",
  "image_url": "string",
  "size": "string",
  "color": "string",
  "user_id": "string"
}
```

## api/v1/clothes/{clothe_id} (GET)
服の詳細を取得するエンドポイント
### Request
```
(pathParameter) clothe_id: "string"
```
### Response
```
{
  "clothe_id": "string",
  "image_url": "string",
  "size": "string",
  "color": "string",
  "user_id": "string"
}
```

## api/v1/clothes/{clothe_id} (DELETE)
服を削除するエンドポイント
### Request
```
(pathParameter) clothe_id: "string"
```
### Response
```
{"detail" : "OK!!"}
```

## api/v1/friends/ (GET)
自分の追加した友達をすべて取得するエンドポイント
### Request
```
No Parameter
```
### Response 
```
[
  {
    "friend_id": "string",
    "name": "string",
    "tag_color": "string",
    "user": {
      "user_id": "string",
      "email": "user@example.com",
      "name": "string"
    },
    "date": [
      {
        "date_id": "string",
        "friend_id": "string",
        "date": "2022-10-05T08:08:36.185Z"
      }
    ]
  }
]
```

## api/v1/friends/ (PUT)
友達の情報を編集するエンドポイント
### Request
```
(queryParameter) tag_color : "string" 
(Available values: red, orange, yellow, green, blue, indigo, violet)

{
  "image_url": "string",
  "color": "string"
}
```
### Response
```
{
  "clothe_id": "string",
  "image_url": "string",
  "size": "string",
  "color": "string",
  "user_id": "string"
}
```

## /api/v1/friends/ (POST)
友達の登録用のエンドポイント
### Request
```
(queryParameter) tag_color : "string" 
(Available values: red, orange, yellow, green, blue, indigo, violet)

{
  "name": "string",
  "date": "2022-10-05T08:14:13.899Z"
}
```
### Response
```
{
  "friend_id": "string",
  "name": "string",
  "tag_color": "string",
  "user": {
    "user_id": "string",
    "email": "user@example.com",
    "name": "string"
  },
  "date": [
    {
      "date_id": "string",
      "friend_id": "string",
      "date": "2022-10-05T08:14:13.901Z"
    }
  ]
}
```

## api/v1/friends/{friend_id} (DELETE)
友達を削除するエンドポイント
### Request
```
(pathParameter) friend_id: "string"
```
### Response
```
{"detail" : "OK!!"}
```

### api/v1/fashions/ (POST)
コーデを登録するエンドポイント
### Request
```
(pathParameter) name: "string"

{
  "clothe_ids": [
    "string"
  ]
}
```

### Response
```
{
  "fashion_id": "string",
  "user_id": "string",
  "name": "string",
  "clothes": [
    {
      "clothe_id": "string",
      "image_url": "string",
      "size": "string",
      "color": "string",
      "user_id": "string"
    }
  ],
  "date": [
    {
      "date_id": "string",
      "fashion_id": "string",
      "date": "2022-10-05T08:17:21.702Z"
    }
  ]
}
```