"""
Copyright 2016, KnuVerse
All rights reserved.
"""
import copy
import itertools


class TriangleException(Exception):
    """Triangle Exception"""


class Triangles(object):
    def __init__(self):
        self.t1 = None
        self.t2 = None
        self.main_menu = \
            'Choose from the following options: \n' \
            '1) Edit triangle 1\n' \
            '2) Edit triangle 2\n' \
            '3) Get info about triangles\n' \
            '4) Exit\n' \
            ': '
        self.edit_menu = \
            'Enter 3 integers, separated by a space, for the' \
            ' lengths of the triangle: '
        self.info_menu = \
            'Choose from the following options: \n' \
            '1) Type of triangle 1\n' \
            '2) Type of triangle 2\n' \
            '3) Congruence/similarity between triangles 1 and 2\n' \
            '4) Exit\n' \
            ': '
        self.invalid_msg = 'Invalid input. Please try again.'

    def menu(self):
        while True:
            i = input(self.main_menu)
            if i not in {'1', '2', '3', '4'}:
                print(self.invalid_msg)
                continue
            if i == '1':
                self.t1 = self.edit_triangle()
            elif i == '2':
                self.t2 = self.edit_triangle()
            elif i == '3':
                self.get_triangle_info()
            elif i == '4':
                break

    def edit_triangle(self):
        while True:
            i = input(self.edit_menu)
            try:
                s1, s2, s3 = i.split(' ')
                s1, s2, s3 = int(s1), int(s2), int(s3)
                if not (s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1):
                    raise TriangleException('\nProvided side lengths cannot form a triangle\n')
            except TriangleException as te:
                print(te)
                continue
            except Exception:
                print(self.invalid_msg)
                continue
            if s1 <= 0 or s2 <=0 or s3 <= 0:
                print(self.invalid_msg)
                continue
            return [s1, s2, s3]

    def get_triangle_info(self):
        while True:
            i = input(self.info_menu)
            if i not in {'1', '2', '3', '4'}:
                print(self.invalid_msg)
                continue
            if i == '1':
                self.show_triangle_info(self.t1)
            elif i == '2':
                self.show_triangle_info(self.t2)
            elif i == '3':
                self.get_congruency_similarity()
            elif i == '4':
                break
        return

    @staticmethod
    def show_triangle_info(triangle):
        if triangle is None:
            print('Triangle is unset.')
            return

        type2 = None
        if all(x == triangle[0] for x in triangle):
            type1 = 'equilateral'
            type2 = 'acute'
        elif len(set(triangle)) == 2:
            type1 = 'isosceles'
        else:
            type1 = 'scalene'

        if not type2:
            largest = max(triangle)
            hypotenuse = 0
            for x in triangle:
                if x != largest:
                    hypotenuse += x**2

            if hypotenuse == largest**2:
                type2 = 'right'
            elif hypotenuse < largest**2:
                type2 = 'obtuse'
            else:
                type2 = 'acute'

        print('\nTriangle is {} and {}\n'.format(type1, type2))

    def get_congruency_similarity(self):
        if self.t1 is None or self.t2 is None:
            print('\nBoth triangles must be set first\n')
            return

        # Check congruency
        test_t2 = copy.copy(self.t2)
        for side in self.t1:
            result = self.check_if_in(side, test_t2)
            if not result:
                break

        if not test_t2:
            print('\nTriangles are congruent\n')
            return

        for perm in itertools.permutations(self.t2, 3):
            if self.t1[0]/float(perm[0]) == self.t1[1]/float(perm[1]) == self.t1[2]/float(perm[2]):
                print('\nTriangles are similar\n')
                return

        print('\nTriangles are neither congruent nor similar\n')

    @staticmethod
    def check_if_in(side, possibles):
        if side in possibles:
            possibles.remove(side)
            return True
        else:
            return False


if __name__ == '__main__':
    t = Triangles()
    t.menu()
