# def check(a):
#     if a.choose == 'chess':
#         if a.width is not None and a.height is not None and a.width.isdigit() and a.height.isdigit() and \
#                 int(a.width) % 2 != 1 and int(a.height) % 2 != 1 and a.width != 'default' and a.height != 'default':
#             return True
#         else:
#             return False
#     if a.choose == 'analytics':
#         if a.envelope_a is not None and a.envelope_b is not None and a.envelope_c is not None and \
#                 a.envelope_d is not None and a.envelope_a.replace('.', '', 1).isdigit() and \
#                 a.envelope_b.replace('.', '', 1).isdigit() and a.envelope_c.replace('.', '', 1).isdigit() and \
#                 a.envelope_d.replace('.', '', 1).isdigit() and float(a.envelope_a) > 0 and float(a.envelope_b) > 0 and \
#                 float(a.envelope_c) > 0 and float(a.envelope_d) > 0:
#             return True
#         else:
#             return False
#     if a.choose == 'geron_triangle':
#         if a.triangle_name is not None and a.triangle_a is not None and a.triangle_b is not None \
#                 and a.triangle_c is not None and not a.triangle_a.isalpha() \
#                 and not a.triangle_b.isalpha() and not a.triangle_c.isalpha() \
#                 and a.triangle_name != 'def' and a.triangle_a != 'def' and a.triangle_b != 'def' \
#                 and a.triangle_c != 'def' and (float(a.triangle_c) < (float(a.triangle_a) + float(a.triangle_b)) \
#                 or float(a.triangle_c) > (float(a.triangle_a) - float(a.triangle_b))):
#             return True
#         else:
#             return False
#
#
# def check_triangle_list(triangles):
#     if len(triangles) == 4 and triangles[1].replace('.', '', 1).isdigit() and \
#             triangles[2].replace('.', '', 1).isdigit() and triangles[3].replace('.', '', 1).isdigit() and \
#             (float(triangles[3]) < (float(triangles[1]) + float(triangles[2])) or
#              float(triangles[3]) > (float(triangles[1]) - float(triangles[2]))):
#         return True
#     else:
#         return False
