from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from duende.core import StructuredVertex


# -----------------------------------------------------------------------------
# CLASS GREMLIN REMOTE CONNECTION
# -----------------------------------------------------------------------------
class RemoteGremlinConnection(object):

    """
        This class is used to encapsulate the connection to a remote
        Gremlin Server.
    """

    def __init__(self, connection_string: str, remote_traversal_source):
        """
        TODO support for authenticated requests
        :param connection_string:
        :param remote_traversal_source:
        """
        self.__connection_str = connection_string
        self.__remote_traversal_source = remote_traversal_source
        self.__graph = Graph()

    @property
    def graph(self):
        return self.__graph.traversal()\
            .withRemote(
            DriverRemoteConnection(
                self.__connection_str,
                self.__remote_traversal_source
            )
        )


# -----------------------------------------------------------------------------
# CLASS DUENDE
# -----------------------------------------------------------------------------
class Duende(object):

    def __init__(self, connection: RemoteGremlinConnection):
        self.conn = connection

    @property
    def g(self):
        return self.conn.graph

    def purge_graph(self):
        return self.g.V().drop().toList()

    # -------------------------------------------------------------------------
    # METHOD CONNECT TWO VERTICES
    # -------------------------------------------------------------------------
    def __add__(self, other: StructuredVertex):
        return self._create_vertex(other.label, other.state)

    # -------------------------------------------------------------------------
    # METHOD CREATE VERTEX
    # -------------------------------------------------------------------------
    def _create_vertex(self, label, properties: dict):
        print(properties)
        if 'uid' not in properties.keys():
            raise AttributeError('All vertices must contain a uid')

        t = self.g.addV(label)
        for prop in properties.keys():
            t = t.property(prop, properties[prop])
        return t.toList()

    # -------------------------------------------------------------------------
    # METHOD SELECT VERTICES
    # -------------------------------------------------------------------------
    def select_vertices(self, selector: dict):
        result = self.g.V()
        if 'label' in selector:
            result.hasLabel(selector['label'])
            del selector['label']
        for key in selector.keys():
            result = result.has(key, selector[key])
        return result.next()

    def connect(self, mapping: dict):
        return self.connect_two_vertices(
            mapping['origin'],
            mapping['target'],
            mapping['edge']
        )

    # -------------------------------------------------------------------------
    # METHOD CONNECT TWO VERTICES
    # -------------------------------------------------------------------------
    def connect_two_vertices(self, origin_selector: dict, target_selector: dict,
                             edge_label, edge_properties: dict = None):
        origin = self.select_vertices(origin_selector)
        target = self.select_vertices(target_selector)
        if origin and target:
            e = self.g.V(origin).addE(edge_label)
            if edge_properties:
                for prop in edge_properties.keys():
                    e.property(prop, edge_properties[prop])
            return e.to(target).next()
        return None




