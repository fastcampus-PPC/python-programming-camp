class GradeMap:
    _instance = None

    @classmethod
    def _getInstance(cls):
        return cls._instance


    @classmethod
    def instance(cls, *args, **kargs):
        cls._instance = cls(*args, **kargs)
        cls.instance = cls._getInstance
        return cls._instance


    def __init__(self):
        self._dict = {}


    def setitem(self, key, item):
        # some codes here
        pass


    def getitem(self, key):
        return self._dict[key]


    def length(self):
        return len(self._dict)


    def clear(self):
        return self._dict.clear()


    def copy(self):
        return self._dict.copy()


    def has_key(self, key):
        return key in self._dict


    def keys(self):
        return self._dict.keys()


    def items(self):
        return self._dict.items()


    def get_grade(self, value):
        return self._dict.get(value)