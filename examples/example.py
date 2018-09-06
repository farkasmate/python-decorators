"""Decorator example."""

import sys
import logging
from decorators import log

@log
def query_data():
    """Querying data."""
    logging.info("Querying data.")

    result = "Example data"
    logging.debug("Raw data: %s", result) # Won't be printed with default level

    return result

@log(level=logging.DEBUG)
def persist_data(_data):
    """Persisting data."""
    logging.info("Persisting data.")

    logging.debug("Step 1.") # Printed as level is DEBUG
    logging.debug("Step 2.") # Printed as level is DEBUG
    logging.debug("Step 3.") # Printed as level is DEBUG

def main():
    """Main entry point for the script."""
    logging.info("Starting script.") # Won't be printed without decorator
    data = query_data()
    persist_data(data)

if __name__ == '__main__':
    sys.exit(main())
