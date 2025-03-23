from langchain_community.chat_models import ChatOllama
from langchain.schema.messages import HumanMessage
import base64
import cv2
import io
import numpy as np
import sys
from app.constants import  VISION_MODEL_NAME
from app.exceptions import LlmAppException
from app.logging import logging

class VisionModel:

    def __init__(self):
        try:
            self.llm = ChatOllama(model = VISION_MODEL_NAME)
            logging.info(f"Llama vision model {VISION_MODEL_NAME} initiated sucessfully ")

        except Exception as e:
            logging.error(f"Failed to initilize Llama Model: {e}")
        
    def encode_image(self,image : np.ndarray) -> str:

        try:
            # encode image to memeory buffer in jpeg format 
            success, buffer = cv2.imencode('.jpg',image)

            if not success:
                raise ValueError("could not encode image")
            
            img_base64 = base64.b64encode(buffer).decode("utf-8")

            logging.info("Image sucessfully encoded to base 64 using openc cv")

            return img_base64
        
        except Exception as e:
            
            logging.error(f"Error encoding the image: {e}")
            raise LlmAppException(e,sys)

    def get_response(self, promt: str, image: np.ndarray) -> str:

        try:
            image_b64 = self.encode_image(image)

            message = HumanMessage(
                content = [
                    {"type" : "text" , "text": promt},
                    {"type" : "image_url", "image_url": {"url": f" data:image/jpeg;base64,{image_b64}"}}
            ]
            )

            response = self.llm([message])
            logging.info(f"Sucessfully generated respoanse from {VISION_MODEL_NAME}")

            return response.content
        
        except Exception as e:
            logging.error(f"Error during model inference: {e}")
            raise LlmAppException(e,sys)

