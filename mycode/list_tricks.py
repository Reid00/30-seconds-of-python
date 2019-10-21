from math import ceil


class ListTricks:
    def __init__(self):
        print(f'Those is some py-tricks for list data structure')

    def all_equal(self, lst):
        """
        确认在list 里面的元素是否都相同
        Yes true,No, false
        :return:
        """
        return lst[:] == lst[:-1]

    def all_unique(self, lst):
        """
        认在list 里面的元素是否唯一
        :param lst:
        :return:
        """
        return len(lst) == len(set(lst))

    def bifurcate(self, lst, filter):
        """
        将列表值分组
        :param lst:
        :param filter: also list tag,true or false
        :return:
        """
        return [
            [x for i, x in enumerate(lst) if filter[i] == True],
            [x for i, x in enumerate(lst) if filter[i] == False],
        ]

    def bifurcate_by(self, lst, fn):
        """

        :param lst:
        :param fn: this is a function
        :return:
        """
        return [
            [x for x in lst if fn(x)],
            [x for x in lst if not fn(x)],
        ]

    def chunk(self, lst, size):
        """
        把一个list 分成指定的大小
        :param lst:
        :param size:
        :return:
        """
        return list(
            map(lambda x: lst[x * size:x * size + size],
                list(range(0, ceil(len(lst) / size)))
                )
        )

    def compact(self, lst):
        """
        用filter 过滤掉无效的值(False,None,0 and "")
        :param lst:
        :return:
        """
        return list(filter(bool, lst))

    def count_by(self, lst, fn=lambda x: x):
        """
        根据fn 这个功能对list 进行过滤
        :param lst:
        :param fn: 函数
        :return:
        """
        key = {}
        for ele in map(fn, lst):
            key[ele] = 1 if ele not in key else key[ele] + 1
        return key

    def difference(self, lst1, lst2):
        """
        比较两个list 之间的不同
        :param lst1:
        :param lst2:
        :return:
        """
        lst2 = set(lst2)
        return [item for item in lst1 if item not in lst2]


if __name__ == '__main__':
    lst_trk = ListTricks()
    print(lst_trk.difference([1, 2, 3], [1, 2, 4]))  # [3]
    print(lst_trk.count_by(['one', 'two', 'three'], len))  # {3: 2, 5: 1}
    print(lst_trk.compact([0, 1, False, 2, '', 34]))  # [1, 2, 34]
    print(lst_trk.chunk([1, 2, 3, 4, 5], 2))  # [[1, 2], [3, 4], [5]]
    print(lst_trk.bifurcate_by(['beef', 'boop', 'foo', 'bar'],
                               lambda x: x[0] == 'b'))  # [['beef', 'boop', 'bar'], ['foo']]
    print(lst_trk.bifurcate(['beef', 'boop', 'foo', 'bar'],
                            [True, True, False, True]))  # [['beef', 'boop', 'bar'], ['foo']]
    print(lst_trk.all_unique([1, 2, 3, 4, 4]))  # False
    print(lst_trk.all_equal([1, 1, 1]))  # False
