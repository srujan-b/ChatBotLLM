from app.models import QuestionAnalysisModel
from app.log import logging
from app.exceptions import LlmAppException,ModelInferencingError
import sys
from app.instructions import QUESTIONS_INSTRUCTIONS

class QuestionServices:

    def __init__(self):

        try:
            self.model = QuestionAnalysisModel()
            logging.info("QuestionService Initilized sucessfully")
        except Exception as e:
            logging.error("QuestionService Initilized Failed")
            raise LlmAppException(e,sys)
    
    def analyze_patient_answers(self , user_answers : str , instructions :str = QUESTIONS_INSTRUCTIONS ) -> str:

        try: 
            logging.info("Starting patient question analysis")

            response = self.model.get_response(instructions , user_answers)


            logging.info("Sucessfully received response from Questions Model")
            return response

        except Exception as e:
            logging.error("Error during questions model inference : {e}")
            raise ModelInferencingError(detail = "Error analysing patient answers ")
