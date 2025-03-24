from fastapi import APIRouter, UploadFile, Form ,File
from app.services import QuestionServices,VisionModelServices
from app.exceptions import LlmAppException

router = APIRouter()

@router.post("/v1/analyze")
async def analyze_patient(
    user_answers: str = Form(...),
    image: UploadFile = File(...)
):  
    print("Iam here")
    try:
        # print(user_answers,"user_answers")
        # Initialize services
        question_service = QuestionServices()
        vision_service = VisionModelServices()

        # 1. Analyze patient answers
        question_output = question_service.analyze_patient_answers(
            user_answers=user_answers
        )

        # 2. Analyze image with combined prompt
        image_prompt = "Analyze the provided medical image based on patient information."
        combined_prompt = question_output + " " + image_prompt

        vision_output = vision_service.process_request(
            image_file=image,
            prompt=combined_prompt
        )

        return {
            "question_model_analysis": question_output,
            "vision_model_analysis": vision_output
        }

    except Exception as e:
        raise LlmAppException(e)
