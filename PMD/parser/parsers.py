from abc import ABCMeta, abstractmethod
from enum import Enum


class InputType(Enum):
    ls = 1
    dir = 2
    unknown = 3


class ParserBase(metaclass=ABCMeta):
    def __init__(self, input_text, extensions):
        self.input = input_text.splitlines()
        self.extensions = extensions

    @abstractmethod
    def read_directories(self):
        pass

    def _read_directories(self, num_word):
        directory = ''
        output = []
        for line in self.input:
            if len(line) == 0:
                continue
            elif line == '\n':
                continue
            elif self._check_if_directory(line):
                directory = self._parse_directory(line)
            else:
                title = self._parse_line(line, num_word)
                if self._check_extension(title):
                    output.append(directory + title)
        return output

    @abstractmethod
    def _check_if_directory(self, line):
        pass

    @abstractmethod
    def _parse_directory(self, line):
        pass

    @staticmethod
    def _parse_line(line, num_word):
        words = line.split(None, num_word - 1)
        if len(words) < num_word:
            return ''
        else:
            return words[num_word - 1]

    def _check_extension(self, title):
        if len(title) > 3 and title[-4] == '.':
            for ext in self.extensions:
                if title.endswith(ext):
                    return True
        return False


class ParserLS(ParserBase):
    def read_directories(self):
        return self._read_directories(9)

    def _check_if_directory(self, line):
        return line.startswith(".")

    def _parse_directory(self, line):
        return line[0:-1] + '/'


class ParserDIR(ParserBase):
    def __init__(self, input_text, extensions):
        super(ParserDIR, self).__init__(input_text, extensions)
        self.firstDir = ''

    def read_directories(self):
        self._set_first_dir()
        return self._read_directories(4)

    def _check_if_directory(self, line):
        return line.startswith(" Katalog:")

    def _parse_directory(self, line):
        return self._parse_directory_zero(line).replace(self.firstDir, "./")

    def _set_first_dir(self):
        i = 0
        for line in self.input:
            i += 1
            if i > 5:
                self.firstDir = ''
                return
            elif self._check_if_directory(line):
                self.firstDir = self._parse_directory_zero(line)
                return
        self.firstDir = ''

    @staticmethod
    def _parse_directory_zero(line):
        return (line[10:] + '/').replace("\\", "/")


def recognize_file_type(input_text):
    i = 0
    for line in input_text.splitlines():
        i += 1
        if i > 5:
            return InputType.unknown
        elif line == '.:':
            return InputType.ls
        elif line.count('Katalog:') > 0:
            return InputType.dir

    return InputType.unknown
