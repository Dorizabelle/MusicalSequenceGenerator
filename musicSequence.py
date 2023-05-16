import sys
import subprocess
import random

# create a double of the intervals and reverse the strength to show bad melodies
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        """
        This method makes sure that the graph is symmetrical.
        In other words, if there's a path from node A to B with a value V,
        there needs to be a path from node B to node A with a value V.
        """
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def print_result(random_sequence, x):
    path = []
    node = random_sequence[0] # Start with the first node in the sequence
    
    for i in range(1, len(random_sequence)): # Iterate over the rest of the nodes in the sequence
        path.append(node)
        node = random_sequence[i]
    path.append(node)
    
    print("We found the following random sequence ofa notes:")
    print(" -> ".join(psath)) 
    return " ".join(path)

#
if __name__ == "__main__":

    print('Enter the note you would like to start on "a", "ais", "b", "c", "cis", "d", "dis", "e", "f", "fis", "g",  "gis".  and "is" indicates sharp):')
    startNote = input()
    print(startNote + " is the note")
    print('Would you like a good or bad sequence? Enter g for good, and b for bad: ')
    quality = input()
  
    print('Enter the desired length of the melody:')
    length = int(input())


    nodes = ["a", "ais", "b", "c", "cis", "d", "dis", "e", "f", "fis", "g",  "gis"]
 
    init_graph = {}
    for node in nodes:
        init_graph[node] = {}
    
    #correct intervals
    #Perfect fifths
    init_graph["c"]["g"] = 11
    init_graph["cis"]["gis"] = 11
    init_graph["d"]["a"] = 11
    init_graph["dis"]["ais"] =11
    init_graph["e"]["b"] = 11
    init_graph["f"]["c"] = 11
    init_graph["fis"]["cis"] = 11
    init_graph["g"]["d"] = 11
    init_graph["gis"]["dis"] = 11
    init_graph["a"]["e"] = 11
    init_graph["ais"]["f"] = 11
    init_graph["b"]["fis"] = 11

    #Perfect fourths up
    init_graph["c"]["f"] = 10
    init_graph["cis"]["fis"] = 10
    init_graph["d"]["g"] = 10
    init_graph["dis"]["gis"] =10
    init_graph["e"]["a"] = 10
    init_graph["f"]["ais"] = 10
    init_graph["fis"]["b"] = 10
    init_graph["g"]["c"] = 10
    init_graph["gis"]["cis"] = 10
    init_graph["a"]["d"] = 10
    init_graph["ais"]["dis"] = 10
    init_graph["b"]["e"] = 10

    #Major Thirds    
    init_graph["c"]["e"] = 9
    init_graph["cis"]["f"] = 9
    init_graph["d"]["fis"] = 9
    init_graph["dis"]["g"] =9
    init_graph["e"]["gis"] =9
    init_graph["f"]["a"] =9
    init_graph["fis"]["ais"] =9
    init_graph["g"]["b"] =9
    init_graph["gis"]["c"] =9
    init_graph["a"]["cis"] =9
    init_graph["ais"]["d"] =9
    init_graph["b"]["dis"] =9

    #Minor thirds up
    init_graph["c"]["dis"] = 8
    init_graph["cis"]["e"] = 8
    init_graph["d"]["f"] = 8
    init_graph["dis"]["fis"] = 8
    init_graph["e"]["g"] = 8
    init_graph["f"]["gis"] = 8
    init_graph["fis"]["a"] = 8
    init_graph["g"]["ais"] = 8
    init_graph["gis"]["b"] = 8
    init_graph["a"]["c"] = 8
    init_graph["ais"]["cis"] = 8
    init_graph["b"]["d"] = 8

    #major 6th up
    init_graph["c"]["a"] = 7
    init_graph["cis"]["ais"] = 7
    init_graph["d"]["b"] = 7
    init_graph["dis"]["c"] = 7
    init_graph["e"]["cis"] = 7
    init_graph["f"]["d"] = 7
    init_graph["fis"]["dis"] = 7
    init_graph["g"]["e"] = 7
    init_graph["gis"]["f"] = 7
    init_graph["a"]["fis"] = 7
    init_graph["ais"]["g"] = 7
    init_graph["b"]["gis"] = 7
    
    #minor 6th up
    init_graph["c"]["gis"] = 6
    init_graph["cis"]["a"] = 6
    init_graph["d"]["ais"] = 6
    init_graph["dis"]["b"] = 6
    init_graph["e"]["c"] = 6
    init_graph["f"]["cis"] = 6
    init_graph["fis"]["d"] = 6
    init_graph["g"]["dis"] = 6
    init_graph["gis"]["e"] = 6
    init_graph["a"]["f"] = 6
    init_graph["ais"]["fis"] = 6
    init_graph["b"]["g"] = 6

    #Major second up
    init_graph["c"]["d"] = 5
    init_graph["cis"]["dis"] = 5
    init_graph["d"]["e"] = 5
    init_graph["dis"]["f"] = 5
    init_graph["e"]["fis"] = 5
    init_graph["f"]["g"] = 5
    init_graph["fis"]["gis"] = 5
    init_graph["g"]["a"] = 5
    init_graph["gis"]["ais"] = 5
    init_graph["a"]["b"] = 5
    init_graph["ais"]["c"] = 5
    init_graph["b"]["cis"] = 5

     #minor 7th up
    init_graph["c"]["ais"] = 4
    init_graph["cis"]["b"] = 4
    init_graph["d"]["c"] = 4
    init_graph["dis"]["cis"] = 4
    init_graph["e"]["d"] = 4
    init_graph["f"]["dis"] = 4
    init_graph["fis"]["e"] = 4
    init_graph["g"]["f"] = 4
    init_graph["gis"]["fis"] = 4
    init_graph["a"]["g"] = 4
    init_graph["ais"]["gis"] = 4
    init_graph["b"]["a"] = 4

    #major 7th up
    init_graph["c"]["b"] = 3
    init_graph["cis"]["c"] = 3
    init_graph["d"]["cis"] = 3
    init_graph["dis"]["d"] = 3
    init_graph["e"]["dis"] = 3
    init_graph["f"]["e"] = 3
    init_graph["fis"]["f"] = 3
    init_graph["g"]["fis"] = 3
    init_graph["gis"]["g"] = 3
    init_graph["a"]["gis"] = 3
    init_graph["ais"]["a"] = 3
    init_graph["b"]["ais"] = 3
    
    #a4 up
    init_graph["c"]["fis"] = 2
    init_graph["cis"]["g"] = 2
    init_graph["d"]["gis"] = 2
    init_graph["dis"]["a"] = 2
    init_graph["e"]["ais"] = 2
    init_graph["f"]["b"] = 2
    init_graph["fis"]["c"] = 2
    init_graph["g"]["cis"] = 2
    init_graph["gis"]["d"] = 2
    init_graph["a"]["dis"] = 2
    init_graph["ais"]["e"] = 2
    init_graph["b"]["f"] = 2

    #Minor second up
    init_graph["c"]["cis"] = 1
    init_graph["cis"]["d"] = 1
    init_graph["d"]["dis"] = 1
    init_graph["dis"]["e"] = 1
    init_graph["e"]["f"] = 1
    init_graph["f"]["fis"] = 1
    init_graph["fis"]["g"] = 1
    init_graph["g"]["gis"] = 1
    init_graph["gis"]["a"] = 1
    init_graph["a"]["ais"] = 1
    init_graph["ais"]["b"] = 1
    init_graph["b"]["c"] = 1

    graph = Graph(nodes, init_graph)
    
    nextNote=startNote
    new_graph=[startNote]
    for i in range(1, length):

        print(init_graph[nextNote])
        sub_graph={}
        for item in (init_graph[nextNote]):
            if quality=="g":
                if init_graph[nextNote][item]>=6:
                    sub_graph[item]=init_graph[nextNote][item]
            if quality=="b":
                if init_graph[nextNote][item]<=5:
                    sub_graph[item]=init_graph[nextNote][item]
        len_notes=(len(sub_graph))

        print(len_notes)
        random_sample_numbers=(random.sample(range(0,len_notes),1))
        print(random_sample_numbers)
        print("choices ", sub_graph)
        for number in random_sample_numbers:
            nextNote=list(sub_graph)[number]
            print(f"{number}: {nextNote}")
            new_graph.append(nextNote)

    print(f"New Array: {new_graph}")

    result=" ".join(new_graph)

    myFile='drizzyMusic'

    myMusic=result

    myLyrics=result

    multiLines = """  
\\version "2.14.2"

music = \\relative c'' {{
\\time 7/4
{music}
}}

\\addlyrics {{
{lyrics}
}}

\\score {{
\\music
\\layout {{}}
\\midi {{}}
}}

 """.format(lyrics=myLyrics, music=myMusic)

    print(multiLines)

    with open("{file}.ly".format(file=myFile), "w") as file1:
        # Writing data to a file
        file1.writelines(multiLines)

    print('Created {file}.ly\n'.format(file=myFile) )

    p1 = subprocess.Popen('lilypond {file}.ly'.format(file=myFile),shell=True)
    p1.wait()
    pdf=subprocess.Popen('open {file}.pdf'.format(file=myFile),shell=True)
    pdf.wait()
    subprocess.Popen('timidity -Od {file}.midi'.format(file=myFile),shell=True)
