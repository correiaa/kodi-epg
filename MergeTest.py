import filecmp
import unittest

from Merge import Merge


class MyTestCase(unittest.TestCase):
    def test_merging_2_files(self):
        obj_under_test = Merge()
        obj_under_test.merge("file1", "file2")
        self.assertEquals(True, filecmp.cmp("file3", "output"))


if __name__ == '__main__':
    unittest.main()
