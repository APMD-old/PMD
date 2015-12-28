from unittest import TestCase
from mock import Mock, patch, mock_open
import builtins
from parsers import ParserDIR

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

data = []
def writeDirectory_mock_(*args, **kwargs):
    data.append(args[0])

class TestParserDIR(TestCase):
    open_ = mock_open()

    @patch('parsers.ParserDIR._writeMovie', side_effect=writeDirectory_mock_)
    @patch('parsers.ParserDIR._clearFile', return_value=None)
    def test_readDirectories(self, mock1, mock2):
        mymock = mock_open(read_data=DataForTest_DIR)
        mymock.return_value.__iter__ = lambda self: self
        mymock.return_value.__next__ = lambda self: self.readline()

        with patch('builtins.open', mymock):

            extensions = ("avi","mp4","mkv")
            parser = ParserDIR("","",extensions)
            parser.readDirectories()

            self.assertEqual(data[0],'./Epoka Lodowcowa/Epoka Lodowcowa.avi')
            self.assertEqual(data[1],'./Kły/Sezon1/Kly1.mp4')
            self.assertEqual(data[2],'./Kły/Sezon1/Kly2.avi')
            self.assertEqual(data[3],'./Kły/Sezon2/Kly10.mp4')
            self.assertEqual(data[4],'./Kły/Sezon2/Kly11.avi')
