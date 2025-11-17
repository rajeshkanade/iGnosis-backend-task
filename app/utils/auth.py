import bcrypt, jwt, time

SECRET_KEY = "supersecret123"
ALGO = "HS256"

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def create_jwt(payload: dict) -> str:
    payload.update({"exp": time.time() + 3600})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGO)

def decode_jwt(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGO])
    except:
        return None
