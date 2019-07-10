class StructuredVertex(object):

    def __init__(self, uid):
        self.uid = uid
        self.label = self.__class__.__name__.lower()

    @property
    def state(self) -> dict:
        s = {}
        variables = [i for i in dir(self) if not callable(i) and i != 'state' and not i.startswith('__')]
        variables = [i for i in variables if i != 'label']
        # for attribute in [i for i in dir(self) if not callable(i) and i != 'label' and not i.startswith("__")]:
        for x in variables:
            s[x] = getattr(self, x, "")
        return s


