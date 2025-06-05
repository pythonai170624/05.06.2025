from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI(title="Example API", description="A simple FastAPI with Swagger UI", version="1.0")

# Define a Pydantic model for input data
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI example!"}

# Define a POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item_received": item}
