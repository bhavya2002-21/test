#include <iostream>
#include <list>
#include <stdio.h>
using namespace std;

class Graph
{
	int V;
	list<int> *adj;
public:
	Graph(int V) { this->V = V; adj = new list<int>[V]; }
	~Graph()	 { delete [] adj; }
	void addEdge(int v, int w);
	void Coloring();
};

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
	adj[w].push_back(v); 
}

void Graph::Coloring()
{
	int result[V];
	result[0] = 0;
	for (int u = 1; u < V; u++)
		result[u] = -1; 
	bool available[V];
	for (int cr = 0; cr < V; cr++)
		available[cr] = false;
	for (int u = 1; u < V; u++)
	{
		list<int>::iterator i;
		for (i = adj[u].begin(); i != adj[u].end(); ++i)
			if (result[*i] != -1)
				available[result[*i]] = true;
		int cr;
		for (cr = 0; cr < V; cr++)
			if (available[cr] == false)
				break;
		result[u] = cr;
		for (i = adj[u].begin(); i != adj[u].end(); ++i)
			if (result[*i] != -1)
				available[result[*i]] = false;
	}
	const char* colour[3]= { "Red", "Green", "Blue" };
	for (int u = 0; u < V; u++)
		cout << "Vertex " << u << " ---> Color "<< colour[result[u]] << endl;
}

int main()
{
	Graph g(7);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 2);
	g.addEdge(1, 3);
	g.addEdge(2, 3);
	g.addEdge(2, 4);
	g.addEdge(2, 5);
	g.addEdge(3, 4);
	g.addEdge(4, 5);
	
	cout << "Coloring of graph\n";
	g.Coloring();
	
	return 0;
}