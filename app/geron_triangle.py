from math import sqrt
from app.ask import ask


def geron_triangle(args):
    def triangle(a, b, c):
        p = (float(a) + float(b) + float(c)) / 2
        return sqrt(float(p) * (float(p) - float(a)) * (float(p) - float(b)) * (float(p) - float(c)))

    def _check_args():
        if args.triangle_name is not None and args.triangle_a is not None and args.triangle_b is not None \
                and args.triangle_c is not None and not args.triangle_a.isalpha() \
                and not args.triangle_b.isalpha() and not args.triangle_c.isalpha() \
                and args.triangle_name != 'def' and args.triangle_a != 'def' and args.triangle_b != 'def' \
                and args.triangle_c != 'def' and (float(args.triangle_c) < (float(args.triangle_a) + float(args.triangle_b)) or float(args.triangle_c) > (float(args.triangle_a) - float(args.triangle_b))):
            return True
        else:
            return False

    def _check_triangle_list(triangles):
        if len(triangles) == 4 and triangles[1].replace('.', '', 1).isdigit() and \
                triangles[2].replace('.', '', 1).isdigit() and triangles[3].replace('.', '', 1).isdigit() and \
                (float(triangles[3]) < (float(triangles[1]) + float(triangles[2])) or
                 float(triangles[3]) > (float(triangles[1]) - float(triangles[2]))):
            return True
        else:
            return False

    while True:
        if _check_args():
            print(triangle(args.triangle_a, args.triangle_b, args.triangle_c))
            args.triangle_name = args.triangle_a = args.triangle_b = args.triangle_c = 'def'
        else:
            while True:
                result = {}
                arg_list = []
                while True:
                    triangles = input('Enter <triangle name>, <side a>, <side b>, '
                                      '<side c> (Parties must be number or float): ').replace(' ', '').split(
                        ',')
                    if _check_triangle_list(triangles):
                        arg_list.append(triangles)
                    else:
                        print('Parameters not entered correctly')
                        continue
                    ask_triangle = input('Add triangle? (Y / YES): ').lower()
                    if ask_triangle == 'y' or ask_triangle == 'yes':
                        continue
                    else:
                        break
                for i in arg_list:
                    result[i[0]] = result.get(i[0], 0) + triangle(i[1], i[2], i[3])
                for name, value in sorted(result.items(), key=lambda x: x[1], reverse=True):
                    print(f'{name}: {value} cm')

                if ask():
                    continue
                else:
                    break
            break
