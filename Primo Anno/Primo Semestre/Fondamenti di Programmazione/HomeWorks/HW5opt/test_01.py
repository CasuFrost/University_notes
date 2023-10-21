import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

TIMEOUT=1.5 *4/3

@ddt
class Test(testlib.TestCase):

    def do_test(self, fimm, fout, expectedpng, expected):
        '''Test implementation:
            - fimm: textfile where posters are listed
            - fout: image filename to output
            - expectedpng: image filename with the expected image
            - expected: expected return value
            TIMEOUT: 1.5 seconds for each test
        '''
        if DEBUG:
                import program01 as program
                result = program.ex1(fimm, fout)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_open(allowed_filenames_modes={fimm: ['r'], fout:['wb'] }), \
                    self.check_imports(allowed=['program01',    '_io', 'encodings.utf_8','images','png',
                                                                '__future__','itertools','math','re','operator',
                                                                'struct','sys','warnings','zlib','array',
                                                                'functools','cpngfilters']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                import program01 as program
                result   = program.ex1(fimm,fout)
        self.assertEqual(type(result),  int,     "the expected return value has to be an integer")
        self.assertEqual(result,        expected, "the returned value is not the expected one")
        self.check_img_file(fout, expectedpng)
        return 1

    #   test_ID  expected
    @data(('1',   1080),
          ('2',    672),
          ('5',    478),
          ('25',  1928),
          ('45',  2384),
          ('65',  2414),
          ('85',  2130),
          ('105', 1926),
          ('125', 2192),
          ('145', 1864),
          ('165', 1836),
          ('185', 1636),
          ('sidebyside', 324),
          ('hidden', 1480),
          )
    @unpack
    def test_data(self, ID, expected):
        file_txt     = f"rectangles_{ID}.txt"
        file_png     = f"test_{ID}.png"
        expected_png = f"res_{ID}.png"
        return self.do_test(file_txt, file_png, expected_png, expected)

if __name__ == '__main__':
    Test.main()
