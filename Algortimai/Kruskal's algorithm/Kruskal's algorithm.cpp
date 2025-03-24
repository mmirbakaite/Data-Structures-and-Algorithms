// Kruskalio algortimas

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

#define edge pair <int, int>

class Graph {
private:
    vector<pair<int, edge> > G;  // grafas
    vector<pair<int, edge> > T;  // minamalus medis
    int* parent;
    int V;                       // krastiniu kiekis
public:
    Graph(int V);
    void AddWeightedEdge(int u, int v, int w);
    int  findset(int i);
    void unionset(int u, int v);
    void kruskal();
    void print();
};

// pradiniai duomenys Krusklaio algoritmui
Graph::Graph(int V) {
    parent = new int[V];
    for (int i = 0; i < V; i++)
        parent[i] = i;

    G.clear();
    T.clear();
}

// prideda svorinæ briaunà prie grafo
void Graph::AddWeightedEdge(int u, int v, int w) {
    G.push_back(make_pair(w, edge(u, v)));
}

// tikrina, kuriam aibës elementui priklauso konkretus mazgas
int Graph::findset(int i) {
    if (i == parent[i])
        return i;
    else
        return findset(parent[i]);
}

// sujungiami aibes elementai
void Graph::unionset(int u, int v) {
    parent[u] = parent[v];
}

// jungia visas grafo virðûnes su minimaliais svoriais
void Graph::kruskal() {
    int i, uRep, vRep;
    sort(G.begin(), G.end());     // svorio padidejimas
    for (i = 0; i < G.size(); i++) {
        uRep = findset(G[i].second.first);
        vRep = findset(G[i].second.second);
        if (uRep != vRep) {
            T.push_back(G[i]);    // pridejimas prie medzio
            unionset(uRep, vRep);
        }
    }
}

// isspausdina gauta minamalaus jungimosi medi
void Graph::print() {
    cout << "Briauna :"
        << " Svoris" << endl;
    for (int i = 0; i < T.size(); i++) {
        cout << T[i].second.first << " - " << T[i].second.second << " : "
            << T[i].first;
        cout << endl;
    }
}

int main() {
    Graph g(3);
    g.AddWeightedEdge(0, 1, 4);
    g.AddWeightedEdge(0, 2, 3);
    g.AddWeightedEdge(1, 2, 2);
    /*
    g.AddWeightedEdge(1, 0, 4);
    g.AddWeightedEdge(2, 0, 4);
    g.AddWeightedEdge(2, 1, 2);
    g.AddWeightedEdge(2, 3, 3);
    g.AddWeightedEdge(2, 5, 2);
    g.AddWeightedEdge(2, 4, 4);
    g.AddWeightedEdge(3, 2, 3);
    g.AddWeightedEdge(3, 4, 3);
    g.AddWeightedEdge(4, 2, 4);
    g.AddWeightedEdge(4, 3, 3);
    g.AddWeightedEdge(5, 2, 2);
    g.AddWeightedEdge(5, 4, 3);
    */
    g.kruskal();
    g.print();
    return 0;
}
