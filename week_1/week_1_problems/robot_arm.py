import sys
import math
import random
import unittest
import itertools


# How much do I need to handle special cases?
def robot_arm_path(points):
    shortest_distance = math.inf

    all_the_combos = itertools.permutations(points)

    shortest_permutation = None
    # Yuck
    for combination in all_the_combos:
        distance = 0
        for first, second in zip(combination, combination[1:]):
            distance += calculate_distance(first, second)
        if distance < shortest_distance:
            shortest_permutation = combination
        shortest_distance = min(shortest_distance, distance)

    return shortest_permutation


def point_generator(number_of_points):
    return [(random.randint(-10, 10), random.randint(-10, 10))
            for _ in range(number_of_points)]


def calculate_distance(point_one, point_two):
    x_distance = (point_two[0] - point_one[0]) ** 2
    y_distance = (point_two[1] - point_one[1]) ** 2
    return math.sqrt(x_distance + y_distance)


def run_algorithm(number_points):
    points = point_generator(number_points)
    return robot_arm_path(points)


class TestRobotArm(unittest.TestCase):
    def test_point_generator(self):
        points = point_generator(10)
        self.assertEqual(10, len(points))

    def test_distance(self):
        self.assertEqual(2, calculate_distance((0, 0), (0, 2)))
        other_point = calculate_distance((-3, 4), (5, -9))
        self.assertEqual(15.26434, round(other_point, 5))

def main():
    unittest.main()


if __name__ == '__main__':
    shortest = run_algorithm(int(sys.argv[1:][0]))
    print(shortest)
    # main()
