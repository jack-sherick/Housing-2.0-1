from typing import Annotated
import uvicorn
from fastapi import Body, FastAPI, File, UploadFile
from pydantic import BaseModel

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(f: UploadFile):
    return {"Filename": f.file.read()}

@app.post("/file/")
async def create_file(f: Annotated[bytes, File()]):
    for i in range(0, len(f)):
        print(f[i])
    #return {"test": len(f)}

@app.get("/items/{item_id}")
async def create_item(item_id: int):
    return {"Items": item_id}

if __name__ == '__main__':
    pass
    #uvicorn.run(app, host='127.0.0.1', port=8000)