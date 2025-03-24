import uvicorn
import cv2
from app.services.vision_services import VisionModelServices
from app.exceptions import LlmAppException
import sys

if __name__ == "__main__":

    try:
        print("Strating main.py")

        service = VisionModelServices()

        image_path = "/root/ChatBotLLM/acne.jpg"

        with open(image_path,"rb") as img_file:

            prompt = """
You are a professional dermatologist assistant. Analyze the given image and describe any visible skin condition or abnormality. Based on the appearance, categorize the condition as either minor or serious.

If the condition appears minor, provide practical suggestions, tips, or over-the-counter remedies that can help manage or improve the condition.

If the condition appears serious (e.g., severe infection, suspicious moles, deep wounds, signs of skin cancer, or anything that requires medical attention), respond strictly with:
'This condition appears serious. Please consult a qualified dermatologist or healthcare professional immediately.'

Do not attempt to give home remedies or solutions for serious cases.

and at the end add "Disclaimer: This analysis is AI-generated and should not replace professional medical advice. 


and add in bold "do you still need a consult with General Practioner ?"
"""

            output = service.process_request(image_file=image_path, promt= prompt)

            print("\n Generated o/p :\n", output)
            
    except Exception as e:
        raise LlmAppException(e,sys)         