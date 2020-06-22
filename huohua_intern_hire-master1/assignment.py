import csv
from adapter import StreamAdapter
import json
from typing import Dict, Hashable, Iterable


class CourseWareB(StreamAdapter):
    """
    在下面定义CourseWareB
    答案状态在commonComponentState下的4cb5f12f9e164c6c545a55202bc818f2下的answer字段
    正确答案是1，2，0，3
    """

    @staticmethod
    def __extract_panel_status(panel_status: Dict[str, str]) -> tuple:
        panel_state = list(panel_status.values())[0]
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
    # 使用标准的Python类库导入csv数据
    filename = 'data.csv'
    eFile = open(filename)
    # 读取csv文件
    eReader = csv.reader(eFile, delimiter="\t")
    dt = list(eReader)

    result = []
    for x in range(1, len(dt)-1):
        result.append(CourseWareB.load_raw_state(dt[x][3]))

    print(result)

    is_right = []
    for y in result:
        is_right.append(CourseWareB.is_user_right(y))

    print(is_right)

    m = [0, 3]
    final = []
    for x in range(0, len(dt)-1):
        dt1 = []
        for y in m:
            dt1.append(dt[x][y])
        final.append(dt1)
    print(final)

    final[0].append("is_right")
    print(final)
    for x in range(1, len(dt)-1):
        final[x].append(is_right[x-1])

    print(final)

    with open("result.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(final[0])
        row = final[1:len(final)]
        for r in row:
            writer.writerow(r)

