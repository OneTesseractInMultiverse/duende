from gremlin_python.structure.graph import Graph

from gremlin_python import statics
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Order
from gremlin_python.process.traversal import Cardinality
from gremlin_python.process.traversal import Column
from gremlin_python.process.traversal import Direction
from gremlin_python.process.traversal import Operator
from gremlin_python.process.traversal import P
from gremlin_python.process.traversal import Pop
from gremlin_python.process.traversal import Scope
from gremlin_python.process.traversal import Barrier
from gremlin_python.process.traversal import Bindings
from gremlin_python.process.graph_traversal import GraphTraversal
from gremlin_python.process.graph_traversal import as_ as AnonymousTraversal
from gremlin_python.process.graph_traversal import GraphTraversalSource


g = Graph().traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin', 'g'))

print(g.addV('person').property('name', 'Pedro').property('last_name', 'Guzman').toList())
print(g.V().toList())



