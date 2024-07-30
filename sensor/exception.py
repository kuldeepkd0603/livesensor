import sys 
import os 


def error_message_detial(error,error_detial:sys):
    _,_exc_tb =exc_error_detial.exc_info()git push origin main --force

    filename=exc_tb.tb_frame.f_code.co_filename
    
    
    filename=exc_tb.tb_frame.f_code.co_filename
    
    error_message="error occurd in the file namer is [{0}] and the line number is [{1} and the error is [{2}]]".format(filename,exc_tb.th_lineno,str(error))
     
     
    return error_message
class SesorException(Exception):
    
    
    def __init__(self,error_message,error_detial:sys):
        
        super().__init__(error_message)
        
        
        self.error_message=error_message_detial(error_message, error_detial=error_detial)
        
        
    def __str__(self):
        return self.error_message
    