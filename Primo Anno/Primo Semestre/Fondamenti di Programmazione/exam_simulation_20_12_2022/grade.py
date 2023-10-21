# -*- coding: utf-8 -*-
import testlib
import isrecursive
import os
import sys

if not os.path.isfile('program.py'):
    print('WARNING: Save program.empty.py as program.py\n'
          'ATTENZIONE: salvare program.vuoto.py con nome program.py')
    sys.exit(0)
import program

################################################################################
# ------- THE SOURCE CODE FROM THIS POINT FORWARD IS FOR TESTING ONLY -------- #
# ----- The use of the following functions in your program is forbidden ------ #
# ---------------------------------------------------------------------------- #
# --- IL CODICE SORGENTE DI SEGUITO È ESCLUSIVAMENTE PER EFFETTUARE I TEST --- #
# ------- L'uso delle funzioni seguenti nel vostro programma è vietato --------#
################################################################################

#### Use DEBUG=True to disable the recursion tests and enable the
#### stack trace: each error will produce a more verbose output
####
#### Mettete DEBUG=True per disattivare i test di ricorsione  e
#### fare debug delle funzioni più facilmente attivando stack trace
#DEBUG = True
DEBUG = False
#############################################################################

COL = {'RED': '\u001b[31m',
       'RST': '\u001b[0m',
       'GREEN': '\u001b[32m',
       'YELLOW' : '\u001b[33m'}


def error_message(res, expected, msg=None):
    msg_std = f"Valore NON corretto! [NOT OK]\n TUO RISULTATO = {res} \n ma e' ATTESO = {expected}"
    if msg is None:
        msg = msg_std
    else:
        msg = msg + msg_std
    print('*'*50)
    print(msg)

def test_personal_data_entry():
    if 'name' in program.__dict__:
        assert program.name       != 'NAME', f"{COL['YELLOW']}ERROR: Please assign the 'name' variable with YOUR NAME in program.py{COL['RST']}"
        assert program.surname    != 'SURNAME', f"{COL['YELLOW']}ERROR: Please assign the 'surname' variable with YOUR SURNAME in program.py{COL['RST']}"
        assert program.student_id != 'MATRICULATION NUMBER', f"{COL['YELLOW']}ERROR: Please assign the 'student_id' variable with YOUR MATRICULATION NUMBER in program.py{COL['RST']}"
    else:
        assert program.nome      != 'NOME', f"{COL['YELLOW']}ERRORE: Indica il tuo NOME in program.py{COL['RST']}"
        assert program.cognome   != 'COGNOME', f"{COL['YELLOW']}ERRORE: Indica il tuo COGNOME in program.py{COL['RST']}"
        assert program.matricola != 'MATRICOLA', f"{COL['YELLOW']}ERRORE: Indica il tuo NUMERO DI MATRICOLA in program.py{COL['RST']}"
    return 0

###############################################################################

def do_func1_tests(string_list, expected):
    res = program.func1(string_list)

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The expected list is {expected} instead of {res}.\n''')
        return 0
    return 2/3


def test_func1_1():
    '''
    ['Home', 'dog', 'HASSe','Zar']
    '''
    string_list = ['Home', 'dog', 'HASSe','Zar']
    expected = ['Zar', 'Home', 'HASSe']
    return do_func1_tests(string_list, expected)

def test_func1_2():
    '''
    'The Beatles were an English rock band, formed in Liverpool in 1960, that comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr.'
    '''
    string_list = 'The Beatles were an English rock band, formed in Liverpool in 1960, that comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr.'.split()
    expected = ['The', 'John', 'Paul', 'Ringo', 'George', 'Starr.', 'Beatles', 'English', 'Lennon,', 'Harrison', 'Liverpool', 'McCartney,']
    return do_func1_tests(string_list, expected)

def test_func1_3():
    '''
    'Harry and Meghan: Seven takeaways from their Netflix series'
    '''
    string_list = 'Harry and Meghan: Seven takeaways from their Netflix series'.split()
    expected = ['Harry', 'Seven', 'Meghan:', 'Netflix']
    return do_func1_tests(string_list, expected)

def do_func2_tests(pathname, expected):
    res = program.func2(pathname)

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The expected dictionary is {expected} instead of {res}.\n''')
        return 0
    return 2/3


