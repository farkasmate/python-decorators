# python-decorators

Example decorators.

## @log decorator

The @log decorator allows you to use the *logging* module and mark functions you want to log on certain log levels.

The default log elvel using @log without any parameter is INFO.

### Usage

    import logging
    from decorators import log

    @log(level=logging.INFO)
    def example():
        """Log decorator example."""
        logging.info("Info message.")   # Will be printed
        logging.debug("Debug message.") # Won't be printed

Check the examples directory for details.

## Run linter

    pipenv install --dev
    pipenv run pylint decorators

## Package

    pipenv run python setup.py sdist bdist_wheel
