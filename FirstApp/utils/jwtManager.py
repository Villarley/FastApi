from jwt import encode, decode
def CreateToken(data: dict):
    token:str = encode(payload=data, key="mysqlkey", algorithm="HS256")
    return token
def ValidateToken(token:str) -> dict:
    data: dict = decode(token, key="mysqlkey", algorithms=['HS256'])
    return data