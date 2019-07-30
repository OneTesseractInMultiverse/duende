from duende import RemoteGremlinConnection, Duende
from duende.core import StructuredVertex, StructuredEdge
import pprint

connection = RemoteGremlinConnection('ws://169.46.9.99:31831/gremlin', 'g')

graph = Duende(connection=connection)

graph.purge_graph()


class Person(StructuredVertex):

    def __init__(self, uid, name, last_name):
        super().__init__(uid=uid)
        self.name = name
        self.last_name = last_name


for i in range(3):
    p = Person('ABC123{}'.format(i), 'RandomName{}'.format(i), 'RandomLastName{}'.format(i))
    print(graph + p)

pprint.pprint(graph.g.V().hasLabel('person').valueMap().toList())

# graph.connect_two_vertices({'uid': '1239'}, {'uid': '1238'}, 'knows', {})

# pprint.pprint(graph.g.V().outE('knows').inV().values('name', 'last_name').toList())



