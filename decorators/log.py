"""Log decorators."""

import logging

def log(func=None, level=logging.INFO):
    """Meta wrapper for handling optional level parameter."""
    def log_wrapper(func):
        """The actual wrapper."""
        def wrapper(*args, **kwargs):
            """Sets root logger level temporarily for the wrapped function."""
            root_logger = logging.getLogger()
            original_level = root_logger.getEffectiveLevel()
            root_logger.setLevel(level)

            result = func(*args, **kwargs)

            root_logger.setLevel(original_level)
            return result
        return wrapper
    if func:
        return log_wrapper(func)
    return log_wrapper
