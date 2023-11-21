import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")



logging.basicConfig(level=logging.DEBUG, filename="logs.log",
                    filemode="w", format="we have next logging"
                    " message:%(asctime)s:%(levelname)s - %(message)s")
logging.debug("debug")
logging.info("info")
