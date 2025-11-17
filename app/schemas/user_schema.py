from pydantic import BaseModel, Field
from typing import Annotated

Username = Annotated[
    str,
    Field(
        min_length=4,
        pattern=r"^[a-z0-9]+$",
        description="Username must be lowercase alphabets only, min length 4",
        example="rajesh123",
    )
]

Password = Annotated[
    str,
    Field(
        min_length=5,
        pattern=r"^[A-Za-z0-9@#\$%\^&\*\!\?\-_\.]+$",
        description=(
            "At least 5 characters. Must include: 1 uppercase, 1 lowercase, 1 digit. "
            "Special characters not allowed."
        ),
        example="Rajesh@123",
    )
]
FirstName = Annotated[
    str,
    Field(
        pattern=r"^[A-Za-z]+$",
        description="Alphabets only",
        example="Rajesh",
    )
]
LastName = Annotated[
    str,
    Field(
        pattern=r"^[A-Za-z]+$",
        description="Alphabets only",
        example="Kanade",
    )
]

class SignupRequest(BaseModel):
    username: Username
    password: Password
    fname: FirstName
    lname: LastName


class SigninRequest(BaseModel):
    username: Username
    password: Annotated[
        str,
        Field(
            min_length=5,
            description="Raw password for signing in",
            example="Rajesh@123",
        )
    ]

class SimpleResult(BaseModel):
    result: bool = Field(..., example=True)
    message: str | None = Field(default=None, example="Signup successful")


class SigninSuccess(BaseModel):
    result: bool = Field(..., example=True)
    jwt: str = Field(..., description="JWT token", example="eyJhbGciOiJIUzI1NiIs...")
    message: str = Field(..., example="Signin successful")


class UserData(BaseModel):
    fname: str = Field(..., example="Rajesh")
    lname: str = Field(..., example="Kanade")
    password: str = Field(..., example="$2b$12$abcd...")  # hashed password

class UserResponse(BaseModel):
    result: bool = Field(..., example=True)
    data: UserData
    
    
class UserMe(BaseModel): 
    userId: str = Field(..., example="741a35bd-b2d1-4652-9d0a-576ee3c238f2")
    username: str = Field(..., example="rajesh123")
    fname: str = Field(..., example="Rajesh")
    lname: str = Field(..., example="Kanade")
    password : str= Field(..., example="$2b$12$abcd...")

class UserMeResponse(BaseModel):
    result: bool = Field(..., example=True)
    data: UserMe


class ErrorResponse(BaseModel):
    result: bool = Field(default=False, example=False)
    error: str = Field(..., example="Invalid token")
