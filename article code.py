import string

from vocabulary import Digraph, Word, Edge

graph=Digraph()
with open('article')as f:
    previous_word=None
    for i,line in enumerate(f):
        table = str.maketrans(dict.fromkeys(string.punctuation))
        line = line.translate(table)
        for w,word in enumerate(line.split()):
            print(i,w,word)
            node=graph.add_node(Word(word.lower(),(i,w)))
            if previous_word:
                graph.add_edge(Edge(previous_word,node))
            previous_word=node
    f.close()
print (graph)

