import testlib
import random
from ddt import file_data, ddt, data, unpack

# change this variable to True to disable timeout and enable print
DEBUG=True
DEBUG=False

TIMEOUT=1# * 2 # VM warp factor

@ddt
class Test(testlib.TestCase):
    def do_test(self, starting_file, expected):
        """Test implementation
        - bases:		list of bases (integers > 1)
        - expected:		expected result
        TIMEOUT: 1 seconds for each test
        """
        if DEBUG:
                import program01 as program
                result = program.most_frequent_chars(starting_file)
        else:
            with    self.ignored_function('builtins.print'), \
                    self.ignored_function('pprint.pprint'), \
                    self.forbidden_function('builtins.input'), \
                    self.forbidden_function('builtins.eval'), \
                    self.check_imports(allowed=['program01','_io', 'typing', 'encodings.utf_8']), \
                    self.timeout(TIMEOUT), \
                    self.timer(TIMEOUT):
                import program01 as program
                result = program.most_frequent_chars(starting_file)
        self.assertEqual(len(result), len(expected), 
                         (f"The constructed string has different len ({len(result)}) from the expected one ({len(expected)})\n",
                          f"La stringa costruita ha lunghezza diversa ({len(result)}) rispetto a quella attesa ({len(expected)})"))
        self.assertEqual(result, expected, 
                         (f"The constructed string ({result}) differs from the expected one ({expected})\n",
                          f"La stringa costruita ({result}) non corrisponde a quella attesa ({expected})"))
        return 1

    def test_intricacy(self):
        self.check_max_ciclomatic_complexity()

    def test_zz_top_types(self):
        import sys
        from typeguard.importhook import install_import_hook
        from typeguard import typechecked
        @typechecked
        def mfc(starting_file : str) -> str:
            return program.most_frequent_chars(starting_file)
        try:
            del sys.modules['program01']
        except:pass
        with install_import_hook('program01'):
            import program01 as program
            starting_file = 'test01/A.txt'
            mfc(starting_file)

    def test_example(self):
        starting_file = 'test01/A.txt'
        expected = 'hareennt'
        return self.do_test(starting_file, expected)
    
    @data(
            ('test02/bullfight.txt', 'poternusakesness'),
            ('test03/woodchuck.txt', 'aanreeaseesable'),
            ('test04/pampers.txt', 'ceeelieessseds'),
            ('test05/avocados.txt','sereeieeesssssncy'),
            ('test06/strums.txt', 'sereeeeesssssssynssm'),
            ('test07/sinew.txt', 'すひびずじぞぜぃけそみきおょぇどべしこしこれれあねきゞ゜ぷ'),
            ('test08/boilings.txt', '🚏🏞😨♣☢🐸‼🗻🌚🥷🍯🎽♾🗽🍄⚔🫓😠🍈🪀🏞➡🍼👩😻📿🌁🕌👾🤓😚®❇💒🦪👒💂☪🥡🥕'),
            ('test09/meddles.txt', 'ᛢᚦᛝᛡᚤᚬᚬᛍᚸᛘᚣᚢᛜᛥᚳᛜᛖᛄᚢᛊᚬᛟᛈᛅᛞᚹᛯᚼᛁᚺ'),
            ('test10/aileron.txt', 'ᛠᚣᚻᛝᚧᛜ᛭くᚻᛝᚭᛈᚺᛦᚩᛞᛏᚽᛪᚢᚰᚯひᛃだᚯᚨろᚷᚦᛕᚸᛯᛄᛩᛂᚲᛆᛏᚰᛨぼゆᛇᛮᛚᚯᛓやᚼかᚯᚨᛦ᛫ᚩᚲᛋᚽ👘♒ぜ🕋ゔ🕣📬💊☺🦌'),
            ('test11/metonymies.txt', 'ᛃᚬᛝᚸᛈᚦᚱᛦᛢᛮᚼᛋᚯᛤᚳᛈᛓᚿᛊᚬᛈᚯᛎᚦᛅᛮᚧᚬᛦᚲᚮᚶᛑきᛓᛔᛮぞᛘᚼᛤᚩᛮᚼᛋᛛᛡᚱᛌᛑᚩᛪきᛤᛃᛅᛞᛏᛣᚤᚻᚦᚢᚩᛨᛐᛘゔᚷᚴᚧᚺᛖᛑᛨᛈがᛃᛥᚽᛚᚣᛋᚾᚳᚩごばᚩᚰぐがたᚨᚼᚩᛉ゜ᛅᚬᚲぅしᛪᚵᚨぎᛝᛡᛀごでᛟᚸゖそぇが🏟🃏じゔᚫぴ💌🔸😖ᛆᛪᚯ᛫ᚤᛑᚺᚾᛒᛦにぼ゙ぞゃせねねな'),
            ('test12/incipience.txt', 'sereeeeeesssssssりᚷᛈᚳᚽᚿᚪᛙᛪᛄᚩᚿᛨᚧᚮめわᛂᛆᛘᛤᛤᛜᛉᛈᚣのぽᚳᛅᚺᛊᛛᚪᚶᚡᛘᚷᚥᛑ᛬ᛋᚥᚩᚮᛏᛅᛎᚯᚱᚽしᚻᛔᚳᛇᚪᛅᚲᚪᛨᛒゐᚨᚰᚽᚩᚿつげᛊつᚢだᛇᚺᛯᚮりᚬᚴᚹよょぬおᚱᛮᛏᚹᛑᚮっᛋ🛢ᚲᛢ📲ぃᚭᛡゐぴ🆖🫒⏰👹🍹ᛅ⏏◀🛄👍🌽🔥🎅🆙🦒🦟🔤🚓😗😕ᛦᛃᛮᛈᛂ'),
            )
    @unpack
    def test_single(self, starting_file, expected):
        return self.do_test(starting_file, expected)

    ######################### SECRET TESTS START HERE! #########################


if __name__ == '__main__':
    Test.main()

