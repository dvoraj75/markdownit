import logging

from markdownit.app import MarkdownitApp
from markdownit.config import Config


if __name__ == "__main__":
    config = Config()
    logging.basicConfig(
        format=config.logginf_format,
        level=config.logging_level,
    )
    logger = logging.getLogger(__name__)
    # todo: accept list of files from command line
    logger.info("Starting markdownit app...")
    MarkdownitApp(config=config).run()
