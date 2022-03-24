import unittest

from ddt import ddt,file_data


@ddt
class ReadFileData(unittest.TestCase):

    @file_data('yaml01.yaml')
    def test_01_read_file_data(self,username,password):
        print(username)

    @file_data('yaml01.yaml')
    def test_02_read_file_data(self, *args, **kwargs):
        print(kwargs)

if __name__ == '__main__':
    unittest.main()