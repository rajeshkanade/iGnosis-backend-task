# User Authentication API

A lightweight, fast, and secure user authentication server built with **FastAPI** and **Python**. This application provides user signup, signin, and profile management with JWT token-based authentication.

## 🎯 Overview

This API implements a complete authentication system with:
- User registration (Signup)
- User login (Signin) with JWT token generation
- Secure user profile access
- Password hashing using bcrypt
- JSON file-based data storage (no database required)

## 📋 Features

✅ **User Signup** - Create new user accounts with validation
✅ **User Signin** - Authenticate users and receive JWT tokens
✅ **User Profile** - Access authenticated user information
✅ **Data Validation** - Strict validation rules for username, password, and names
✅ **Password Security** - Passwords are hashed using bcrypt
✅ **JWT Authentication** - Token-based authentication for protected endpoints
✅ **JSON Storage** - Users stored in `users.json` file (no external database needed)

## 🏗️ Project Structure

```
backend-python/
├── app/
│   ├── __init__.py
│   ├── config.py                 # Configuration and secrets
│   ├── main.py                   # FastAPI application and endpoints
│   ├── users.json                # User data storage
│   ├── schemas/
│   │   └── user_schema.py        # Pydantic models for request/response validation
│   └── utils/
│       ├── auth.py               # Authentication utilities (hashing, JWT)
│       └── file_handler.py       # JSON file operations
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (create this)
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (if using git):
```bash
git clone <your-repo-url>
cd backend-python
```

2. **Create a virtual environment**:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Create `.env` file** (optional, for custom JWT secret):
```bash
echo JWT_SECRET=your_super_secret_key_here > .env
```

5. **Run the server**:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

The app is deployed and publicly available at: `https://ignosis-backend-task-production.up.railway.app/`

## 📚 API Endpoints

### 1. User Signup

Create a new user account.

**Endpoint:** `POST /signup`

**Request Body:**
```json
{
  "username": "rajesh123",
  "password": "Rajesh@123",
  "fname": "Rajesh",
  "lname": "Kanade"
}
```

**Success Response (201 Created):**
```json
{
  "result": true,
  "message": "SignUp success. Please proceed to Signin"
}
```

**Error Response (400 Bad Request):**
```json
{
  "result": false,
  "error": "Username already exists"
}
```

**Validation Rules:**
- `username`: Lowercase letters and numbers only, minimum 4 characters
- `password`: Minimum 5 characters, must contain 1 uppercase, 1 lowercase, 1 digit. No special characters allowed
- `fname`: English alphabets only
- `lname`: English alphabets only

---

### 2. User Signin

Authenticate user and receive JWT token.

**Endpoint:** `POST /signin`

**Request Body:**
```json
{
  "username": "rajesh123",
  "password": "Rajesh@123"
}
```

**Success Response (200 OK):**
```json
{
  "result": true,
  "jwt": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "message": "Signin Success"
}
```

**Error Response (401 Unauthorized):**
```json
{
  "result": false,
  "error": "Invalid username or password"
}
```

---

### 3. Get User Profile

Retrieve authenticated user's information.

**Endpoint:** `GET /user/me`

**Headers Required:**
```
Authorization: <JWT_TOKEN>
```

Example:
```
Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Success Response (200 OK):**
```json
{
  "result": true,
  "data": {
    "userId": "741a35bd-b2d1-4652-9d0a-576ee3c238f2",
    "username": "rajesh123",
    "fname": "Rajesh",
    "lname": "Kanade",
    "password": "$2b$12$abcd..."
  }
}
```

**Error Response (401 Unauthorized) - Missing Token:**
```json
{
  "result": false,
  "error": "Please provide a JWT token for authentication"
}
```

**Error Response (401 Unauthorized) - Invalid Token:**
```json
{
  "result": false,
  "error": "JWT Verification Failed"
}
```

---

## 🧪 Testing with Postman

### Video Demo

Watch the complete API validation video showing all endpoints running successfully:

<video width="100%" controls>
  <source src="postman-validation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Video Contents:**
- ✅ Successful user signup
- ✅ Successful user signin with JWT token
- ✅ Successful user profile retrieval
- ✅ All API responses in Postman

[📥 Download Video](./postman-validation.mp4)

### Setup

1. **Download Postman** from [postman.com](https://www.postman.com)

2. **Import Collection** (Optional):
   - Click `Import` → `URL`
   - Paste: `https://raw.githubusercontent.com/UXGorilla/hiring-backend/main/collection.json`

3. **Set Environment Variables**:
   - Click the settings icon (gear icon)
   - Create new environment or select existing
   - Add variables:
     - `baseUrl`: `http://localhost:8000`
     - `username`: `rajesh123` (test username)
     - `password`: `Rajesh@123` (test password)
     - `fname`: `Rajesh`
     - `lname`: `Kanade`

4. **API Postman Validate Successfully**
    ![Image](/postman-validation.png)

### Test Workflow

1. **Create a request for Signup:**
   - Method: `POST`
   - URL: `{{baseUrl}}/signup`
   - Body (raw JSON):
   ```json
   {
     "username": "{{username}}",
     "password": "{{password}}",
     "fname": "{{fname}}",
     "lname": "{{lname}}"
   }
   ```

