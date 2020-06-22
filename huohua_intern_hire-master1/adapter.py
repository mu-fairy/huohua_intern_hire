import abc
from typing import Hashable, Iterable


class StreamAdapter(abc.ABC):
    """
    为了探究 自主模式 与 学生转化率、正确率 之间的关系，
    StreamAdapter为了解决“不同课件（cw_code）、不同题（cw_position）”之间的差异，抽象了处理差异的若干个方法。

    测试文件见 PROJ_DIR/tests/*_adapter.py
    """

    @classmethod
    @abc.abstractmethod
    def is_user_right(cls, stream: Iterable) -> bool:
        """
        根据学生做题的数据打点列表，判断学生正误

        Keyword arguments:
        stream -- 学生做题的数据打点列表（由于题目的答案打点不同，列表内元素可能是不同的数据格式）
        """
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def load_raw_state(cls, raw_state: str) -> Hashable:
        """
        将hive中字符串形式的作答数据，解析成python的高级数据结构

        Keyword arguments:
        raw_state -- 学生单个时间戳下的打点数据
        """
        raise NotImplementedError
