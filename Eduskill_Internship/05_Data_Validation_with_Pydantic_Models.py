from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class User(BaseModel):
    username: str
    age: int  # Type-hinted as integer

@app.post("/users/")
async def create_user(user: User):  # 'user' parameter is type-hinted as our User model
    # FastAPI automatically validates the incoming JSON against the User model
    # If validation fails, it returns a 422 error
    return {"message": f"User {user.username} created successfully with age {user.age}."}



#  Terminal: uvicorn 05_Data_Validation_with_Pydantic_Models:app --reload
#  Browser: http://127.0.0.1:8000/docs
