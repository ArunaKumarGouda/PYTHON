from fastapi import FastAPI

app = FastAPI()

@app.get("/greet/{name}")
async def greet_user(name: str):  # 'name' parameter is type-hinted as a string
    return {"message": f"Hello, {name}!"}

# Terminal: uvicorn 04_FastAPI:app --reload
# Browser: http://127.0.0.1:8000/docs
# Browser: http://127.0.0.1:8000/greet/Arun
