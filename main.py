from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}


@app.get("/test")
async def root():
    return {"greeting": "Help", "message": "Omg"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}



# Launches the server by running the script - Added by me
if __name__ == '__main__':
    import subprocess
    subprocess.run(['uvicorn', 'example_API:app', '--reload'])
