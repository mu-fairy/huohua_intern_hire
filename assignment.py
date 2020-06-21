from adapter import StreamAdapter
import json
from typing import Dict, Hashable, Iterable
import pandas as pd
import numpy as np


class CourseWareB(StreamAdapter):
    """
    在下面定义CourseWareB
    答案状态在commonComponentState下的4cb5f12f9e164c6c545a55202bc818f2下的answer字段
    正确答案是1，2，0，3
    """

    @staticmethod
    def __extract_panel_status(panel_status: Dict[str, str]) -> tuple:
        panel_state = [0, 0, 0, 0]
        m = panel_status.values()
        for i in m:
            panel_state = i
        return tuple(panel_state)

    @classmethod
    def load_raw_state(cls, raw_state: str) -> Hashable:

        state = json.loads(raw_state).get("commonComponentState")
        upper_panel_status = (0, 0, 0, 0)
        if state is not None:

            if "4cb5f12f9e164c6c545a55202bc818f2" in state:
                upper_panel_status = cls.__extract_panel_status(
                    state["4cb5f12f9e164c6c545a55202bc818f2"]
                )

        return upper_panel_status

    @classmethod
    def is_user_right(cls, stream: Iterable) -> bool:
        """
        正确答案是：
        1,2,0,3
        """
        right_ans = (1, 2, 0, 3)
        return stream == right_ans


if __name__ == "__main__":
    """
    在这里处理日志输出，输出结果为result.csv，三个字段为：学生ID，状态，是否为正确状态
    """
    dt = pd.read_csv("data.csv", error_bad_lines=False, sep="\t")
    raw_state = dt["state"]

    result = []
    for x in raw_state:
        result.append(CourseWareB.load_raw_state(x))

    is_right = []
    for y in result:
        is_right.append(CourseWareB.is_user_right(y))

    is_right = pd.DataFrame(is_right)
    dt['is_right'] = is_right

    dt = dt.drop(columns=["cr_code", "trace_id", "ctime_ts"])
    # print(dt)
    dt.to_csv('result.csv')
