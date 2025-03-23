import uvicorn
import cv2
from app.services.vision_services import VisionModelServices
from app.exceptions import LlmAppException

if __name__ == "__main__":

    try:
        print("Strating main.py")

        service = VisionModelServices()

        image_path = "/Scenary.jpg"

        with open(image_path,"rb") as img_file:

            prompt = "Describe the image"

            output = service.process_request(image_file=image_path, promt= prompt)

            print("\n Generated o/p :\n", output)
            
            