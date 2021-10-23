class Box:
    def __init__(self, min_entry, max_entry):
        self._min_entry = min_entry
        self._max_entry = max_entry

    def get_min_value(self):
        return int(self._min_entry.get())

    def get_max_value(self):
        return int(self._max_entry.get())

    def get_set_of_values(self):
        my_set = set()
        for i in range(self.get_min_value(), self.get_max_value() + 1):
            my_set.add(frozenset({i}))
        return my_set
