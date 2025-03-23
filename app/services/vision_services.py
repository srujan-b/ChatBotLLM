import cv2
from models import VisionModel
from core import logging
from exceptions import LlmAppException,ImageProcessingError,ModelInferencingError
import sys

class VisionModelServices:

    def __init__ (self):

        try:
            self.model = VisionModel()
            logging.info("Vision Model services initilized sucessfully")
        except Exception as e:
            logging.error(f"Error initilizing Vision Service : {e}")
            raise LlmAppException(e,sys)
    
    def process_request(self, image_file, promt: str) -> str:

        try:
            logging.info("Strting image processing and model inferencing")

            # step 1: load the image

            image = cv2.imload(image_file)
            image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

            logging.info("Image Loaded and converted to RGB")

            # step2 : pass the model

            response = self.model.get_response(promt,image_rgb)

            logging.info("Received response from the model")

            return response

        except IOError as e:

            logging.error(f"Error processing image: {e}")
            raise ImageProcessingError(detail="Invalid image format or unrelaible image")
        
        except Exception as e:
            logging.error(f"Model inferencing failed: {e}")
            raise ModelInferencingError(detail= "Error during model inferencing")
