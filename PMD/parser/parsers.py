from abc import ABCMeta, abstractmethod


class ParserBase(metaclass=ABCMeta):
    def __init__(self, inputFile, outputFile, extensions):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.extensions = extensions

    @abstractmethod
    def readDirectories(self):
        pass

    def _readDirectories(self,numWord):
        self._clearFile()
        directory = ''
        with open(self.inputFile, 'r') as f:
            for line in f:
                if len(line) == 0:
                    return
                elif line == '\n':
                    continue
                elif self._checkIfDirectory(line):
                    directory = self._parseDirectory(line)
                else:
                    title = self._parserLine(line,numWord)
                    if self._checkExtension(title):
                        self._writeMovie(directory+title)

    def _writeMovie(self, path_to_movie):
        with open(self.outputFile, 'a') as f:
            f.write(path_to_movie+'\n')

    def _clearFile(self):
        with open(self.outputFile, 'w') as f:
            f.write('')

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
        elif len(words[numWord-1])<numWord:
            return ''
        else:
            return words[numWord-1][0:-1]

    def _checkExtension(self, fileName):
        if len(fileName) > 3 and fileName[-4] == '.':
            for ext in self.extensions:
                if fileName.endswith(ext):
                    return True

        return False




class ParserLS(ParserBase):
    def readDirectories(self):
        self._readDirectories(9)

    def _checkIfDirectory(self, line):
        return line.startswith(".")

    def _parseDirectory(self, line):
        return line[0:-2]+'/'




class ParserDIR(ParserBase):
    def __init__(self, inputFile, outputFile, extensions):
        super(ParserDIR, self).__init__(inputFile, outputFile, extensions)
        self.firstDir = ''

    def readDirectories(self):
        self._setFirstDir()
        self._readDirectories(4)

    def _checkIfDirectory(self, line):
        return line.startswith(" Katalog:")

    def _parseDirectory_Zero(self, line):
        return (line[10:-1]+'/').replace("\\","/")

    def _parseDirectory(self, line):
        return self._parseDirectory_Zero(line).replace(self.firstDir,"./")


    def _setFirstDir(self):
        with open(self.inputFile, 'r') as f:
            i = 0
            for line in f:
                i += 1
                if i > 5:
                    self.firstDir= ''
                    return
                if len(line) == 0:
                    self.firstDir = ''
                    return
                elif self._checkIfDirectory(line):
                    self.firstDir = self._parseDirectory_Zero(line)
                    return
        self.firstDir = ''





def recognizeFileType(fileName):
    with open(fileName, 'r') as f:
        i = 0
        for line in f:
            i += 1
            if i > 5:
                return 'UNKNOWN'
            if len(line) == 0:
                return 'UNKNOWN'
            elif line == '.:\n':
                return 'LS'
            elif line.count('Katalog:') > 0:
                return 'DIR'

    return 'UNKNOWN'

