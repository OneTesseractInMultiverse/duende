from gremlin_python.structure.graph import Graph

from gremlin_python import statics
from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

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
from gremlin_python.structure.graph import Vertex
from gremlin_python.process.graph_traversal import GraphTraversal
from gremlin_python.process.graph_traversal import as_ as AnonymousTraversal
from gremlin_python.process.graph_traversal import GraphTraversalSource
import csv
import pprint
import re
import time


# -------------------------------------------------------------------
# FUNCTION ADD EDGE
# -------------------------------------------------------------------
def add_vertex(data: dict, traversal, label):
    transaction = traversal.addV(label)
    for key in data.keys():
        if data[key] is None or str(data[key]) == "":
            transaction.property(key, 'n/a')
        else:
            transaction.property(key, str(data[key]))
    return transaction.next()


# -------------------------------------------------------------------
# FUNCTION DELETE EVERYTHING
# -------------------------------------------------------------------
def delete_everything(traversal: GraphTraversalSource):
    return traversal.V().drop().toList()


def get_property_pivot(data, prop):
    customers = []
    for vmx in data:
        customers.append(vmx[prop])
    return list(set(customers))


g = Graph().traversal().withRemote(DriverRemoteConnection('ws://169.46.9.99:32344/gremlin', 'dataplatform_dev'))


parsed_data = []

with open('assets.csv') as f:
    parsed_data = [{k: v for k, v in row.items()}
                   for row in csv.DictReader(f, skipinitialspace=True)]

# for v in parsed_data:
#     print(add_vertex(v, g, "VirtualMachineConfigurationItem"))
#
#
# for v in get_property_pivot(parsed_data, 'customer_id')[0:10]:
#
#     g.V().hasLabel("VirtualMachineConfigurationItem").has('')
#
#
# for v in get_property_pivot(parsed_data, 'datacenter_id'):
#     print(add_vertex({'id': v}, g, "DataCenter"))
#
#

xz = None

# for v in get_property_pivot(parsed_data, 'hypervisor_cluster_id'):
#     if v is not None and v != "":
#         print(v)
#         xz = g.withSideEffect(
#             'a',
#             g.V().hasLabel("VirtualMachineConfigurationItem").has('hypervisor_cluster_id', v).range(0, 15).toList()
#         ).V().hasLabel("HypervisorCluster").has('id', v).outE('owns', 'a')
# print(xz.toList())

#
# for v in get_property_pivot(parsed_data, 'hypervisor_cluster_id'):
#     if v is not None and v != "":
#         print(v)
#         hypervisor = g.V().hasLabel("HypervisorCluster").has('id', v).range(0, 1).next()
#         print(hypervisor)


cluster: Vertex = g.V().hasLabel("HypervisorCluster").has('id', 'test_hypervisor_001').next()
print(type(cluster))

vertices = g.V().hasLabel("VirtualMachineConfigurationItem").has('hypervisor_cluster_id', 'test_hypervisor_001').range(0, 20).toList()

for x in vertices:
    g.V(cluster).outE("hosts").to(x).next()


# print(g.V().hasLabel("VirtualMachineConfigurationItem").has('short_hostname', 'cnbj11v101038').toList())

# pprint.pprint(g.V().hasLabel("VirtualMachineConfigurationItem").range(0, 1).valueMap().toList())

# pprint.pprint(g.V().hasLabel("VirtualMachineConfigurationItem").has('host_shortname', 'gbcnvpwxaa031').range(0, 1).toList())


