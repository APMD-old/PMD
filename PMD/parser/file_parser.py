from PMD.parser.parsers import InputType
from . import parsers


class FileParser:
    def __init__(self):
        self.extensions = ("avi", "mp4", "mkv")

    def read_directories(self, input_text):
        type = parsers.recognize_file_type(input_text)

        if type == InputType.ls:
            parser = parsers.ParserLS(input_text, self.extensions)
        elif type == InputType.dir:
            parser = parsers.ParserDIR(input_text, self.extensions)
        else:
            return []

        return parser.read_directories()
