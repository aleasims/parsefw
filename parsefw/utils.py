class named_list(list):
    def __getitem__(self, key):
        if isinstance(key, str):
            return
        else:
            return super().__getitem__(key)
 