def test_func2_1():
    '''
    animals.txt
    '''
    pathname = 'animals.txt'
    expected = {'cat': {'meaow', 'purr'}, 'dog': {'woof'}}
    return do_func2_tests(pathname, expected)

def test_func2_2():
    '''
    beatles.txt
    '''
    pathname = 'beatles.txt'
    expected = {'ringo': {'starr'}, 'John': {'Lennon'}, 'Paul': {'McCartney'}, 'George': {'Harrison'}, 'Ringo': {'Starr'}}
    return do_func2_tests(pathname, expected)

def test_func2_3():
    '''
    numbers.txt
    '''
    pathname = 'numbers.txt'
    expected = {'1': {'654', '54'}, '2': {'65', '54'}, '3': {'-3', '54545'}, '4': {'64'}, '0': {'4343'}}
    return do_func2_tests(pathname, expected)

def do_func3_tests(listA, listB, listC, expected, outpath):
    actual_out_path = outpath.replace('!!TMP!!', 'out')
    # before running anything remove if any
    if os.path.exists(actual_out_path):
        os.remove(actual_out_path)
        
    res = program.func3(listA, listB, listC, actual_out_path)

    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The expected list is {expected} instead of {res}.\n''')
        return 0

    
    if os.path.isfile(actual_out_path):
        try:
            testlib.check_text_file(actual_out_path,
                                    outpath.replace('!!TMP!!', 'exp'))
        except: 
            print("Output file differs!", end=' ')
            return 0
        else:         
            print("Output file matches", end=' ') # all goodwe proceed
    else:
        print(f"I cannot find the output file in {actual_out_path}", end=' ')
        return 0

    return 2/3


def test_func3_1():
    '''
    [4, 1, 3, 5, 2]
    [5, 1, 1, 2, 3]
    [10, 5, 9, 9, 6]
    '''
    lists = [[4, 1, 3, 5, 2],
    [5, 1, 1, 2, 3],
    [10, 5, 9, 9, 6]]
    expected = 90
    return do_func3_tests(*lists, expected, 'func3_1_!!TMP!!.txt')

def test_func3_2():
    '''
    [-3, -6, -6, -9, -1]
    [1, -5, 9, -3, -2]
    [6, 7, 10, -7, -2]
    '''
    lists = [[-3, -6, -6, -9, -1],
    [1, -5, 9, -3, -2],
    [6, 7, 10, -7, -2]]
    expected = 84
    return do_func3_tests(*lists, expected, 'func3_2_!!TMP!!.txt')

def test_func3_3():
    '''
    [-13, 33, -83, 25, -68]
    [36, -7, 92, -29, 3]
    [83, 14, -59, -66, -11]
    '''
    lists = [[-13, 33, -83, 25, -68],
    [36, -7, 92, -29, 3],
    [83, 14, -59, -66, -11]]
    expected = 1909
    return do_func3_tests(*lists, expected, 'func3_3_!!TMP!!.txt')

# ----------------------------------- EX.1 ----------------------------------- #

def do_func4_tests(triangles, expected):
    val = len(triangles) - len(expected)
    res = program.func4(triangles)

    testlib.check(type(res), type(val), None, f"Wrong return type! Returned={type(res)}, expected={type(expected)}")

    if triangles != expected:
        print(f'''{'*'*50}\n[ERROR] The list triangles should be modified in {expected} instead of {triangles}.\n'''
              f'''[ERROR] La lista triangles dovrebbe essere modificata in {expected} invece che {triangles}.\n{'*'*50}''')
        return 0
    if res != val:
        print(f'''{'*'*50}\n[ERROR] The expected removed element be {expected} instead of {triangles}.\n'''
              f'''[ERROR] In numero di elementi rimosse deve essere {expected} invece che {triangles}.\n{'*'*50}''')
        return 0
    return 2


def test_func4_1():
    '''
    triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = [(3, 4, 5), (12, 36.05551, 34)]
    '''
    triangles = [(3, 4, 5), (12, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = [(3, 4, 5), (12, 36.05551, 34)]
    return do_func4_tests(triangles, expected)

def test_func4_2():
    '''
    triangles = [(3, 4, 6), (11, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = []
    '''
    triangles = [(3, 4, 6), (11, 36.05551, 34), (1,1,3), (8,8,8), (2, 3, 4)]
    expected = []
    return do_func4_tests(triangles, expected)

def test_func4_3():
    '''
    triangles = [(6.0208, 4.0, 4.5),
             (5.5, 8.74586, 6.8),
             (12.8, 10.2, 16.3704),
             (2.3, 8.51645, 8.2),
             (7.9, 10.29417, 6),
             (12.5873, 8.8, 9.0)]
    expected = [(6.0208, 4.0, 4.5), (5.5, 8.74586, 6.8), (2.3, 8.51645, 8.2), (12.5873, 8.8, 9.0)]
    '''
    triangles = [(6.0208, 4.0, 4.5),
             (5.5, 8.74586, 6.8),
             (12.8, 10.2, 16.3704),
             (2.3, 8.51645, 8.2),
             (7.9, 10.29417, 6),
             (12.5873, 8.8, 9.0)]
    expected = [(6.0208, 4.0, 4.5), (5.5, 8.74586, 6.8), (2.3, 8.51645, 8.2), (12.5873, 8.8, 9.0)]
    return do_func4_tests(triangles, expected)

import images

def do_test_func5(ID, expected):
    img_in  = f'func5/image0{ID}.png'
    img_out = f'func5_your_image0{ID}.png'
    img_exp = f'func5/expected0{ID}.png'
    # remove the previous image each time if it is there
    if os.path.exists(img_out):
        os.remove(img_out)
    # now run

    res = program.func5(images.load(img_in), img_out)
    if res != expected:
        print(f'''{'*'*50}\n[ERROR] The number of rectangle should be {expected} instead of {res}.\n'''
              f'''[ERROR] Il numero di rettangoli deve essere {expected} invece che {res}.\n{'*'*50}''')
        return 0
    testlib.check_img_file(img_out, img_exp)
    return 2


def test_func5_1():
    '''imm_in = func5/image01.png
    imm_out = func5/expected01.png
    expected = (0, 0, 0)
    '''
    ID = 1
    expected = (0, 0, 0)
    return do_test_func5(ID, expected)


def test_func5_2():
    '''imm_in = func5/image01.png
    imm_out = func5/expected01.png
    expected = 3
    '''
    ID = 2
    expected = (0, 0, 0)
    return do_test_func5(ID, expected)


def test_func5_3():
    '''imm_in = func5/image01.png
    imm_out = func5/expected01.png
    expected = 3
    '''
    ID = 3
    expected = (0, 0, 0)
    return do_test_func5(ID, expected)
# ----------------------------------- EX.1 ----------------------------------- #
def do_test_ex1(directory, namefile, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex1(directory, namefile)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex1(directory, namefile)
    testlib.check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
    return 2

def test_ex1_1():
    '''directory = 'ex3/A'
    filename = 'a.txt'
    expected = [22, 100, 90]
    '''
    directory = 'ex3/A'
    filename = 'a.txt'
    expected = [22, 100, 90]
    return do_test_ex1(directory, filename, expected)


def test_ex1_2():
    '''directory = 'ex3/B'
    filename = 'b.txt'
    expected = [33, 69, 270]
    '''
    directory = 'ex3/B'
    filename = 'b.txt'
    expected = [33, 69, 270]
    return do_test_ex1(directory, filename, expected)


def test_ex1_3():
    '''directory = 'ex3/C'
    filename = 'a.txt'
    expected = [23, 728, 490, 335, 11111]
    '''
    directory = 'ex3/C'
    filename = 'a.txt'
    expected = [23, 728, 490, 335, 11111]
    return 1 + do_test_ex1(directory, filename, expected)
# ----------------------------------- EX. 2----------------------------------- #


def do_ex2_test(strings, n, expected):
    if not DEBUG:
        try:
            isrecursive.decorate_module(program)
            program.ex2(strings, n)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("The program does not employ recursion / Il programma non adotta un approccio ricorsivo")
        finally:
            isrecursive.undecorate_module(program)

    res = program.ex2(strings, n)
    if not isinstance(res, (list, set)):
        testlib.check(type(res), set, None, f"Wrong return type! Returned={type(res)}, expected=list or set")
    p=0
    if type(res) == list:
        testlib.check(res, expected, None, f"Wrong list! Returned={res}, expected={expected}")
        print("Correct list returned", end=' ')
        p=2
    elif type(res) == set:
        testlib.check(res, set(expected), None, f"Wrong set! Returned={res}, expected={expected}")
        print("Correct set returned", end=' ')
        p=1
    return p

def test_ex2_1():
    '''
    strings = {'a','b','c','de'}
    n = 2
    expected = ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    '''
    strings = {'a','b','c','de'}
    n = 2
    expected = ['ade', 'bde', 'cde', 'dea', 'deb', 'dec', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    return do_ex2_test(strings, n, expected)

def test_ex2_2():
    '''
    strings = {'p', 'ro', 'gra', 'mmin', 'Python'}
    n = 3
    expected = ['Pythongrammin', 'Pythonmmingra', 'graPythonmmin', 'gramminPython', 'mminPythongra', 'mmingraPython', 'Pythonmminro', 'Pythonrommin', 'mminPythonro', 'mminroPython', 'roPythonmmin', 'romminPython', 'Pythongraro', 'Pythonmminp', 'Pythonpmmin', 'Pythonrogra', 'graPythonro', 'graroPython', 'mminPythonp', 'mminpPython', 'pPythonmmin', 'pmminPython', 'roPythongra', 'rograPython', 'Pythongrap', 'Pythonpgra', 'graPythonp', 'grapPython', 'pPythongra', 'pgraPython', 'Pythonpro', 'Pythonrop', 'gramminro', 'grarommin', 'mmingraro', 'mminrogra', 'pPythonro', 'proPython', 'roPythonp', 'rogrammin', 'rommingra', 'ropPython', 'gramminp', 'grapmmin', 'mmingrap', 'mminpgra', 'pgrammin', 'pmmingra', 'mminpro', 'mminrop', 'pmminro', 'prommin', 'romminp', 'ropmmin', 'grapro', 'grarop', 'pgraro', 'progra', 'rograp', 'ropgra']
    '''
    strings =  {'p', 'ro', 'gra', 'mmin', 'Python'}
    n = 3
    expected = ['Pythongrammin', 'Pythonmmingra', 'graPythonmmin', 'gramminPython', 'mminPythongra', 'mmingraPython', 'Pythonmminro', 'Pythonrommin', 'mminPythonro', 'mminroPython', 'roPythonmmin', 'romminPython', 'Pythongraro', 'Pythonmminp', 'Pythonpmmin', 'Pythonrogra', 'graPythonro', 'graroPython', 'mminPythonp', 'mminpPython', 'pPythonmmin', 'pmminPython', 'roPythongra', 'rograPython', 'Pythongrap', 'Pythonpgra', 'graPythonp', 'grapPython', 'pPythongra', 'pgraPython', 'Pythonpro', 'Pythonrop', 'gramminro', 'grarommin', 'mmingraro', 'mminrogra', 'pPythonro', 'proPython', 'roPythonp', 'rogrammin', 'rommingra', 'ropPython', 'gramminp', 'grapmmin', 'mmingrap', 'mminpgra', 'pgrammin', 'pmmingra', 'mminpro', 'mminrop', 'pmminro', 'prommin', 'romminp', 'ropmmin', 'grapro', 'grarop', 'pgraro', 'progra', 'rograp', 'ropgra']
    return do_ex2_test(strings, n, expected)

def test_ex2_3():
    '''
    strings = {'bim','bum','ba','le','giu'}
    n = 5
    expected = ['babimbumgiule', 'babimbumlegiu', 'babimgiubumle', 'babimgiulebum', 'babimlebumgiu', 'babimlegiubum', 'babumbimgiule', 'babumbimlegiu', 'babumgiubimle', 'babumgiulebim', 'babumlebimgiu', 'babumlegiubim', 'bagiubimbumle', 'bagiubimlebum', 'bagiubumbimle', 'bagiubumlebim', 'bagiulebimbum', 'bagiulebumbim', 'balebimbumgiu', 'balebimgiubum', 'balebumbimgiu', 'balebumgiubim', 'balegiubimbum', 'balegiubumbim', 'bimbabumgiule', 'bimbabumlegiu', 'bimbagiubumle', 'bimbagiulebum', 'bimbalebumgiu', 'bimbalegiubum', 'bimbumbagiule', 'bimbumbalegiu', 'bimbumgiubale', 'bimbumgiuleba', 'bimbumlebagiu', 'bimbumlegiuba', 'bimgiubabumle', 'bimgiubalebum', 'bimgiubumbale', 'bimgiubumleba', 'bimgiulebabum', 'bimgiulebumba', 'bimlebabumgiu', 'bimlebagiubum', 'bimlebumbagiu', 'bimlebumgiuba', 'bimlegiubabum', 'bimlegiubumba', 'bumbabimgiule', 'bumbabimlegiu', 'bumbagiubimle', 'bumbagiulebim', 'bumbalebimgiu', 'bumbalegiubim', 'bumbimbagiule', 'bumbimbalegiu', 'bumbimgiubale', 'bumbimgiuleba', 'bumbimlebagiu', 'bumbimlegiuba', 'bumgiubabimle', 'bumgiubalebim', 'bumgiubimbale', 'bumgiubimleba', 'bumgiulebabim', 'bumgiulebimba', 'bumlebabimgiu', 'bumlebagiubim', 'bumlebimbagiu', 'bumlebimgiuba', 'bumlegiubabim', 'bumlegiubimba', 'giubabimbumle', 'giubabimlebum', 'giubabumbimle', 'giubabumlebim', 'giubalebimbum', 'giubalebumbim', 'giubimbabumle', 'giubimbalebum', 'giubimbumbale', 'giubimbumleba', 'giubimlebabum', 'giubimlebumba', 'giubumbabimle', 'giubumbalebim', 'giubumbimbale', 'giubumbimleba', 'giubumlebabim', 'giubumlebimba', 'giulebabimbum', 'giulebabumbim', 'giulebimbabum', 'giulebimbumba', 'giulebumbabim', 'giulebumbimba', 'lebabimbumgiu', 'lebabimgiubum', 'lebabumbimgiu', 'lebabumgiubim', 'lebagiubimbum', 'lebagiubumbim', 'lebimbabumgiu', 'lebimbagiubum', 'lebimbumbagiu', 'lebimbumgiuba', 'lebimgiubabum', 'lebimgiubumba', 'lebumbabimgiu', 'lebumbagiubim', 'lebumbimbagiu', 'lebumbimgiuba', 'lebumgiubabim', 'lebumgiubimba', 'legiubabimbum', 'legiubabumbim', 'legiubimbabum', 'legiubimbumba', 'legiubumbabim', 'legiubumbimba']
    '''
    strings = {'bim','bum','ba','le','giu'}
    n = 5
    expected = ['babimbumgiule', 'babimbumlegiu', 'babimgiubumle', 'babimgiulebum', 'babimlebumgiu', 'babimlegiubum', 'babumbimgiule', 'babumbimlegiu', 'babumgiubimle', 'babumgiulebim', 'babumlebimgiu', 'babumlegiubim', 'bagiubimbumle', 'bagiubimlebum', 'bagiubumbimle', 'bagiubumlebim', 'bagiulebimbum', 'bagiulebumbim', 'balebimbumgiu', 'balebimgiubum', 'balebumbimgiu', 'balebumgiubim', 'balegiubimbum', 'balegiubumbim', 'bimbabumgiule', 'bimbabumlegiu', 'bimbagiubumle', 'bimbagiulebum', 'bimbalebumgiu', 'bimbalegiubum', 'bimbumbagiule', 'bimbumbalegiu', 'bimbumgiubale', 'bimbumgiuleba', 'bimbumlebagiu', 'bimbumlegiuba', 'bimgiubabumle', 'bimgiubalebum', 'bimgiubumbale', 'bimgiubumleba', 'bimgiulebabum', 'bimgiulebumba', 'bimlebabumgiu', 'bimlebagiubum', 'bimlebumbagiu', 'bimlebumgiuba', 'bimlegiubabum', 'bimlegiubumba', 'bumbabimgiule', 'bumbabimlegiu', 'bumbagiubimle', 'bumbagiulebim', 'bumbalebimgiu', 'bumbalegiubim', 'bumbimbagiule', 'bumbimbalegiu', 'bumbimgiubale', 'bumbimgiuleba', 'bumbimlebagiu', 'bumbimlegiuba', 'bumgiubabimle', 'bumgiubalebim', 'bumgiubimbale', 'bumgiubimleba', 'bumgiulebabim', 'bumgiulebimba', 'bumlebabimgiu', 'bumlebagiubim', 'bumlebimbagiu', 'bumlebimgiuba', 'bumlegiubabim', 'bumlegiubimba', 'giubabimbumle', 'giubabimlebum', 'giubabumbimle', 'giubabumlebim', 'giubalebimbum', 'giubalebumbim', 'giubimbabumle', 'giubimbalebum', 'giubimbumbale', 'giubimbumleba', 'giubimlebabum', 'giubimlebumba', 'giubumbabimle', 'giubumbalebim', 'giubumbimbale', 'giubumbimleba', 'giubumlebabim', 'giubumlebimba', 'giulebabimbum', 'giulebabumbim', 'giulebimbabum', 'giulebimbumba', 'giulebumbabim', 'giulebumbimba', 'lebabimbumgiu', 'lebabimgiubum', 'lebabumbimgiu', 'lebabumgiubim', 'lebagiubimbum', 'lebagiubumbim', 'lebimbabumgiu', 'lebimbagiubum', 'lebimbumbagiu', 'lebimbumgiuba', 'lebimgiubabum', 'lebimgiubumba', 'lebumbabimgiu', 'lebumbagiubim', 'lebumbimbagiu', 'lebumbimgiuba', 'lebumgiubabim', 'lebumgiubimba', 'legiubabimbum', 'legiubabumbim', 'legiubimbabum', 'legiubimbumba', 'legiubumbabim', 'legiubumbimba']
    return 1 + do_ex2_test(strings, n, expected)


################################################################################

tests = [
    # TO RUN ONLY SOME OF THE TESTS, comment any of the following entries
    # PER DISATTIVARE ALCUNI TEST, commentare gli elementi seguenti
    test_func1_1, test_func1_2, test_func1_3,
    test_func2_1, test_func2_2, test_func2_3,
    test_func3_1, test_func3_2, test_func3_3,
    test_func4_1, test_func4_2, test_func4_3,
    test_func5_1, test_func5_2, test_func5_3,
    test_ex1_1,  test_ex1_2, test_ex1_3,
    test_ex2_1,  test_ex2_2, test_ex2_3,
    test_personal_data_entry,
]


if __name__ == '__main__':
    testlib.runtests(tests,
                     verbose=True,
                     logfile='grade.csv',
                     stack_trace=DEBUG)
    grades = {}
    total  = 0
    with open('grade.csv') as F:
        for line in F:
            test, points = line.split(',')
            _, name, *_ = test.split('_')
            if name == 'personal': continue
            total += float(points)
            grades[name] = grades.get(name, 0) + float(points)
    #%% Constraint for the exam
    constraint1 = len([name for name,grade in grades.items() if grade>0 and name.startswith('func')]) >= 3
    constraint2 = len([name for name,grade in grades.items() if grade>0 and name.startswith('ex')]) >= 1
    constraint3 = total >= 18
    constraint4 = all((constraint1, constraint2, constraint3))
    if not constraint1:
        print(f'YOU HAVE NOT PASSED AT LEAST 3 FUNC EXERCISES: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint2:
        print(f'YOU HAVE NOT PASSED AT LEAST 1 RECURSIVE EXERCISE: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    elif not constraint3:
        print(f'THE FINAL GRADE IS LESS THAN 18: {COL["RED"]}EXAM NOT PASSED{COL["RST"]}')
    else:
        print(f"YOU HAVE {COL['GREEN']}PASSED{COL['RST']} THE EXAM WITH {COL['GREEN']}{total}{COL['RST']} POINTS")
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    print(f"Three func problems solved:  {BOLD} {COL['GREEN'] if constraint1 else COL['RED']} {constraint1}{COL['RST']}{ENDC}")
    print(f"One ex problem solved:       {BOLD} {COL['GREEN'] if constraint2 else COL['RED']} {constraint2}{COL['RST']} ")
    print(f"Total > 18:                  {BOLD} {COL['GREEN'] if constraint3 else COL['RED']} {constraint3}{COL['RST']}{ENDC}")
    print(f"Exam passed:                 {BOLD} {COL['GREEN'] if constraint4 else COL['RED']} {constraint4}{COL['RST']}{ENDC}")
################################################################################
