import uvicorn
import cv2
from app.services import VisionModelServices,QuestionServices
from app.exceptions import LlmAppException
from app.log import logging
import sys

if __name__ == "__main__":

    try:


        print("Strating main.py")

        question_service = QuestionServices()

        user_answers = "I have achne problem for a long time i have used all kind of medication but is of no use its a serious issue I think i need to consult a doctor"
        question_output = question_service.analyze_patient_answers(
        user_answers=user_answers)
        print("\nQuestion Model Output:\n", question_output)


        vision_service = VisionModelServices()

        image_path = "/root/ChatBotLLM/acne.jpg"

        with open(image_path,"rb") as img_file:

           
            image_prompt = "Check for any medical abnormalities in this image."
            vision_output = vision_service.process_request(
                image_file=image_path,
                prompt=question_output +" "+ image_prompt
            )
            print("\nVision Model Output:\n", vision_output)
    except Exception as e:
        raise LlmAppException(e)         