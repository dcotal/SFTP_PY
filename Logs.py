from datetime import datetime
import logging
   

def file_log():
        logger = logging.getLogger('SFTP_log')
        logger.setLevel(logging.DEBUG)
        now = datetime.now()
        file_dir = 'G:/log/' + now.strftime("%Y%m%d") + '.log'
        fh = logging.FileHandler(file_dir)
        fh.setLevel(logging.DEBUG)
        logger.addHandler(fh)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        if (logger.hasHandlers()):
            logger.handlers.clear()
        
        logger.addHandler(fh)
        return logger