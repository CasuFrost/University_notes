import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

TIMEOUT=6 * 2 # VM warp factor

@ddt
class Test(testlib.TestCase):
    def do_test(self, list_of_xkcd : list[str], k : int, expected : list[int]):
        """Test implementation
        - list_of_xkcd:		list of xkcd formatted strings
        - k:			    how many maxima to return
        - expected:		    expected result
        TIMEOUT: 2 seconds for each test
        """
        tuple_of_xkcd = tuple(list_of_xkcd)
        if DEBUG:
                import program01 as program
                result = program.decode_XKCD_tuple(tuple_of_xkcd, k)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_imports(allowed=['program01','_io', 'typing']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.decode_XKCD_tuple(tuple_of_xkcd, k)
        for r in result:
            self.assertTrue(0<r<4000,
                          (f"All result numbers must be bigger than 0 and lower than 4000 (you got {r})\n"
                           f"Tutti i numeri ottenuti devono essere maggiori di 0 e minori di 4000 (hai ottenuto {r})"))
        self.assertEqual(len(result), k,
                         (f'The output list should have {k} elements\n'
                          f'La lista risultante deve avere {k} elementi'))
        self.assertSetEqual(set(result), set(expected), 
                         (f"The set of result numbers is different than the set of expected ones\n",
                          f"L'insieme dei numeri tornati nel risultato non corrisponde all'insieme dei valori attesi"))
        self.assertEqual(result, sorted(result, reverse=True),
                         (f"The result should be sorted by decreasing values\n",
                          f"Il risultato deve essere ordinato in ordine decrescente"))
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          'Il valore di ritorno è errato'))
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
            self.test_example1()

    @data (
            ("1101001000",           889),
            ("1000100100010100110", 1999),
            ("100010001050015" ,    2494),
            ("50010010050101015",    774)
             )
    @unpack
    def test_decode_value( self, xkcd : str, expected : int ):
        import program01 as program
        result = program.decode_value(xkcd)
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          'Il valore di ritorno è errato'))

    @data (
             # list of weights                  expected,    error
            ([1, 10, 100, 1000],                     889,    1111),
            ([1000, 100, 1000, 10, 100, 1, 10],     1999,    2221),
            ([1000, 1000, 10, 500, 1, 5] ,          2494,    2516),
            ([500, 100, 100, 50, 10, 10, 1, 5],      774,     776)
             )
    @unpack
    def test_list_of_weigths_to_number( self, integers : list[int], expected : int, error1 : int ):
        import program01 as program
        result = program.list_of_weights_to_number(integers)
        self.assertNotEqual(result, error1,
                            ("You did not subtract weights that are followed by heavier weights\n",
                             "Non hai sottratto i pesi che sono seguiti da pesi maggiori"))
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          'Il valore di ritorno è errato'))

    @data ( [1, 10, 100, 1000],
            [1000, 100, 1000, 10, 100, 1, 10], 
            [1000, 1000, 10, 500, 1, 5] ,     
            [500, 100, 100, 50, 10, 10, 1, 5],
             )
    def test_xkcd_to_list_of_weights(self, expected : list[int]):
        import program01 as program
        xkcd = ''.join(map(str,expected))
        result = program.xkcd_to_list_of_weights(xkcd)
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          'Il valore di ritorno è errato'))

    def test_example1(self):
        list_of_xkcd  = [ "1000100100010100110",  "100010001050015" , "50010010050101015"]
        k        = 2
        expected = [2494, 1999]
        return self.do_test(list_of_xkcd  , k, expected)

    def test_strange_numbers(self):
        list_of_xkcd  = [ "150",  "1050110" , "100100010100110", "11000", "1500", "10050010100110"]
        k        = 6
        expected = [999, 999, 499, 499, 49, 49,]
        return self.do_test(list_of_xkcd  , k, expected)


    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()


