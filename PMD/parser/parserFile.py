import parsers

class parserFile:
    def __init__(self, inputFile, outputFile):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.extensions = ("avi","mp4","mkv")

    def readDirectories(self):
        type = parsers.recognizeFileType(self.inputFile)

        if( type  == "LS" ):
            parser = parsers.ParserLS(self.inputFile, self.outputFile,self.extensions)
        elif( type  == "DIR" ):
            parser = parsers.ParserDIR(self.inputFile, self.outputFile,self.extensions)
        else :
            return -1

        parser.readDirectories()
        return 0
