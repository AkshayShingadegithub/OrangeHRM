import inspect
import logging

class LogGenerator:

    @staticmethod
    def loggen():

        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\Pytest rev\\orangeHRM scratch\\Logs\\test_login_ddt")
        format = logging.Formatter("%(asctime)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
