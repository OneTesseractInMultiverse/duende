from duende import RemoteGremlinConnection, Duende
from duende.core import StructuredVertex, StructuredEdge
import pprint

connection = RemoteGremlinConnection('ws://localhost:8182/gremlin', 'g')

graph = Duende(connection=connection)

graph.purge_graph()


class Person(StructuredVertex):

    def __init__(self, uid, name, last_name):
        super().__init__(uid=uid)
        self.name = name
        self.last_name = last_name


class IsFriendOf(StructuredEdge):

    def __init__(self, since: str):
        super().__init__()
        self.since = since


for i in range(10):
    p = Person('123{}'.format(i), 'Pedro{}'.format(i), 'Guzman{}'.format(i))
    print(graph + p)

pprint.pprint(graph.g.V().hasLabel('person').valueMap().toList())

p1 = Person('xyz', 'John', 'Smith')
p2 = Person('abc', 'Jane', 'Smith')
e = IsFriendOf(since='1/1/2019')
graph.connect(p1 - (e > p2))

# graph.connect_two_vertices({'uid': '1239'}, {'uid': '1238'}, 'knows', {})

pprint.pprint(graph.g.V().outE('knows').inV().values('name', 'last_name').toList())



