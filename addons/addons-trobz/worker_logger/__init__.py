# Copyright 2009-2018 Trobz (http://trobz.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

import logging
import logging.handlers
import os
from openerp import tools
import sys
import threading

_logger = logging.getLogger(__name__)

_logger.addHandler(logging.StreamHandler(sys.stdout))

path_prefix = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, _NOTHING, DEFAULT = range(10)
# The background is set with 40 plus the number of the color, and the foreground with 30
# These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"
COLOR_PATTERN = "%s%s%%s%s" % (COLOR_SEQ, COLOR_SEQ, RESET_SEQ)
LEVEL_COLOR_MAPPING = {
    logging.DEBUG: (BLUE, DEFAULT),
    logging.INFO: (GREEN, DEFAULT),
    logging.WARNING: (YELLOW, DEFAULT),
    logging.ERROR: (RED, DEFAULT),
    logging.CRITICAL: (WHITE, RED),
}


class DBFormatter(logging.Formatter):
    def format(self, record):
        record.pid = os.getpid()
        record.dbname = getattr(threading.currentThread(), 'dbname', '?')
        return logging.Formatter.format(self, record)


_logger_init = False


def init_logger():
    global _logger_init
    if _logger_init:
        return
    _logger_init = True

    root_logger = logging.getLogger()
    # create a format for log messages and dates
    format = '%(asctime)s %(pid)s %(levelname)s %(dbname)s %(name)s: %(message)s'

    if tools.config['logfile']:
        # LogFile Handler
        logf = tools.config['logfile']

        # in case, logfile is stdout, don't override
        if 'stdout' in logf:
            return

        try:
            # We check we have the right location for the log files
            dirname = os.path.dirname(logf)
            if dirname and not os.path.isdir(dirname):
                os.makedirs(dirname)

            if tools.config['logrotate'] is not False \
                    and int(tools.config['workers']) > 1:
                _logger.info("# OVERRIDE NATIVE logrotate init_logger #")
                try:
                    # try to import TimedRotatingFileHandlerSafe
                    from safe_logger import TimedRotatingFileHandlerSafe
                    log_handler = TimedRotatingFileHandlerSafe

                    # remove native TimedRotatingFileHandler of python
                    for handler in root_logger.handlers[:]:
                        # check if has TimedRotatingFileHandler
                        if isinstance(
                            handler,
                            logging.handlers.TimedRotatingFileHandler
                        ):
                            # remove TimedRotatingFileHandler from root Logger
                            root_logger.removeHandler(handler)

                            # set update new log_handler time safe
                            new_handler = log_handler(
                                filename=logf, when='D',
                                interval=1, backupCount=30
                            )
                            formatter = DBFormatter(format)
                            new_handler.setFormatter(formatter)
                            root_logger.addHandler(new_handler)
                            _logger.info(
                                "################# Using  "
                                "TimedRotatingFileHandlerSafe ###############"
                            )
                except Exception:
                    _logger.error(
                        " >>> OVERRIDE logfile rotate with multi-worker Fail #"
                    )
            else:
                _logger.error("""Don't meet requirement to override logrotate.
                              These settings in your config file must be: \n
                              1. Logrotate = True \n
                              2. Workers > 1""")

        except Exception:
            sys.stderr.write(
                "ERROR: couldn't create the logfile directory."
                " Logging to the standard output.\n")


# self invoke to override
init_logger()
