import traceback
import functools
from libs import ResponseCode as Rc


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def router_exception_checker(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            print(bcolors.WARNING + traceback.format_exc() + bcolors.ENDC)
            error_msg = 'exception {}: {}'.format(type(e).__name__, e.message)
            return Rc(type_='unknown',
                      msg_=error_msg).customized_error()
    return wrapper