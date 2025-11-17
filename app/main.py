from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from app.schemas.user_schema import SignupRequest, SigninRequest, UserMe, ErrorResponse, UserMeResponse
from app.utils.file_handler import read_users, write_users
from app.utils.auth import hash_password, verify_password, create_jwt, decode_jwt
from uuid import uuid4



app = FastAPI(title="User Auth API")
security = HTTPBearer(auto_error=False)


@app.get("/")
def read_root():
    return {"message": "Welcome to the User Auth API"}


@app.post("/signup", responses={400: {"model": ErrorResponse}})
def signup(data: SignupRequest):
    users = read_users()
    if any(u["username"] == data.username for u in users):
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = {
        "userId": str(uuid4()),
        "username": data.username,
        "fname": data.fname,
        "lname": data.lname,
        "password": hash_password(data.password),
    }

    users.append(new_user)
    write_users(users)

    return JSONResponse( status_code = 201 , content = {
        "result" : True, 
        "message": "SignUp success. Please proceed to Signin"
    })


@app.post("/signin", responses={401: {"model": ErrorResponse}})
def signin(data: SigninRequest):
    users = read_users()

    user = next((u for u in users if u["username"] == data.username), None)
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_jwt({"username": user["username"], "fname": user["fname"], "userId": user["userId"]})
    return JSONResponse(status_code = 200, content = {
        "result" : True,
        "jwt": token,
        "message" : "Signin Success"
    })


@app.get("/user/me", response_model=UserMeResponse , responses={401: {"model": ErrorResponse}})
def get_user_me(credentials=Depends(security)):
    token = credentials.credentials if credentials else None
    if not token : 
        return JSONResponse(
            status_code=401,
            content={
                "result" : False,
                "error": "Please provide a JWT token for authentication"
            }
        )
    payload = decode_jwt(token)

    if not payload:
        return JSONResponse(
            status_code=401,
            content={
                "result" : False,
                "error": "JWT Verification Failed"
            }
        )

    users = read_users()
    user = next((u for u in users if u["username"] == payload["username"]), None)

    if not user:
        return JSONResponse(
            status_code=401,
            content={
                "result" : False,
                "error": "User not found"
            }

        )

    return UserMeResponse(
        result = True,
        data = UserMe(
        userId=user["userId"],
        username=user["username"],
        fname=user["fname"],
        lname=user["lname"],
        password=user["password"]
        )
    )
