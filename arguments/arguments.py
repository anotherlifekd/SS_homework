import argparse


def parse():
    parser = argparse.ArgumentParser(description="Elementary tasks homework")

    # ALL_PROGRAMS
    parser.add_argument('choose', nargs='?', help='Programs: <chess>, <analytics>, <geron_triangle>, <files>, '
                                                  '<sequence>, <numbers>, <fibonacci>, <happy_ticket>. Select the '
                                                  'program for the first argument. Then select the appropriate '
                                                  'parameters for your task in the positional arguments.')
    # CHESS
    parser.add_argument('--width', nargs='?', dest='width', help='Chess board. Set width', default='default')
    parser.add_argument('--height', nargs='?', dest='height', help='Chess board. Set height', default='default')

    # ANALYTICS
    parser.add_argument('--envelope_a', nargs='?', dest='envelope_a',
                        help='Analytics. Set A side (first envelope):', default='default')
    parser.add_argument('--envelope_b', nargs='?', dest='envelope_b',
                        help='Analytics. Set B side (first envelope):', default='default')
    parser.add_argument('--envelope_c', nargs='?', dest='envelope_c',
                        help='Analytics. Set A side (second envelope):', default='default')
    parser.add_argument('--envelope_d', nargs='?', dest='envelope_d',
                        help='Analytics. Set A side (second envelope):', default='default')

    # TRIANGLE
    parser.add_argument('--triangle_name', nargs='?', dest='triangle_name',
                        help='Geron triangle. Set name:', default='def')
    parser.add_argument('--triangle_a', nargs='?', dest='triangle_a', help='Geron triangle. Set A side:', default='def')
    parser.add_argument('--triangle_b', nargs='?', dest='triangle_b', help='Geron triangle. Set B side:', default='def')
    parser.add_argument('--triangle_c', nargs='?', dest='triangle_c', help='Geron triangle. Set C side:', default='def')

    # FILES
    parser.add_argument('--files_name', nargs='?', dest='files_name', help='Files. Set name:', default='def')
    parser.add_argument('--mod', nargs='?', dest='mod', help='Files. Set mod:', default='def')
    parser.add_argument('--string_for_count', nargs='?', dest='string_for_count',
                        help='Files. Set a string:', default='def')
    parser.add_argument('--string_for_search', nargs='?', dest='string_for_search',
                        help='Files. Set search string:', default='def')
    parser.add_argument('--string_for_replace', nargs='?', dest='string_for_replace',
                        help='Files. Set replace string:', default='def')

    # SEQUENCE
    parser.add_argument('--n', nargs='?', dest='n', help='Sequence. Set n:', default='default')

    # NUMBERS
    parser.add_argument('--num', nargs='?', dest='num', help='Numbers. Set your number:', default='default')

    # FIBONACCI
    parser.add_argument('--arg_1', nargs='?', dest='arg_1', help='Fibonacci. Set start:', default='default')
    parser.add_argument('--arg_2', nargs='?', dest='arg_2', help='Fibonacci. Set end:', default='default')

    return parser.parse_args()
