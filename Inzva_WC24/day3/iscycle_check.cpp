 //^ complexity is 
bool isCycleUndirected(int u, int p)  {
    vis[u] = true;
    bool isCycle = false;
    for ( auto v : adjList[u] ) {
        if ( v == p ) continue;
        
        if ( vis[v] ) isCycle = true;
        isCycle |= isCycleUndirected(v, u);
    }
    return isCycle;
}

//* directed için visited parametresini visited ve finished olarak tutuyoruz(0,1 yerine 0,1(visited),2(finished))
//* finished bir noda geldiysek sorun yok ama unfinished ama visited bir noda denk gelirsek cycle var demek