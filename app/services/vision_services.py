import cv2
from app.models import VisionModel
from app.log import logging
from app.exceptions import LlmAppException,ImageProcessingError,ModelInferencingError
import sys
from app.instructions import VISION_INSTRUCTIONS
import numpy as np

class VisionModelServices:

    def __init__ (self):

        try:
            self.model = VisionModel()
            logging.info("Vision Model services initilized sucessfully")
        except Exception as e:
            logging.error(f"Error initilizing Vision Service : {e}")
            raise LlmAppException(e,sys)
    
    def process_request(self, image_file, prompt: str , instructions: str = VISION_INSTRUCTIONS) -> str:

        try:
            logging.info("Starting image processing and model inferencing")

            # Step 1: Load the image
            logging.info(f"Received image file: {image_file}")

            if isinstance(image_file, str):
                image = cv2.imread(image_file)
                if image is None:
                    raise ValueError(f"Failed to read image from path: {image_file}")
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            else:
                # Assuming it's UploadFile or file-like object (from FastAPI)
                image_bytes = image_file.file.read()
                nparr = np.frombuffer(image_bytes, np.uint8)
                image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                if image is None:
                    raise ValueError(f"Failed to decode uploaded image.")
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            logging.info("Image Loaded and converted to RGB")

            # Step 2 : Pass to model
            response = self.model.get_response(prompt, image_rgb, instructions)

            logging.info("Received response from the model")

            return response

        except IOError as e:

            logging.error(f"Error processing image: {e}")
            raise ImageProcessingError(detail="Invalid image format or unrelaible image")
        
        except Exception as e:
            logging.error(f"Model inferencing failed: {e}")
            raise ModelInferencingError(detail= "Error during model inferencing")
