GRAPH = {}

# ----------- Data Processing -----------
def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.readlines(chunk_size)
        if not data:
            break
        yield data

def construct_graph(line):
    vertex = line.split(' ')[0]
    head = line.split(' ')[1]
    if vertex in GRAPH:
        GRAPH[vertex].append(head)
    else:
        GRAPH[vertex] = [head]


f = open('SCC.txt')
for piece in read_in_chunks(f):
    for line in piece:
        construct_graph(line)
