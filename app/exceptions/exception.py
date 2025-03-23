import sys
from app.core import logging

class LlmAppException(Exception):

    def __init__(self,error_message,error_details:sys):

        self.error_message = error_message
        _,_,exc_tb = error_details

        self.line_no = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):

        return "Error occured in python script name[{0}] Line number[{1}] error message[{2}]".format(
            self.file_name,self.line_no,self.error_message
        )
    