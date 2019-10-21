class ObjectTricks:
    def __init__(self):
        print(f'this is a Object py-trick')

    def keys_only(self, dict):
        """
        拿出key
        :param dict:
        :return:
        """
        return list(dict.keys())

    def map_values(self, obj, fn):
        """
        取出具有相同结构的次级键值对
        :param obj:
        :param fn:
        :return:
        """
        ret = {}
        for key in obj.keys():
            ret[key] = fn(obj[key])
        return ret

    def values_only(self, dict):
        return list(dict.values())


if __name__ == '__main__':
    obj_trk = ObjectTricks()
    users = {
        'fred-u': {'user': 'fred', 'age': 40},
        'pebbles-u': {'user': 'pebbles', 'age': 1}
    }
    print(obj_trk.map_values(users, lambda x: x['age']))  # {'fred-u': 40, 'pebbles-u': 1}
