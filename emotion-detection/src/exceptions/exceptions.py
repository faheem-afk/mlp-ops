class CustomException(Exception):
    def __init__(self, error):
        self.error = error
        self.file_name = error.__traceback__.tb_frame.f_code.co_filename
        self.line_no = error.__traceback__.tb_lineno
       
    def __str__(self):
        return f"Error occurred in {self.file_name} at line {self.line_no}: {str(self.error)}"
    