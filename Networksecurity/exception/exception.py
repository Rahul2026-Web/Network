import os
import sys

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from networksecurity.logging import logger  # ✅ This will import the logger object

class NetworksecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb else "Unknown"
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"

    def __str__(self):
        return (
            f"Error occurred in python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message [{self.error_message}]"
        )

if __name__ == "__main__":
    try:
        logger.logger.info("Enter the try block")  # ✅ Corrected usage
        a = 1 / 0
    except Exception as e:
        raise NetworksecurityException(e, sys) from e
