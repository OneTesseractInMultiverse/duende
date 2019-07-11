import re


# -----------------------------------------------------------------------------
# CLASS STRUCTURED EDGE
# -----------------------------------------------------------------------------
class StructuredEdge(object):

    # -------------------------------------------------------------------------
    # CONVERT
    # -------------------------------------------------------------------------
    @staticmethod
    def cnv(name):
        """
        TODO Move this into a base class to avoid duplicated code
        :param name:
        :return:
        """
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    # -------------------------------------------------------------------------
    # CONSTRUCTOR ENDS
    # -------------------------------------------------------------------------
    def __init__(self):
        self.label = self.cnv(name=self.__class__.__name__)
        self.target_selector = None

    # -------------------------------------------------------------------------
    # STATE
    # -------------------------------------------------------------------------
    @property
    def state(self) -> dict:
        s = {}
        variables = [i for i in dir(self) if not callable(i) and i != 'state' and not i.startswith('__')]
        variables = [i for i in variables if i != 'label']
        variables = [i for i in variables if i != 'target_selector']
        variables = [i for i in variables if i != 'cnv']
        for x in variables:
            s[x] = getattr(self, x, "")
        return s

    # -------------------------------------------------------------------------
    # ARROW OPERATOR
    # -------------------------------------------------------------------------
    def __gt__(self, other):
        self.target_selector = other.selector


# -----------------------------------------------------------------------------
# CLASS STRUCTURED VERTEX
# -----------------------------------------------------------------------------
class StructuredVertex(object):

    # -------------------------------------------------------------------------
    # CONVERT
    # -------------------------------------------------------------------------
    @staticmethod
    def cnv(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    # -------------------------------------------------------------------------
    # CONSTRUCTOR
    # -------------------------------------------------------------------------
    def __init__(self, uid):
        self.uid = uid
        self.label = self.cnv(name=str(self.__class__.__name__))

    # -------------------------------------------------------------------------
    # STATE
    # -------------------------------------------------------------------------
    @property
    def state(self) -> dict:
        s = {}
        variables = [i for i in dir(self) if not callable(i) and i != 'state' and not i.startswith('__')]
        variables = [i for i in variables if i != 'label']
        variables = [i for i in variables if i != 'cnv']
        variables = [i for i in variables if i != 'selector']
        for x in variables:
            s[x] = getattr(self, x, "")
        return s

    @property
    def selector(self) -> dict:
        return {
            'label': self.label,
            'uid': self.uid
        }

    # -------------------------------------------------------------------------
    # OPERATOR - OVERRIDE
    # -------------------------------------------------------------------------
    def __sub__(self, other: StructuredEdge):
        print(other)
        return {
            'origin': self.selector,
            'edge': other.state,
            'target': other.target_selector
        }






