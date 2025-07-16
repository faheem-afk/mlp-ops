# logging

    # logger 

        # Formatter
        
        # Levels
            # debug : checkpoints
            # info : important checkpoints - e.g.., model trained
            # warning : when some doesn't work, but it won't hinder the result
            # error : execution stopped
            # critical : website down
    
    # handler

        # file
    
        # console
    
    
import logging


logger = logging.getLogger("data_ingesttion_logger")
logger.setLevel('INFO')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

file_handler = logging.FileHandler('logs')
file_handler.setLevel('ERROR')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info('this is an info message')
logger.error('This is a error message')
