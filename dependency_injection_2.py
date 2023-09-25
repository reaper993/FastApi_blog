from fastapi import FastAPI, Depends

dev_db = ["DB for Development"]

def get_db_session():
    return dev_db

app = FastAPI()

@app.post("/items")
def add_item(item: str, db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {"message": f"Added item: {item}"}