import testlib
from ddt import ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG = True
DEBUG = False

TIMEOUT = 4 # * 2 # VM warp factor

@ddt
class Test(testlib.TestCase):

    def do_test(self, filename, expected = ()):
        filename

        if DEBUG:
            import program01 as program
            result = program.dumbothello(filename)
        else:
            with self.assertIsRecursive('program01') as program:
                   program.dumbothello(filename)
                   del program
            with   self.ignored_function('builtins.print'), \
                   self.ignored_function('pprint.pprint'), \
                   self.forbidden_function('builtins.input'), \
                   self.forbidden_function('builtins.eval'), \
                   self.check_open(allowed={filename: 'rt'}), \
                   self.check_imports(allowed=['program01', '_io','typing', 'tree','encodings.utf_8']), \
                   self.timeout(TIMEOUT), \
                   self.timer(TIMEOUT):
                import program01 as program
                result = program.dumbothello(filename)
        self.assertEqual(result, expected,
                         f"\n{'*'*10} [ENG] The output result {result} is not the expected {expected} {'*'*10}\n"
                         f"{'*'*10} [ITA] Il risultato {result} non è quello atteso {expected} {'*'*10}")
        return 1

    def test_intricacy(self):
        self.check_max_ciclomatic_complexity()

    def test_zz_top_types(self):
        from typeguard.importhook import install_import_hook
        try:
            import sys
            del sys.modules['program01']
        except:pass
        with install_import_hook('program01'):
            import program01
            program01.dumbothello('boards/01.txt')

    def test_untampered_types(self):
        tipi = { 'dumbothello': {
                        'filename': str, 
                        'return': tuple[int,int,int]} 
              }
        self.check_types_present(tipi)


    @data(
        ('boards/01.txt', (2, 16, 0)),
        ('boards/02.txt', (78, 2, 16)),
        ('boards/03.txt', (1574, 2700, 1926)),
        ('boards/04.txt', (1538, 2292, 1502)),
        ('boards/05.txt', (70, 48, 0)),
        ('boards/06.txt', (190, 274, 104)),
        ('boards/07.txt', (60, 25, 13)),
        ('boards/08.txt', (2742, 1204, 794)),
        ('boards/09.txt', (0, 16, 15))
    )
    @unpack
    def test_data(self, testn, expected):
            return self.do_test(testn, expected)

    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()


