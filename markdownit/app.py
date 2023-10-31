import logging
import os
from typing import List, Set, TextIO

from bs4 import BeautifulSoup

from markdownit.config import Config


# TODO: exceptions


class Document:
    def __init__(self, html_file: TextIO):
        """
        TODO:
        setup other params and jekyll_frontmatter
        """
        self.soup: BeautifulSoup = BeautifulSoup(html_file, "html.parser")
        self.file_path = html_file.name


class MarkdownitApp:
    def __init__(self, config: Config):
        self._config: Config = config
        self.logger: logging.Logger = logging.getLogger(__class__.__name__)

    def run(self):
        """
        TODO
        send these files do preprocessor
        output from preprocessor send to converter
        write converted string to file
        """
        html_files: Set[str] = self.get_html_files()  # todo: check file type
        self.logger.info("Got %d files to process", len(html_files))

        while html_files:
            html_file: str = html_files.pop()

            with open(html_file, encoding='utf-8') as f:
                document: Document = Document(f)

            self.logger.info("Processing file: %s", document.file_path)

    def get_html_files(self) -> Set[str]:
        """
        Return set of html files.
        Join all html files from root_html_folder param from config.py
        and html_files list from config.py
        """
        files: Set[str] = set()
        if self._config.root_html_folder:
            files.update(self.list_dir(self._config.root_html_folder))
        if self._config.html_files:
            files.update(self._config.html_files)
        return files

    def list_dir(self, path: str) -> List[str]:
        f"""
        List recursively directory in path param and return list of files in the folder
        """
        files = []
        # todo: catch exceptions
        for filename in os.listdir(path):
            f: str = os.path.join(path, filename)
            if os.path.isfile(f):
                files.append(f)
            elif os.path.isdir(f):
                files.extend(self.list_dir(f))
        return files
