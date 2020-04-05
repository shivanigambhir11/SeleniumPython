import logging

class BaseClass:


    def test_loggingDemo(self):
        logger = logging.getLogger(__name__)      # __create object of logging &"_ name__"= @ runtime it will fetch test case name

        filehandler = logging.FileHandler("logfile.log")  # file location , it will come from parent

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # [asctime for timestamp, level name for info/critical, name for test case name
                                                                                            # message for actual message ]
        filehandler.setFormatter(formatter)  # pass the formatter info into filehandler using setformatter and the filehandler will take that in addhandler along

        logger.addHandler(filehandler)  # create a file where information will be stored,  it's a method which will accept file handler,

        logger.setLevel(logging.INFO)  # order is like debug, info, error, warning and critical. If i say Info debug is above that will not be printed


        return logger
        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.warning("some thing is in warning mode")
        # logger.error("A major error has happened")
        # logger.critical("Critical issue- null pointer exception")


