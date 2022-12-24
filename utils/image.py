import cloudinary
import cloudinary.uploader
import os
import dotenv
from fastapi import HTTPException

def tagging_image(img_url: str):
    dotenv.load_dotenv()
    cloud_name = os.environ.get('CLOUD_NAME')
    api_key = os.environ.get('API_KEY')
    api_secret = os.environ.get('API_SECRET')
    cloudinary.config(
        cloud_name=cloud_name,
        api_key=api_key,
        api_secret=api_secret
    )

    result = {"url": "", "type":""}
    uploaddata = cloudinary.uploader.upload(img_url,
                                            detection="cld-fashion", auto_tagging=0.6, )
    print(uploaddata["url"])
    result["url"] = uploaddata["url"]
    print(uploaddata["tags"][0])
    tag = uploaddata["tags"][0]
    result["type"] = tag
    try:
        attributesdata = uploaddata["info"]["detection"]["object_detection"]['data']["cld-fashion"]["tags"][tag][0]["attributes"]
    except:
        raise HTTPException(status_code=400, detail="Bat Image Request")

    if "sleeve length" in attributesdata:
        length = attributesdata["sleeve length"][0][0]
        print(length)
    elif "leg length" in attributesdata:
        length = attributesdata["leg length"][0][0]
        print(length)
    elif "skirt length" in attributesdata:
        length = attributesdata["skirt length"][0][0]
        print(length)
    else:
        length = "none"
        print("can't get length")

    seasonev = "none"

    if length in ["mini", "short", "above the knee"]:
        seasonev = "short"
    elif length in ["knee", "below the knee", "3/4 cropped", "elbow"]:
        seasonev = "midium"
    elif length in ["7/8 cropped", "three quarter", "midi"]:
        seasonev = "semilong"
    elif length in ["full", "maxi", "long (wrist)"]:
        seasonev = "long"
    else:
        seasonev = "nosleaves"
    print(seasonev)

    return result
