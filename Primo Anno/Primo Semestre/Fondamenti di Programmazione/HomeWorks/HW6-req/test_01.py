import os
import json
import testlib
from ddt import ddt, data, unpack

# change this variable to True to disable timeout and enable print
#DEBUG = True
DEBUG = False

TIMEOUT = 1 #* 2 # VM warp factor

import images


def get_input(input_json, key='input'):
    with open(input_json) as fr:
        js = json.load(fr)
        return js[key]

@ddt
class Test(testlib.TestCase):

    def do_test(self, file_json):
        if not os.path.exists('output'):
            os.makedirs('output')
        parameters = get_input(file_json)
        expected_img, len_snake = get_input(file_json, key='expected')
        if DEBUG:
            import program01 as program
            result = program.generate_snake(**parameters)
        else:
            with   self.ignored_function('builtins.print'), \
                   self.ignored_function('pprint.pprint'), \
                   self.forbidden_function('builtins.input'), \
                   self.forbidden_function('builtins.eval'), \
                   self.check_open({parameters['start_img']: 'rb',
                                    parameters['out_img']: 'bwb' }), \
                   self.check_imports(allowed=['program01', '_io','typing', 'images','encodings.utf_8']), \
                   self.timeout(TIMEOUT), \
                   self.timer(TIMEOUT):
                import program01 as program
                result = program.generate_snake(**parameters)
        self.assertEqual(result, len_snake,
                         f"\n{'*'*10} [ENG] The length of the snake is not {result} yet it is {len_snake} {'*'*10}\n"
                         f"{'*'*10} [ITA] La lunghezza dello snake non e' {result} ma e' {len_snake} {'*'*10}")
        out_img = parameters['out_img']
        self.check_img_file(out_img, expected_img)
        if os.path.exists(out_img):
            os.remove(out_img)
        return 1

    def test_intricacy(self):
        self.check_max_ciclomatic_complexity()

    def test_zz_top_types(self):
        self.should_skip('skipped during timing')
        from typeguard.importhook import install_import_hook
        try:
            import sys
            del sys.modules['program01']
        except:pass
        with install_import_hook('program01'):
            import program01
            params = get_input('./data/input_01.json')
            program01.generate_snake(**params)
            out_img = params['out_img']
            if os.path.exists(out_img):
                os.remove(out_img)

    def test_untampered_types(self):
        tipi = { 'generate_snake': {
                        'start_img': str, 
                        'position': list[int, int],
                        'commands': str, 
                        'out_img': str, 
                        'return': int} 
              }
        self.check_types_present(tipi)
            
    @data(
        ('./data/input_00.json',),
        ('./data/input_01.json',),
        ('./data/input_02.json',),
        ('./data/input_03.json',),
        ('./data/input_04.json',),
        ('./data/input_05.json',),
        ('./data/input_06.json',),
        ('./data/input_07.json',),
        ('./data/input_08.json',),
        ('./data/input_09.json',),
        ('./data/input_10.json',),
    )
    @unpack
    def test_data(self, file_json):
        return self.do_test(file_json)

    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()


