from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse

from convert_png import convert_png
from remove_background import remove_background

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/remove-bg")
async def handle_remove_background(file: UploadFile = File(...)):
    input_image = await file.read()
    output_image = remove_background(input_image)
    output_io = convert_png(output_image)

    return StreamingResponse(output_io, media_type="image/png")
