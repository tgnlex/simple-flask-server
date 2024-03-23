from loguru import logger

log = logger
log.trace("A trace message.")
log.debug("A debug message.")
log.info("An info message.")
log.success("A success message.")
log.warning("A warning message.")
log.error("An error message.")
log.critical("A critical message.")
log.level("EMERGENCY", no=60, color="<red>", icon="!!!")
log.log=("EMERGENCY", "Status: {status}", "Warning, please address this immediately. Message: {message}", "File: {file}",)