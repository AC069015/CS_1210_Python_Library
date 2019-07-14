from HW8queue1210 import *
from HW8BasicGraph import *

#####
#
# classic Breadth First Search
#
# See, e.g., http://en.wikipedia.org/wiki/Breadth-first_search
#

def bfs(graph, startNode):
    for n in graph.nodes:
        n.setStatus('unseen')
    startNode.setStatus('seen')
    #print("Initializing queue with: ", startNode.name)
    queue = Queue()
    queue.enqueue(startNode)
    while queue.size() != 0:
        #print(queue)
        currentNode = queue.dequeue()
        #print("removed {} from queue. Processing neighbors".format(currentNode.name))
        for node in graph.neighborsOf(currentNode):
            if node.getStatus() == 'unseen':
                node.setStatus('seen')
                node.setParent(currentNode)
                queue.enqueue(node)
        currentNode.setStatus('processed')



