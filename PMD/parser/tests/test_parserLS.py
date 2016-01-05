from unittest import TestCase
from parsers import ParserLS

DataForTest_LS=""".:
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

class TestParserLS(TestCase):
    def test_readDirectories(self):
        extensions = ("avi","mp4","mkv")
        parser = ParserLS(DataForTest_LS,extensions)
        data = parser.readDirectories()

        self.assertEqual(data[0],'./Epoka Lodowcowa/Epoka Lodowcowa.avi')
        self.assertEqual(data[1],'./Kły/Sezon1/Kly1.mp4')
        self.assertEqual(data[2],'./Kły/Sezon1/Kly2.avi')
        self.assertEqual(data[3],'./Kły/Sezon2/Kly10.mp4')
        self.assertEqual(data[4],'./Kły/Sezon2/Kly11.avi')
