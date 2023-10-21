import testlib
import random
from ddt import file_data, ddt, data, unpack

import program01 as program

@ddt
class Test(testlib.TestCase):

    def do_test(self, test_int_seq, test_subtotal, expected):
        """Test implementation
        - test_int_seq: input string
        - test_subtotal: input number
        - expected: expected output
        TIMEOUT: 1 second for each test
        """
        with    self.ignored_function('builtins.print'), \
                self.ignored_function('pprint.pprint'), \
                self.forbidden_function('builtins.input'), \
                self.timeout(1), \
                self.timer(1):
            result = program.ex1(test_int_seq, test_subtotal)
        self.assertEqual(type(result), int,
                         ('The output type should be: int\n'
                          '[Il tipo di dato in output deve essere: int]'))
        self.assertEqual(result, expected,
                         ('The return value is incorrect\n'
                          '[Il valore di ritorno è errato]'))
        return 1

    @file_data("test_01.json")
    def test_1_S1(self, test_int_seq, test_subtotal, expected):
        return self.do_test(test_int_seq, test_subtotal, expected)

    def test_many_zeros_1000(self):
        """Test with a string having 1000 0’s and
        250,000 sequences such that
        the sum of their values is equal to 2
        [Test con una stringa avente 1000 zeri e
         250.000 sequenze tali che
         la somma dei loro valori sia uguale a 2]"""
        test_seq_len  = 1000
        half          = test_seq_len // 2
        zeros         = ['0'] * (half-1)
        test_int_seq  = ",".join(zeros + ['1']*2 + zeros)
        test_subtotal = 2
        expected      = half ** 2
        return self.do_test(test_int_seq, test_subtotal, expected)

    def test_many_1s(self):
        """Test with a string having 20,000 1’s and
        19,001 sequences such that
        the sum of their values is equal to 1000
        [Test con una stringa avente 20,000 valori uguali a 1 e
         19.001 sequenze tali che
         la somma dei loro valori sia uguale a 1000]"""
        test_seq_len  = 20000
        test_int_seq  = ",".join(['1'] * test_seq_len)
        test_subtotal = 1000
        expected      = test_seq_len - test_subtotal + 1
        return self.do_test(test_int_seq, test_subtotal, expected)

    def test_many_internal_zeros(self):
        """Test with a string having 1,000 0’s and
        1 sequence such that
        the sum of its values is equal to 2
        [Test con una stringa avente 1000 zeri ed
         1 sequenza tale che
         la somma dei suoi valori sia uguale a 2]"""
        test_seq_len  = 1000
        zeros         = ['0'] * test_seq_len
        test_int_seq  = ",".join(['1'] + zeros + ['1'])
        test_subtotal = 2
        expected      = 1
        return self.do_test(test_int_seq, test_subtotal, expected)
    
if __name__ == '__main__':
    Test.main()


