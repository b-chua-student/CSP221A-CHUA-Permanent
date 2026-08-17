import os
import unittest

from logger import configure_logging, ensure_log_directories

class LoggingTestCase(unittest.TestCase):
    LOGGER_NAME = "test_logging"
    LOG_FILE_PATH = "logs/tests/test_logging.log"

    def setUp(self) -> None:
        ensure_log_directories("logs/tests/")
        self.logger = configure_logging(filename=self.LOG_FILE_PATH, logger_name=self.LOGGER_NAME)

    def test_log_directory_exists(self) -> None:
        self.assertTrue(os.path.isdir("logs"))

    def test_logger_configuration(self) -> None:
        self.assertEqual(self.logger.name, self.LOGGER_NAME)

    def test_log_file_not_empty(self) -> None:

        self.assertTrue(os.path.exists(self.LOG_FILE_PATH))
        self.logger.info("Test log.")
        print("Size:", os.path.getsize(self.LOG_FILE_PATH))
        self.assertGreater(os.path.getsize(self.LOG_FILE_PATH), 0) # Raises OSError if LOG_FILE_PATH does not exist or is inaccessible.
        print(self.LOG_FILE_PATH)
