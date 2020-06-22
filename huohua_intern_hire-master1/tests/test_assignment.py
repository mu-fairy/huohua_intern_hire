import json
import unittest
from assignment import CourseWareB


class AssignmentTest(unittest.TestCase):
    """
    这两个测试必写，你也可以增加其他你认为重要的测试
    """

    def test_load_state(self):
        # GIVEN
        raw_state = {
            "commonComponentState": {
                "4cb5f12f9e164c6c545a55202bc818f2": {"answer": [-1, 2, 0, -1]}
            },
        }

        # WHEN
        result = CourseWareB.load_raw_state(json.dumps(raw_state))

        # THEN
        target_state = (-1, 2, 0, -1)
        self.assertEqual(target_state, result)

    def test_right_ans(self):
        # GIVEN
        stream = (1, 2, 0, 3)
        # THEN
        self.assertTrue(CourseWareB.is_user_right(stream))
        #
        stream = (-1, 2, 0, 3)
        self.assertTrue(not CourseWareB.is_user_right(stream))
        #
        stream = [(1, 1, 0, 3)]
        self.assertTrue(not CourseWareB.is_user_right(stream))


if __name__ == "__main__":
    unittest.main()
