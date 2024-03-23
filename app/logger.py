from loguru import logger 

import sys 
log_format = "[{time}] - [{level}] - [{message}]"
loguro_config = {
  "handlers" : [
    {"sink": sys.stderr, "format": log_format, "level": "INFO", "colorize": True, "backtrace": True, "diagnose":True},
    {"sink": "../logs/info/info_{time}.log","level": "INFO",  "rotation": "500MB", "format": log_format, "colorize": True, "backtrace": True, "diagnose":True},
    {"sink": "../logs/debug/debug_{time}.log","level": "DEBUG",  "rotation": "500MB", "format": log_format, "colorize": True, "backtrace": True, "diagnose":True}
  ]
}
log = logger
log.configure(loguro_config)