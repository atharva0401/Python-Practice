''' Python Program to perform operations on graphs.'''
import urllib2
EX_GRAPH0={0:set([1,2]),1:set([]),2:set([])}
EX_GRAPH1={0:set([1,4,5]),1:set([2,6]),2:set([3]),3:set([0]),4:set([1]),5:set([2]),6:set([])}
EX_GRAPH2={0:set([1,4,5]),1:set([2,6]),2:set([3,7]),3:set([7]),4:set([1]),5:set([2]),6:set([]),7:set([3]),8:set([1,2]),9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    ''' Returns a complete directed graph for given number of nodes  in the form of a dictionary'''
    comp_graph={}
    if num_nodes>0:
        for countr1 in range(num_nodes):
            countr2=0
            lis=[]
            while countr2<num_nodes:
                if countr2!=countr1:
                    lis.append(countr2)
                countr2=countr2+1
            comp_graph[countr1]=set(lis)
        return comp_graph
    else:
        return comp_graph

def compute_in_degrees(digraph):
    ''' Computes indegree of each node
    in the given digraph and returns a dictionary
    whose values correspond  to indegree of each node. '''
    key_list=list(digraph.keys())
    in_deg_graph={x:0 for x in key_list}
    for countr1 in key_list:
        node_list=list(digraph[countr1])
        for countr2 in range(len(node_list)):
            key=node_list[countr2]
            in_deg_graph[key]=in_deg_graph[key]+1
    return in_deg_graph

def in_degree_distribution(digraph):
    ''' Computes the indegree distribution of the given digraph
    and returns a dictionary whose values correspond to the number of nodes having a particular indegree'''
    in_d_distr={i:0 for i in range(len(digraph))}
    dum_dict=compute_in_degrees(digraph)
    for countr1 in dum_dict.keys():
        key=dum_dict[countr1]
        in_d_distr[key]=in_d_distr[key]+1
    for countr1 in in_d_distr.keys():
        if in_d_distr[countr1]==0:
            del in_d_distr[countr1]
    return in_d_distr
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

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

citation_graph = load_graph(CITATION_URL)
print(citation_graph)


