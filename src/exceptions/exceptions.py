from fastapi import FastAPI, HTTPException , status , APIRouter
from fastapi.responses import JSONResponse
from fastapi import Request


class ApplicationException(Exception):
    def __init__(self, name: str):
        self.name = name

class PasswordVerificationException(ApplicationException):
    def __init__(self, message: str , HTTPException: HTTPException = HTTPException):
        super().__init__("Password Verification Problem")
        self.message = message
        self.http_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    

class UserNotFoundException(ApplicationException):
    def __init__(self, message: str , HTTPException: HTTPException = HTTPException):
        super().__init__("User Not Found")
        self.message = message
        self.http_exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
class TokenInvalidException(ApplicationException):
    def __init__(self, message: str = "Token is invalid"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)

class InvalidUsernameOrPasswordException(ApplicationException):
    def __init__(self, message: str = "Invalid username or password"):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED)
    
class UserAlreadyExistsException(HTTPException):
    def __init__(self, message: str = "User already exists"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

class NoUsersFoundException(HTTPException):
    def __init__(self, message: str = "No users found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=message)

class TodoNotFoundException(ApplicationException):
    def __init__(self, message: str = "Todo not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND)

class NoTodosFoundException(ApplicationException):
    def __init__(self, message: str = "No todos found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND)


async def application_exception_handler(request: Request, exc: ApplicationException):
    return JSONResponse(
        status_code=exc.http_exception.status_code,
        content={"message": exc.message}
    )