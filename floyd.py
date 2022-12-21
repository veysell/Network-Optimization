class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m' #sarı
    FAIL = '\033[91m' #kırmızı
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
class Graph:
    def __init__(self):
        # dictionary containing keys that map to the corresponding vertex object
        self.vertices = {}
 
    def add_vertex(self, key):
        """Add a vertex with the given key to the graph."""
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    def get_vertex(self, key):
        """Return vertex object with the corresponding key."""
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    def add_edge(self, src_key, dest_key, weight=1):
        """Add edge from src_key to dest_key with given weight."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)
 
    def does_edge_exist(self, src_key, dest_key):
        """Return True if there is an edge from src_key to dest_key."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])
 
    def __len__(self):
        return len(self.vertices)
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    def get_key(self):
        """Return key corresponding to this vertex object."""
        return self.key
 
    def add_neighbour(self, dest, weight):
        """Make this vertex point to dest with given edge weight."""
        self.points_to[dest] = weight
 
    def get_neighbours(self):
        """Return all vertices pointed to by this vertex."""
        return self.points_to.keys()
 
    def get_weight(self, dest):
        """Get weight of edge from this vertex to dest."""
        return self.points_to[dest]
 
    def does_it_point_to(self, dest):
        """Return True if this vertex points to dest."""
        return dest in self.points_to
 
 
def floyd_warshall(g):

    distance = {v:dict.fromkeys(g, float('inf')) for v in g}
    next_v = {v:dict.fromkeys(g, None) for v in g}
 
    for v in g:
        for n in v.get_neighbours():
            distance[v][n] = v.get_weight(n)
            next_v[v][n] = n
 
    for v in g:
         distance[v][v] = 0
         next_v[v][v] = None
 
    for p in g: 
        for v in g:
            for w in g:
                if distance[v][w] > distance[v][p] + distance[p][w]:
                    distance[v][w] = distance[v][p] + distance[p][w]
                    next_v[v][w] = next_v[v][p]
 
    return distance, next_v
 
 
def print_path(next_v, u, v):
    p = u
    while (next_v[p][v]):
        print('{} -> '.format(vertex_no[p.get_key()]), end='')

        p = next_v[p][v]
    print('{} '.format(vertex_no[v.get_key()]), end='')

def print_all_path():
    distance, next_v = floyd_warshall(g)
    print('Shortest distances:')
    for start in g:
        for end in g:
            if next_v[start][end]:
                print('From {} to {}: '.format(start.get_key(),
                                                end.get_key()),
                        end = '')
                print_path(next_v, start, end)
                print('(distance {} KM)'.format(distance[start][end]))

g = Graph()

vertex_no={"1":"İstanbul","2":"Edirne","3":"Kırklareli","4":"Tekirdağ","5":"Çanakkale","6":"Kocaeli","7":"Yalova","8":"Sakarya","9":"Bilecik","10":"Bursa","11":"Balıkesir"}
vertex=     ["1",       "2",        "3",        "4",        "5",        "6",    "7",    "8",        "9",    "10",   "11"]
for key in vertex:
    g.add_vertex(key)

edges=[ # vertex_no ya tanımlanan yollar arası maliyetler aşağıya girilecek
#eğer iki node arasında yol yoksa yazmana gerek yok, 1-1 gibi kendine dönenler için yol varsa maliyetini yoksa 0 yaz 
    ["1","1",0],["1","2",252.4],["1","3",209],["1","4",159.3],["1","6",103.9],
    ["2","1",252.4],["2","2",0],["2","3",65.5],["2","4",143.2],["2","5",230.2],
    ["3","1",209],["3","2",65.5],["3","3",0],["3","4",117.5],
    ["4","1",159.3],["4","2",143.2],["4","3",117.5],["4","4",0],["4","5",159.7],
    ["5","2",230.2],["5","4",159.7],["5","5",0],["5","11",192.4],
    ["6","1",103.9],["6","6",0],["6","7",71.8],["6","8",51.8],["6","10",132.5],
    ["7","6",71.8],["7","7",0],["7","10",74.4],
    ["8","6",51.8],["8","8",0],["8","9",107.4],["8","10",182.7],
    ["9","8",107.4],["9","9",0],["9","10",105.2],
    ["10","6",132.5],["10","7",76.4],["10","8",182.7],["10","9",105.2],["10","10",0],["10","11",147.8],
    ["11","5",192.4],["11","10",147.8],["11","11",0]
    ]
    
for s,d,w in edges:
    g.add_edge(s, d, w)

distance, next_v = floyd_warshall(g)




#burdan aşağısı while mantığı kafanıza göre takılın kolay gelsin
bool=0
isBool="T"
while(isBool.upper()=="T"):
    print("-"*100)
    print(" "*25,bcolors.HEADER,bcolors.BOLD,"Marmara Bölgesi Afet Yönetim Programı")
    print()
    print(bcolors.WARNING,"Arama yapılabilecek şehirler: (NOT: Şehir isimleri yerine sayı yazarak pratik arama yapın!!!)")
    print()
    for i,j in vertex_no.items():
        print(bcolors.OKGREEN," "*10,f'{i}--------->{j}')
    print()
    start_node=input("Yardım edecek afet birimini giriniz: ")
    end_node=input("Yardım ulaştırılacak afet bölgesini giriniz: ")
    for i in range(0,8):
        if(i==4):
            print("Yol Hesaplanıyor")
        else:
            print(bcolors.OKBLUE," "*10,".")
    print()
    print(bcolors.OKCYAN,"Yardımı aşağıdaki güzergah üzerinden ulaştırmanızı tavsiye ediyoruz.",end="\n\n")
    for start in g:
        for end in g:
            if next_v[start][end]:
                if start_node==start.get_key() and end_node==end.get_key():
                    bool=1
                    print(' {} --> {}: '.format(vertex_no[start.get_key()],
                                                    vertex_no[end.get_key()]),
                            end = '')
                    print_path(next_v, start, end)
                    print('(Mesafe {})'.format(distance[start][end]))
    
    print()
    print(bcolors.FAIL,"Tekrar arama yapmak için T, çıkmak için herhangi bir tuşa basınız: ",end="")
    isBool=input("")



