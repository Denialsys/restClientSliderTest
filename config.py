import os
from logging.config import dictConfig

class Config(object):

	##Logger setup
	LOGGER_NAME = 'TestLogger'
	LOG_FILE = os.path.join(os.getcwd(), 'logs/logs.log')

	dictConfig ({
		'version': 1,
		
		## Specify here your prefered formater name and its log format
		'formatters': {
			'fileFormat': {
				'format': '[%(asctime)s] %(levelname)s %(name)s : %(funcName)s - %(message)s'
			},
			'stdoutFormat': {
				'format': '[%(asctime)s] %(levelname)s : %(funcName)s - %(message)s'
			}
		},

		## Specify your log handlers. 'console' : log to stdout or cli, 'file': log to a log file
		'handlers': {

			## This log handler will handle logging levels from INFO and up print it in cli
			'console' : {
				'level': 'INFO',
				'class': 'logging.StreamHandler',
				'formatter': 'stdoutFormat',
				'stream': 'ext://sys.stdout'
			},

			## This log handler will handle logging levels from DEBUG and up save it to file
			'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'fileFormat',
                'filename': LOG_FILE,
                'maxBytes': 1048576,
                'backupCount': 3
            }
		},

		## Set the name of our logger, its concerned logging level and its handlers
		'loggers': {
			LOGGER_NAME: {
				'level': 'DEBUG',
				'handlers': ['console', 'file']
			}
		},
	})