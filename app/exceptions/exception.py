import sys
from fastapi import HTTPException


class LlmAppException(Exception):

    def __init__(self, error_message):
        super().__init__(error_message)

        # Get traceback info
        exc_type, exc_value, exc_tb = sys.exc_info()

        if exc_tb is not None:
            self.line_no = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.line_no = None
            self.file_name = None

        self.error_message = error_message

    def __str__(self):
        return "Error occurred in python script name [{0}] Line number [{1}] error message [{2}]".format(
            self.file_name, self.line_no, self.error_message
        )

class ImageProcessingError(HTTPException):

    def __init__(self,detail= "Image Processing Error"):
        super().__init__(status_code = 400, detail = detail)

class ModelInferencingError(HTTPException):

    def __init__(self,detail = "Model Inferencing Error"):
        super().__init__(status_code = 500, detail = detail)


    