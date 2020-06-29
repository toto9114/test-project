# HOMEWORK

## Environments
```text
./environments/environments.yml
파일에 연결시키고자하는 MySQL 정보를 입력한다.
```

## Docker
```text
docker build -t test-project .
docker-compose up -d
docker-compose logs -f
```

# Table query
```text
./table_query.txt
```

## API Document

### Login - 토큰 생성
#### Endpoint
```text
POST /api/o/token/
```
#### Payload
```text
Content-Type: application/x-www-form-urlencoded
{
    grant_type: password,
    client_id: T3u5jsjokORO9UCMeFG6mxbOuLungS5iKIFi1tXP,
    client_secret: NUySERaNpiiBz6rAQ3AlJeL49SO0QrlK2ja5OmhyUUiCnTbND2wZEUwisgp0OdlmTD6cPVm08ywSkWatFBhkxp29LZKbUbmgIT1q1mXLODyRZTHrk33PRIkDhlcBnduh,
    username: <회원속성에서의 name>,
    password: <password>
}
```
#### Response
```text
HTTP Status code: 200 OK
{
    "access_token": "4Puq1uwEGDal5zKcTMg0wG8oISo4p9",
    "expires_in": 86400,
    "token_type": "Bearer",
    "scope": "read write groups",
    "refresh_token": "jviKULxXeu0dhPMLJD7SKwrctyCMH0"
}
```

### Logout - 토큰 비활성화
#### Endpoint
```text
POST /api/o/revoke_token/
```
#### Payload
```text
Content-Type: application/x-www-form-urlencoded
{
    grant_type: revoke_token,
    client_id: T3u5jsjokORO9UCMeFG6mxbOuLungS5iKIFi1tXP,
    client_secret: NUySERaNpiiBz6rAQ3AlJeL49SO0QrlK2ja5OmhyUUiCnTbND2wZEUwisgp0OdlmTD6cPVm08ywSkWatFBhkxp29LZKbUbmgIT1q1mXLODyRZTHrk33PRIkDhlcBnduh,
    token: <access_token>
}
```
#### Response
```text
HTTP Status code: 200 OK
```

### Signup - 회원가입
#### Endpoint
```text
POST /api/signup/
```
#### Payload
```text
Content-Type: application/json
{
    name:<이름>,
    nickname:<별명>,
    email:<이메일>,
    phone_number:<전화번호>,
    password:<비밀번호>,
    sex: <1(male) 또는 2(female)의 Integer 형태 - 선택사항>
}
```
#### Response
```text
HTTP Status code: 201 Created
{
    "code": "2010000",
    "message": "요청에 성공했습니다.",
    "payload": {
        "id": 1,
        "name": "name",
        "nickname": "nickname",
        "phone_number": "01026724411",
        "email": "jihun3353@gmail.com",
        "sex": null
    }
}
```

### 단일 회원 상세조회
#### Endpoint
```text
Authorization: Bearer <access_token>
GET /api/profile/<profile_id>/
```
#### Response
```text
HTTP Status code: 200 OK
{
    "code": "2000000",
    "message": "요청에 성공했습니다.",
    "payload": {
        "id": 1,
        "name": "name",
        "nickname": "nickname",
        "phone_number": "01026724411",
        "email": "jihun3353@gmail.com",
        "sex": 1
    }
}
```

### 단일 회원의 주문 목록 조회
#### Endpoint
```text
Authorization: Bearer <access_token>
GET /api/order/<profile_id>/
```
#### Response
```text
HTTP Status Code: 200 OK
{
    "code": "2000000",
    "message": "요청에 성공했습니다.",
    "payload": [
        {
            "id": 1,
            "buyer": {
                "id": 1,
                "name": "name",
                "nickname": "nickname",
                "phone_number": "01026724411",
                "email": "jihun3353@gmail.com",
                "sex": 1
            },
            "order_number": "<order_number>",
            "product_name": "<product_name>",
            "dt_order": "2020-06-29T08:00:32.522248Z"
        }
    ]
}
```

### 여러 회원 목록 조회
#### Endpoint
```text
Authorization: Bearer <access_token>
GET /api/profile/
```

#### Parameter
```text
name: 사용자 이름
email: email

ex) http://localhost:8000/api/profile/?name=name&email=jihun33
```

#### Response
```text
HTTP Status Code: 200 OK
{
    "code": "2000000",
    "message": "요청에 성공했습니다.",
    "payload": {
        "count": 4,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "name",
                "nickname": "nickname",
                "phone_number": "01026724411",
                "email": "jihun3353@gmail.com",
                "sex": 1,
                "last_order": {
                    "id": 1,
                    "buyer": {
                        "id": 1,
                        "name": "jihun3353",
                        "nickname": "앨런",
                        "phone_number": "010-2672-4411",
                        "email": "jihun3353@gmail.com",
                        "sex": 1
                    },
                    "order_number": "<order_number>",
                    "product_name": "<product_name>",
                    "dt_order": "2020-06-29T08:00:32.522248Z"
                }
            },
            {
                "id": 2,
                "name": "<name>",
                "nickname": "<nickname>",
                "phone_number": "01026724411",
                "email": "jihun3353@gmail.com",
                "sex": null,
                "last_order": null
            },
            ...
            ...
        ]
    }
}
```
끗