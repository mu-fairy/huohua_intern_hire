import json
from typing import Dict, Hashable, Iterable
from adapter import StreamAdapter


class CourseWareA(StreamAdapter):
    @staticmethod
    def __extract_panel_status(panel_status: Dict[str, str]) -> tuple:
        panel_state = [0, 0, 0]
        for idx, n in panel_status.items():
            panel_state[int(idx)] = int(n)
        return tuple(panel_state)

    @classmethod
    def load_raw_state(cls, raw_state: str) -> Hashable:
        """
        1320aa045341fe29dbd74a5b90b29b84代表上层面板
        414e4fa6b00c471323fdd66abae49717代表下层面板
        每层面板的数据存储形式是 DICT[位置，数量]，例如{"0":2,"2":1}表示在第一格有2只小手，在第三格有1只小手
        """

        state = json.loads(raw_state).get("commonComponentState")
        upper_panel_status = (0, 0, 0)
        lower_panel_status = (0, 0, 0)
        if state is not None:

            if "1320aa045341fe29dbd74a5b90b29b84" in state:
                upper_panel_status = cls.__extract_panel_status(
                    state["1320aa045341fe29dbd74a5b90b29b84"]["status"]
                )

            if "414e4fa6b00c471323fdd66abae49717" in state:
                lower_panel_status = cls.__extract_panel_status(
                    state["414e4fa6b00c471323fdd66abae49717"]["status"]
                )
        return upper_panel_status, lower_panel_status

    @classmethod
    def is_user_right(cls, stream: Iterable) -> bool:
        """
        正确答案是：
        上层面板：第一格3只小手，第二格1只小手，第三格4只小手
        下层面板：第一格4只小手，第二格3只小手，第三格1只小手
        """
        right_ans = ((3, 1, 4), (4, 3, 1))
        return list(stream)[-1] == right_ans
