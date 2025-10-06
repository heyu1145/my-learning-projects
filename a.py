import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test")
logger.info("Hello!")
logger.debug("debugging")
logger.warning("Warn!")
logger.error("Error!")
