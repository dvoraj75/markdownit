import logging

from typing import List


class Config:
    # main paths and params
    root_html_folder: str = "./digital-marketing"
    root_html_assets_folder: str = "./input_files/assets"
    root_md_folder: str = "./output_files/md_files"
    root_md_assets_folder: str = "./output_files/assets"
    html_files: List[str] = []

    # logging
    logging_level: int = logging.DEBUG
    logginf_format: str = "%(asctime)s:%(name)s:%(levelname)s: %(message)s"