2. **Create a request for Signin:**
   - Method: `POST`
   - URL: `{{baseUrl}}/signin`
   - Body (raw JSON):
   ```json
   {
     "username": "{{username}}",
     "password": "{{password}}"
   }
   ```
   - After running, the JWT token will be automatically saved to `accessToken` variable

3. **Create a request for Get User Profile:**
   - Method: `GET`
   - URL: `{{baseUrl}}/user/me`
   - Headers:
     - Key: `Authorization`
     - Value: `{{accessToken}}`

4. **Run all tests:**
   - Click the `Run` button in Postman
   - Select your collection
   - Click `Run Collection`

---

## 🧪 Testing with Newman (CLI)

### Installation

```bash
npm install -g newman
```

### Run Tests

```bash
newman run --env-var baseUrl="http://localhost:8000" --env-var username="rajesh123" --env-var password="Rajesh@123" https://raw.githubusercontent.com/UXGorilla/hiring-backend/main/collection.json
```

---

## 📁 Data Storage

### users.json Format

User data is stored in `app/users.json` with the following structure:

```json
[
  {
    "userId": "741a35bd-b2d1-4652-9d0a-576ee3c238f2",
    "username": "rajesh123",
    "fname": "Rajesh",
    "lname": "Kanade",
    "password": "$2b$12$abcd..."
  },
  {
    "userId": "852b46ce-c3e2-4763-ae1b-687ff4d349g3",
    "username": "john123",
    "fname": "John",
    "lname": "Doe",
    "password": "$2b$12$efgh..."
  }
]
```

---

## 🔐 Security Features

### Password Hashing
- Uses **bcrypt** library for secure password hashing
- Original password is never stored
- Passwords are hashed with a salt value

### JWT Authentication
- JWT tokens are signed with a secret key
- Tokens include username and first name
- Tokens expire after 1 hour
- Invalid or expired tokens are rejected

### Input Validation
- Pydantic models enforce strict validation
- Username must be lowercase alphanumeric
- Password requires mix of uppercase, lowercase, and numbers
- Names are validated to contain only alphabets

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:

```
fastapi==0.121.2          # Web framework
uvicorn==0.38.0           # ASGI server
pydantic==2.12.4          # Data validation
PyJWT==2.10.1             # JWT token creation/verification
bcrypt==5.0.0             # Password hashing
python-dotenv==1.0.0      # Environment variable management
```

To install all dependencies:
```bash
pip install -r requirements.txt
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
JWT_SECRET=your_super_secret_key_here_change_in_production
```

If not provided, a default secret is used (change this in production!).

---

## 📝 Example Workflow

Here's a complete example of how to use the API:

```bash
# 1. Start the server
uvicorn app.main:app --reload

# 2. Signup a new user
curl -X POST "http://localhost:8000/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice123",
    "password": "Alice@456",
    "fname": "Alice",
    "lname": "Smith"
  }'

# Response:
# {"result": true, "message": "SignUp success. Please proceed to Signin"}

# 3. Signin to get JWT token
curl -X POST "http://localhost:8000/signin" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice123",
    "password": "Alice@456"
  }'

# Response:
# {"result": true, "jwt": "eyJ0eXAi...", "message": "Signin Success"}

# 4. Access user profile with token
curl -X GET "http://localhost:8000/user/me" \
  -H "Authorization: eyJ0eXAi..."

# Response:
# {"result": true, "data": {"userId": "...", "username": "alice123", ...}}
```

---

## 🐛 Troubleshooting

### Issue: Port 8000 is already in use
**Solution:** Use a different port:
```bash
uvicorn app.main:app --reload --port 8001
```

### Issue: ModuleNotFoundError
**Solution:** Make sure you've installed dependencies:
```bash
pip install -r requirements.txt
```

### Issue: JWT Verification Failed
**Solution:** 
- Ensure the token is not expired (valid for 1 hour)
- Verify the token is passed correctly in the Authorization header
- Check that the JWT_SECRET is the same on server

### Issue: Username already exists
**Solution:**
- Use a different username
- Or delete the user from `app/users.json` and restart the server

---

## 📄 License

This project is part of the iGnosis Tech hiring process.

---

## 👤 Author

Created as part of the Backend Engineering interview process at iGnosis Tech.

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the API documentation
3. Test endpoints using Postman
4. Check server logs for error messages

---

## ✅ Validation Examples

### Valid Username Examples
✅ `rajesh123` - lowercase with numbers
✅ `alice` - all lowercase
✅ `john99` - lowercase with numbers

### Invalid Username Examples
❌ `Rajesh` - contains uppercase
❌ `raj` - less than 4 characters
❌ `raj@` - contains special character

### Valid Password Examples
✅ `Rajesh@123` - has uppercase, lowercase, digit
✅ `SecurePass1` - has uppercase, lowercase, digit
✅ `MyPass99` - has uppercase, lowercase, digit

### Invalid Password Examples
❌ `password` - no uppercase or digit
❌ `PASS123` - no lowercase
❌ `pass123` - no uppercase
❌ `Pass@123` - contains special character
❌ `Pass1` - only 5 chars (minimum exactly 5)

---

## 🎓 Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [JWT Introduction](https://jwt.io/introduction)
- [Bcrypt Hashing](https://en.wikipedia.org/wiki/Bcrypt)

---

**Happy Coding! 🚀**
