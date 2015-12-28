from unittest import TestCase
from mock import Mock, patch, mock_open
import builtins
import parsers
from parserFile import parserFile

DataForTest_LS = """.:
total 12
-rw------- 1 zdzich zdzich 1659 gru 13 18:03 DIR_File.txt
drwx------ 2 zdzich zdzich 4096 gru 13 17:55 Epoka Lodowcowa
drwx------ 4 zdzich zdzich 4096 gru 13 17:54 Kły
-rw-rw-r-- 1 zdzich zdzich    0 gru 13 18:18 LS_File.txt

./Epoka Lodowcowa:
total 0
-rw------- 1 zdzich zdzich 0 gru 13 17:55 Epoka Lodowcowa.avi

./Kły:
total 8
drwx------ 2 zdzich zdzich 4096 gru 13 17:54 Sezon1
drwx------ 2 zdzich zdzich 4096 gru 13 17:55 Sezon2

./Kły/Sezon1:
total 0
-rw------- 1 zdzich zdzich 0 gru 13 17:53 Kly1.mp4
-rw------- 1 zdzich zdzich 0 gru 13 17:52 Kly1.txt
-rw------- 1 zdzich zdzich 0 gru 13 17:54 Kly2.avi
-rw------- 1 zdzich zdzich 0 gru 13 17:52 Kly2.txt

./Kły/Sezon2:
total 0
-rw------- 1 zdzich zdzich 0 gru 13 17:54 Kly10.mp4
-rw------- 1 zdzich zdzich 0 gru 13 17:54 Kly10.txt
-rw------- 1 zdzich zdzich 0 gru 13 17:54 Kly11.avi
"""

DataForTest_DIR = """
 Wolumin w stacji D nie ma etykiety.
 Numer seryjny woluminu: E0EF-67C2

 Katalog: D:\Filmy

2015-12-13  18:03    <DIR>          .
2015-12-13  18:03    <DIR>          ..
2015-12-13  18:03                 0 DIR_File.txt
2015-12-13  17:55    <DIR>          Epoka Lodowcowa
2015-12-13  17:54    <DIR>          Kły
               1 plik(ów)                  0 bajtów

 Katalog: D:\Filmy\Epoka Lodowcowa

2015-12-13  17:55    <DIR>          .
2015-12-13  17:55    <DIR>          ..
2015-12-13  17:55                 0 Epoka Lodowcowa.avi
               1 plik(ów)                  0 bajtów

 Katalog: D:\Filmy\Kły

2015-12-13  17:54    <DIR>          .
2015-12-13  17:54    <DIR>          ..
2015-12-13  17:54    <DIR>          Sezon1
2015-12-13  17:55    <DIR>          Sezon2
               0 plik(ów)                  0 bajtów

 Katalog: D:\Filmy\Kły\Sezon1

2015-12-13  17:54    <DIR>          .
2015-12-13  17:54    <DIR>          ..
2015-12-13  17:53                 0 Kly1.mp4
2015-12-13  17:52                 0 Kly1.txt
2015-12-13  17:54                 0 Kly2.avi
2015-12-13  17:52                 0 Kly2.txt
               4 plik(ów)                  0 bajtów

 Katalog: D:\Filmy\Kły\Sezon2

2015-12-13  17:55    <DIR>          .
2015-12-13  17:55    <DIR>          ..
2015-12-13  17:54                 0 Kly10.mp4
2015-12-13  17:54                 0 Kly10.txt
2015-12-13  17:54                 0 Kly11.avi
               3 plik(ów)                  0 bajtów

     Razem wymienionych plików:
               9 plik(ów)                  0 bajtów
              14 katalog(ów)   2821976064 bajtów wolnych
"""

DataForTest_UNKNOWN = """2015-12-13  17:54                 0 Kly10.txt
2015-12-13  17:54                 0 Kly11.avi
               3 plik(ów)                  0 bajtów

     Razem wymienionych plików:
               9 plik(ów)                  0 bajtów
              14 katalog(ów)   2821976064 bajtów wolnych
"""

data = []
def writeDirectory_mock_(*args, **kwargs):
    data.append(args[0])

class TestParserFile(TestCase):
    open_ = mock_open()

    @patch('parsers.ParserBase._writeMovie', side_effect=writeDirectory_mock_)
    @patch('parsers.ParserBase._clearFile', return_value=None)
    def test_readDirectories_LS(self, mock1, mock2):

        mymock = mock_open(read_data=DataForTest_LS)
        mymock.return_value.__iter__ = lambda self: self
        mymock.return_value.__next__ = lambda self: self.readline()

        with patch('builtins.open', mymock):

            par = parserFile("","")
            self.assertEqual(par.readDirectories(),0)

        self.assertEqual(data[0],'./Epoka Lodowcowa/Epoka Lodowcowa.avi')
        self.assertEqual(data[1],'./Kły/Sezon1/Kly1.mp4')
        self.assertEqual(data[2],'./Kły/Sezon1/Kly2.avi')
        self.assertEqual(data[3],'./Kły/Sezon2/Kly10.mp4')
        self.assertEqual(data[4],'./Kły/Sezon2/Kly11.avi')

        data.clear()

    @patch('parsers.ParserBase._writeMovie', side_effect=writeDirectory_mock_)
    @patch('parsers.ParserBase._clearFile', return_value=None)
    def test_readDirectories_DIR(self, mock1, mock2):

        mymock = mock_open(read_data=DataForTest_DIR)
        mymock.return_value.__iter__ = lambda self: self
        mymock.return_value.__next__ = lambda self: self.readline()

        with patch('builtins.open', mymock):

            par = parserFile("","")
            self.assertEqual(par.readDirectories(),0)

            self.assertEqual(data[0],'./Epoka Lodowcowa/Epoka Lodowcowa.avi')
            self.assertEqual(data[1],'./Kły/Sezon1/Kly1.mp4')
            self.assertEqual(data[2],'./Kły/Sezon1/Kly2.avi')
            self.assertEqual(data[3],'./Kły/Sezon2/Kly10.mp4')
            self.assertEqual(data[4],'./Kły/Sezon2/Kly11.avi')

        data.clear()


    @patch('parsers.ParserBase._writeMovie', side_effect=writeDirectory_mock_)
    @patch('parsers.ParserBase._clearFile', return_value=None)
    def test_readDirectories_UNKNOWN(self, mock1, mock2):
        mymock = mock_open(read_data=DataForTest_UNKNOWN)
        mymock.return_value.__iter__ = lambda self: self
        mymock.return_value.__next__ = lambda self: self.readline()

        with patch('builtins.open', mymock):
            par = parserFile("","")
            self.assertEqual(par.readDirectories(),-1)

        data.clear()
