# -*- coding: utf-8 -*-
import copy

evaluation_tests = {
    'cubo':   [
        [(4, ),   (7, ),  (3, ), ],
        [64,    343,    27, ]
    ],
    'int_to_str_flt':   [
        [(4, ),   (-7, ),  (3, ),  (-10, ),  (-109, ), ],
        ['4',    7.,    '3',    10.,     109.]
    ],
    'int_to_str':   [
        [(4, ),   (7, ),  (3, ),  (10, ),  (109, ), ],
        ['4',    '7',    '3',    '10',     '109']
    ],
    'num_digits':   [
        [(5, ),   (7, ),  (0, ),  (10, ),  (22, ),  (67, ),
         (99, ),  (77, ),  (1000, ),  (10000, ),  (999999, )],
        [1,    1,    1,    2,     2,     2,
         2,     2,     4,       5,       6]
    ],
    'num_digits_neg':   [
        [(5, ),   (-7, ),  (0, ),  (-10, ),  (-22, ),
         (67, ),  (99, ),  (77, ),  (1000, ),
         (10000, ),  (-999999, )],
        [1,    1,    1,    2,     2,     2,
         2,     2,     4,       5,       6]
    ],
    'num_digits_neg_str':   [
        [("5", ),   ("07", ),  ("0", ),  ("-00010", ),
         ("-22", ),  ("0000067", ),  ("99", ),
         ("00077", ),  ("1000", )],
        [1,    1,    1,    2,     2,
         2,     2,     2,     4, ]
    ],
    'num_digits_neg_str_mix':  [
        [("5", ),   ("-07", ),  (0, ),
         ("-00010", ),  (-22, ),  ("0000067", ),
         ("99", ),  ("00077", ),  (-1000, )],
        [1,    1,    1,    2,     2,
         2,     2,     2,     4, ]
    ],
    'check_int_str': [
        [('pippo', 1), ('pippo2', 2), ('p1pp0', 0),
         ('p1pp0', 0), ('p1pp1', 1), ('-1-1-1-1', -1),
         ('sup3rcalifragilistic3ppalippa', 3),
         ('2121211212121121', 2)],
        [0, 1, 1, 1, 2, 4, 2, 7]
    ],
    'check_S_in_T': [
        [('42130', 'dc6486c479e84c94efce'), ('42130', '4bea7169ef7d4c80b6da'),
         ('42130', '07d35d393fc7158e18b8'),
         ('42130', 'd8f9979694329a71ceed'), ('42130', 'ee86b4cde9f97afec197'),
         ('42130', 'ad3b13c5d12b09e8a0a9'),
         ('42130', '965f00f213ce06143a52'),
         ('42130', '801f35bde2af0ad54972'), ('42130', '769845d480b5043f545f'),
         ('30216', 'a9b66a0353a6e966b6a0'), ],
        [[4, 0, 0, 0, 0], [2, 0, 1, 0, 1], [0, 0, 2, 3, 1], [1, 1, 1, 1, 0],
         [1, 0, 1, 0, 0], [0, 1, 2, 2, 2], [1, 2, 2, 2, 3], [1, 2, 1, 1, 2],
         [4, 0, 0, 1, 2], [2, 2, 0, 0, 6], ]
    ],

    'count_sub_string': [
        [('z', 'abcdefgabcda'), ('a', 'abcdefgabcda'), ('abc', 'abcdefgabcd'),
         ('pippo', 'pipppippopipipipipippppppippo'),
         ('ape', 'aperitivoapeapeapeape'), ('$', '$$$$$$$$ $'),
         ('$$', '$$$$$$$$ $'), ('pap', 'papapapapapapapapapap'),
         ('xxxxxx', 'xx')],
        [0, 3, 2, 2, 5, 9, 7, 10, 0]
    ],
    'count_sub_string_idx': [
        [('z', 'abcdefgabcda'), ('a', 'abcdefgabcda'),
         ('abc', 'abcdefgabcd'), ('pippo', 'pipppippopipipipipippppppippo'),
         ('ape', 'aperitivoapeapeapeape'), ('$', '$$$$$$$$ $'),
         ('$$', '$$$$$$$$ $'), ('pap', 'papapapapapapapapapap'),
         ('xxxxxx', 'xx')],
        [[], [(0, 0), (7, 7), (11, 11)], [(0, 2), (7, 9)],
         [(4, 8), (24, 28)], [(0, 2), (9, 11), (12, 14), (15, 17), (18, 20)],
         [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (9, 9)], [
             (0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)],
         [(0, 2), (2, 4), (4, 6), (6, 8), (8, 10), (10, 12), (12, 14), (14, 16), (16, 18), (18, 20)], []]
    ],
    'check_reverse': [
        [('oppip', 'pippo'), ('opppp', 'pippo'), ('ppip', 'pippo'),
         ('pippo', 'oppip'), ('AzAz', 'zAzA'), ('**', '**'), ('oTTag', 'gatto')],
        [True, False, False,
         True, True, True, False],
    ],
    'sum_max_min': [
        [([1, 2, 3],), ([3, 2, 1],), ([-1, -2, 3],), ],
        [(6, 3, 1), (6, 3, 1), (0, 3, -2)],
    ],
    'sum_positive': [[([10, 5, -5, -20, -30, -1, 20],), 
                      ([-1, 3, -4, 5, -7, 31],)],
                     [35, 39],],
    'sum_multipli': [[([10, 5, -5, -20, -30, -1, 20],), ],
                     [35]],
    'list_multipli': [
        [([10, 5, -5, -20, -30, -1, 20],),
         ([-11, -9, 9, -26, 15, -48, 29, -6, -42, 13, 49, 13, -31, 44, 41, 16, 23, -11, 1, -31],),
         ([-22, -5, 31, -9, 37, -4, 41, 46, 24, -35,
           18, -28, 15, 34, -36, 10, -27, 42, -9, -2],),
         ([-28, 18, -36, -9, 4, -44, -44, 27, 47, 19,
           5, -35, -39, -30, 6, 33, 11, -16, -13, -19],),
         ([13, 37, 26, 22, -40, 41, 35, 19, 46, 3, 46,
           23, 3, -22, -46, -36, 26, -17, -50, 35],),
         ([-50, 4, 23, -45, -4, -37, 30, 16, 49, 7, -13, -4, -15, -34, 46, 34, -7, 10, 38, -7],), ],
        [[10, -20, -30, 20, 10, 5, -5, -20, -30, 20], [-26, -48, -6, -42, 44, 16, 15],
         [-22, -4, 46, 24, 18, -28, 34, -36, 10, 42, -2, -5, -35, 15, 10],
         [-28, 18, -36, 4, -44, -44, -30, 6, -16, 5, -35, -30],
         [26, 22, -40, 46, 46, -22, -46, -36, 26, -50, -40, 35, -50, 35],
         [-50, 4, -4, 30, 16, -4, -34, 46, 34, 10, 38, -50, -45, 30, -15, 10],]
    ],
    'cum_sum': [
        [([-9, 42, 6],), ([0, 1, 3],), ([3, 2, 1],), ([-9, 9, -5, 5],), ],
        [[-9, 33, 39], [0, 1, 4], [3, 5, 6], [-9, 0, -5, 0]]
    ],
    'get_list_except_min_max': [
        [([81, 23, 94, 48, 15, 20, 54, 33, 32, 42, 98, 66, 40, 57, 79, 6, 35, 77, 11, 39, 36, 84, 62, 26, 38, 19, 67, 99, 63, 51, 49, 90, 7, 58, 55, 9, 25, 73, 34],), ([52, -16, -48, 2, -19],), ([94, -29, 79, -57],), ([-44, 51, 24],),
         ([98, 7, 41, 20],), ([-38, 46, 80],), ([-6, -80, -13, 22],), ([0, 24],), ([99, -100],), ],
        [(6,99),(-48, 52), (-57, 94), (-44, 51), (7, 98), (-38, 80), (-80, 22), (0, 24), (-100, 99) ],
        [([81, 23, 94, 48, 15, 20, 54, 33, 32, 42, 98, 66, 40, 57, 79, 35, 77, 11, 39, 36, 84, 62, 26, 38, 19, 67, 63, 51, 49, 90, 7, 58, 55, 9, 25, 73, 34],),([-16, 2, -19],), ([-29, 79],), ([24],),
         ([41, 20],), ([46],), ([-6, -13],), ([],),([],), ],
    ],
    'get_list_except_min_max_general': [
        [([5, 5, 5, 5 , 5],), ([-11, 13, -11,  13, -11],),
         ([-5, 2, -5, 10, -11, -11, 10, 0, -11, 2],), ([],), ],
        [5, 5, 5, 0,],
        [([],), ([],), ([-5, 2, -5, 0, 2],), ([],)]
    ],
    'reshape_by_index' : [
        [([4, 2, 1, -5], [1, 2, 3,  0], [2, 4, 6,  8],),
         ([4, 2, 1, -5], [3, 2, 1,  0], [0, 1, 2,  3],),
         ([0, 1, 7, -5], [1, 0, 2,  3], [3, 8, 20,  21],)],
        [ [None, None, 2, None, 1, None, -5, None, 4],
         [-5, 1, 2, 4],
         [None, None, None, 1, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, 7, -5]]
        ],
    'list_to_tuple' : [
        [ ([(2, -2, 4 ), (2, -2, 1 ), (0, 5, 4 ), (1,3), (1, 1, 5, 11)],),
          ([(1,1), (1,5)],),([(1,1,2), (1,0), (1,2,4,8,16,32)],),
        ],
        [ ([4, -2, 2], [1, -2, 2], [4, 5, 0]), tuple() , ([2, 1, 1], [0, 1], [32, 16, 8, 4, 2, 1]) ]
    ],
    'sort_by_month' : [
        [ (['Settembre', 'luglio', 'gennaio', 'Maggio'],),
          (['Settembre','Dicembre' ,'agosto' ,'Giugno' ,'luglio', 'gennaio', 'Maggio'],),
          (['novembre', 'febbraio'],),
          (['dicembre',
            'novembre',
            'ottobre',
            'settembre',
            'agosto',
            'luglio',
            'giugno',
            'maggio',
            'aprile',
            'marzo',
            'febbraio',
            'gennaio'],)  ],
        [ ['gennaio', 'Maggio', 'luglio', 'Settembre'],
         ['gennaio', 'Maggio', 'Giugno', 'luglio', 'agosto', 'Settembre', 'Dicembre'], ['febbraio', 'novembre'],
         ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre'] ]
    ],
    'sort_by_str' : [
        [ (('aaaaa', 'aaa', 'zzzzz', 'zzz'),),
         (('pipppo', 'pipppo', 'pipo', 'p','q','r','A','a','ab','AA','bb','p1ppp0'),),],
        [ ('zzz', 'aaa', 'zzzzz', 'aaaaa'), ('r', 'q', 'p', 'a', 'A', 'bb', 'ab', 'AA', 'pipo', 'pipppo', 'pipppo', 'p1ppp0')]
    ],
    'int_to_hist' : [
        [ ([1, 1, 1, 1, 4, 4, 4, 5, 5, 10, 10],),
          ([4, 3, -1, -3, 0, -1, 3, -2, 0, 1, 4, 0, -2, 3, 1, -3, 5, 5, 3, 4],),
          ( [6, 4, -1, -4, 0, -2, 5, -3, 0, 1, 7, 0, -4, 4, 2, -4, 7, 8, 5, 7, -3, 4, 7, 3, 0, -7, -1, 2, 7, 8, 0, 6, -4, 5, 1, -8, 4, -2, 6, 3, -8, 0, 6, -4, -3, 6, -5, 1, -4, 8, 5, -1, -7, -3, 0, 7, -7, 1, 4, 1, 5, 1, 8, 2, 1, -1, 2, -2, 1, -4, -5, -5, 2, 3, 0, -7, 4, 6, 7, 6, 7, 7, 1, -2, 3, -4, 5, 6, 7, 2, 8, 1, -1, 3, 8, 7, 5, -7, 2, 0],),],
        ['1\t****\n2\t\n3\t\n4\t***\n5\t**\n6\t\n7\t\n8\t\n9\t\n10\t**\n',
         '-3\t**\n-2\t**\n-1\t**\n0\t***\n1\t**\n2\t\n3\t****\n4\t***\n5\t**\n',
         '-8\t**\n-7\t*****\n-6\t\n-5\t***\n-4\t********\n-3\t****\n-2\t****\n-1\t*****\n0\t*********\n1\t**********\n2\t*******\n3\t*****\n4\t******\n5\t*******\n6\t********\n7\t***********\n8\t******\n']
    ],
    'anagramma' : [
        [('roma','amor'), ('elegant man','a gentleman'), ('fiore','eroii'), ],
        [True, True, False],
    ]
}


def evaluate(funct, is_assert=True):
    fname = funct.__name__
    print(f'> Valutiamo la funzione {fname}')
    if fname in evaluation_tests:
        inpts = evaluation_tests[fname][0]
        expts = evaluation_tests[fname][1]
        in_place = True if len(evaluation_tests[fname]) > 2 else False
        if in_place: iter_expts_in = iter(evaluation_tests[fname][2])
        for i, (inp, ex) in enumerate(zip(inpts, expts), 1):
            inp_copied = copy.deepcopy(inp)
            #tuple([copy.copy(i) for i in inp])
            out = funct(*inp_copied)
            if is_assert:
                assert type(out) == type(ex), (f'\n{"="*50}\nTipi diversi nel'
                                               f'risultato\ninput { inp }\noutput {type(out)}: {out} \nexpected'
                                               f'{type(ex)}: {ex}\n{"="*50}')
                assert out == ex, (f'\n{"="*50}\ninput { inp } \noutput '
                                   f'{out}\nexpected {ex}\n{"="*50}')
                if in_place:
                    exp_in = next(iter_expts_in)
                    for sing_in, sing_exp_in in zip(inp_copied,exp_in):
                        assert sing_in == sing_exp_in, (f'\n{"="*50}\ninput { inp } \nmodified input '
                                                        f'{inp_copied}\nexpected {exp_in}\n{"="*50}')

            print(f'{"="*50}\n>Test {i} input ',*inp,' PASSED! with'
                  f' expected value {out}')
            if in_place:
                print(f'>Also, input ',*inp,' was modified CORRECTLY as ',*exp_in,' ')

    else:
        print((f'> La funzione {fname} non è nei casi di test,'
               'controlla il nome della funzione'))


def show_tests(funct):
    fname = funct.__name__
    print(f'> Mostriamo i test per {fname}')
    if fname in evaluation_tests:
        inpts = evaluation_tests[fname][0]
        expts = evaluation_tests[fname][1]
        in_place = False
        if len(evaluation_tests[fname]) > 2:
            mod_inpts = evaluation_tests[fname][2]
            iter_expts_in = iter(mod_inpts)
            in_place = True
        for count, (inp, exp) in enumerate(zip(inpts, expts)):
            print(f'{"="*50}\n> {count})INPUT: ', *inp, end='\n')
            if in_place:
                exp_in = next(iter_expts_in)
                print(f'> {count})INPUT MODIFICATO: ', *exp_in, end='\n')
            print(f'> {count})ATTESO: ', exp, end='\n\n')
