import unittest
import json
from example import CourseWareA


class ExampleTest(unittest.TestCase):

    def test_load_raw_state(self):
        # GIVEN
        raw_state = {
            "commonComponentState": {
                "1320aa045341fe29dbd74a5b90b29b84": {"status": {"1": 2}},
                "414e4fa6b00c471323fdd66abae49717": {"status": {"2": 1}},
            },
        }

        # WHEN
        result = CourseWareA.load_raw_state(json.dumps(raw_state))

        # THEN
        target_state = ((0, 2, 0), (0, 0, 1))
        self.assertEqual(target_state, result)

    def test_partial_empty_state(self):
        # GIVEN
        raw_state = {
            "commonComponentState": {
                "1320aa045341fe29dbd74a5b90b29b84": {"status": {"1": 2}},
            },
        }

        # WHEN
        result = CourseWareA.load_raw_state(json.dumps(raw_state))

        # THEN
        target_state = ((0, 2, 0), (0, 0, 0))
        self.assertEqual(target_state, result)

    def test_is_user_right(self):
        # GIVEN
        stream = [((3, 1, 4), (4, 3, 1))]
        # THEN
        self.assertTrue(CourseWareA.is_user_right(stream))

        stream = [((3, 1, 3), (3, 3, 1))]
        self.assertTrue(not CourseWareA.is_user_right(stream))

        stream = [((3, 1, 4), (3, 4, 1))]
        self.assertTrue(not CourseWareA.is_user_right(stream))