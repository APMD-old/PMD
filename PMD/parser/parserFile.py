import parsers

class parserFile:
    def __init__(self):
        self.extensions = ("avi","mp4","mkv")

    def readDirectories(self, inputText):
        type = parsers.recognizeFileType(inputText)

        if( type  == "LS" ):
            parser = parsers.ParserLS(inputText, self.extensions)
        elif( type  == "DIR" ):
            parser = parsers.ParserDIR(inputText, self.extensions)
        else :
            return []

        return parser.readDirectories()
