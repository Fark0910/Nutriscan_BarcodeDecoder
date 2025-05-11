
# main.py

from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.responses import JSONResponse
from dynamsoft_barcode_reader_bundle import *
import cv2
import numpy as np
from PIL import Image
import os
from dotenv import load_dotenv
import requests 

load_dotenv()  # Load variables from .env
license_key = os.getenv("DYNAMSOFT_LICENSE_KEY")

app = FastAPI()
# license of dynamo
err_code, err_str = LicenseManager.init_license(license_key)
if err_code not in [EnumErrorCode.EC_OK, EnumErrorCode.EC_LICENSE_CACHE_USED]:
    print("License initialization failed:", err_code, err_str)

cvr_instance = CaptureVisionRouter()

def decode_image(image_data):
    result_json = {"barcodes": []}
    captured_result = cvr_instance.capture(image_data, EnumPresetTemplate.PT_READ_BARCODES)
    if captured_result.get_error_code() != EnumErrorCode.EC_OK:
        return {"error": captured_result.get_error_string()}

    barcode_result = captured_result.get_decoded_barcodes_result()
    items = barcode_result.get_items() if barcode_result else []
    for item in items:
        result_json["barcodes"].append({
            "format": item.get_format_string(),
            "text": item.get_text()
        })
    return result_json

@app.post("/decode")
async def decode(file: UploadFile = File(...)): 
    try:
        content = await file.read()
        np_arr = np.frombuffer(content, np.uint8)
        image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if image is None:
            raise HTTPException(status_code=400, detail="Image decoding failed")

       
        try:
            requests.post("https://nutriscan-backend-api.onrender.com/fastapires", json={"message": "image under processing"})
        except Exception as express_error:
            print("Could not reach Express server:", express_error)

        result = decode_image(image)
        return JSONResponse(content=result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




