from abc import ABCMeta, abstractmethod


class ParserBase(metaclass=ABCMeta):
    def __init__(self, inputText, extensions):
        self.input = inputText.splitlines()
        self.extensions = extensions

    @abstractmethod
    def readDirectories(self):
        pass

    def _readDirectories(self,numWord):
        directory = ''
        output = []
        for line in self.input:
            if len(line) == 0:
                continue
            elif line == '\n':
                continue
            elif self._checkIfDirectory(line):
                directory = self._parseDirectory(line)
            else:
                title = self._parserLine(line,numWord)
                if self._checkExtension(title):
                    output.append(directory+title)
        return output

    @abstractmethod
    def _checkIfDirectory(self, line):
        pass

    @abstractmethod
    def _parseDirectory(self, line):
        pass

    def _parserLine(self, line, numWord):
        words = line.split(None, numWord-1)
        if len(words) < numWord:
            return ''
        else:
            return words[numWord-1]

    def _checkExtension(self, title):
        if len(title) > 3 and title[-4] == '.':
            for ext in self.extensions:
                if title.endswith(ext):
                    return True
        return False


class ParserLS(ParserBase):
    def readDirectories(self):
        return self._readDirectories(9)

    def _checkIfDirectory(self, line):
        return line.startswith(".")

    def _parseDirectory(self, line):
        return line[0:-1]+'/'



class ParserDIR(ParserBase):
    def __init__(self, inputText, extensions):
        super(ParserDIR, self).__init__(inputText, extensions)
        self.firstDir = ''

    def readDirectories(self):
        self._setFirstDir()
        return self._readDirectories(4)

    def _checkIfDirectory(self, line):
        return line.startswith(" Katalog:")

    def _parseDirectory(self, line):
        return self._parseDirectory_Zero(line).replace(self.firstDir,"./")

    def _setFirstDir(self):
        i = 0
        for line in self.input:
            i += 1
            if i > 5:
                self.firstDir= ''
                return
            elif self._checkIfDirectory(line):
                self.firstDir = self._parseDirectory_Zero(line)
                return
        self.firstDir = ''

    def _parseDirectory_Zero(self, line):
        return (line[10:]+'/').replace("\\","/")



def recognizeFileType(inputText):
    i = 0
    for line in inputText.splitlines():
        i += 1
        if i > 5:
            return 'UNKNOWN'
        elif line == '.:':
            return 'LS'
        elif line.count('Katalog:') > 0:
            return 'DIR'

    return 'UNKNOWN'

