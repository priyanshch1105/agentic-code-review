import jwt
import time

def generate_jwt(app_id: str, private_key: str) -> str:
    payload = {
        "iat": int(time.time()) - 60,
        "exp": int(time.time()) + 600,
        "iss": app_id,
    }
    return jwt.encode(payload, private_key, algorithm="RS256")
