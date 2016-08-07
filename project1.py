"""Skripta za analizu citiranosti naučnih radova. Kao input uzima graf. U primeru koji je korišćen ispod,
graf ima 27 770 čvorova (radova iz fizike visokih energija) i 352,768 grana (veza između pojedinačnih radova). 
Program prvo računa citiranost svakog pojedinačnog rada, a zatim izračunava distribuciju dobijene citiranosti, koju potom normalizuje. 
Nakon normalizacije skripta formira dijagram koji na ordinati ima normalizovanu distribuciju citiranosti, 
a na apscisi broj citata svakog pojedinačnog rada.
Na ovaj način prikazani podaci ukazuju na zastupljenost određene citiranosti rada u odnosu na ukupnu populaciju citiranosti radova. 
U  navedonom primeru sa radovima iz fizike visokih energija, na osnovu grafika se može videti da najveći udeo u populaciji imaju
radovi sa malim (jednocifrenim) brojem citata, dok radovi sa velikim (trocifrenim i četvorocifrenim) brojem citata zauzimaju najmanji
udeo u populaciji. Drugim rečima, zavisnost između broja citata pojedinačnog rada, i zastupljenosti  količine radova sa tim brojem
citatata u ukupnoj populaciji je obrnuto proporcionalna."""

import matplotlib.pyplot as plt
import urllib2
import itertools


CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


def compute_in_degrees(digraph):
    """Compute how many nodes enter current node"""
    degrees = {key: 0 for key in digraph.iterkeys()}
    for value in digraph.itervalues():
       
        for val in value:
            degrees[val] += 1
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
