import markdownify

import markdownit.app


class CustomMarkdownConverter(markdownify.MarkdownConverter):
    def __init__(self, document: "markdownit.app.Document", **options):
        self.document: "markdownit.app.Document" = document
        super().__init__(**options)

    def convert_document(self) -> str:
        md_string: str = self.convert_soup(self.document.soup)
        return md_string
