import matplotlib.pyplot as plt
import urllib2


CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def compute_in_degrees(digraph):
    """Compute how many nodes enter current node"""
    degrees = {key: 0 for key in digraph.iterkeys()}
    for _, adjacent in digraph.iteritems():
        # print _, adjacent
        for adj in adjacent:
            degrees[adj] += 1
    return degrees


def in_degree_distribution(digraph):
    """Computes how many different indegrees we have in the graph"""

    dicti = {}
    in_degree = compute_in_degrees(digraph).values()
    for value in in_degree:
        if value not in dicti:
            dicti[value] = 1
        else:
            dicti[value] += 1
    return dicti


def norm(dicti):
    """"this function normalizes values from a given dictionary"""

    distri = in_degree_distribution(dicti)
    normalized = {}
    for key in distri.iterkeys():
        normalized[key] = float(distri[key]) / sum([i for i in distri.itervalues()])

    return normalized



def graph1(graph):
    """Creates a plot from a normalized graph and presents in_degree distribution"""

    dicti = norm(graph)
    y = [value for value in dicti.itervalues()]
    x = [key for key in dicti.iterkeys()]

    plt.plot(x, y, 'co', ms=7.0)

    plt.title('Normalized in-degree distribution of a graph (log-log)')
    plt.xlabel('In-degree')
    plt.ylabel('Normalized weight')
   
    plt.loglog()
    plt.show()
    
    

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print "Loaded graph with", len(graph_lines), "nodes"

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph
    

    
graph1(load_graph(CITATION_URL))
