/* 有 N 个网络节点，标记为 1 到 N。

给定一个列表 times，表示信号经过有向边的传递时间。 times[i] = (u, v, w)，其中 u 是源节点，v 是目标节点， w 是一个信号从源节点传递到目标节点的时间。

现在，我们向当前的节点 K 发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1。

注意:

N 的范围在 [1, 100] 之间。
K 的范围在 [1, N] 之间。
times 的长度在 [1, 6000] 之间。 */

/* 这道题给了我们一些有向边，又给了一个结点K，问至少需要多少时间才能从K到达任何一个结点。这实际上是一个有向图求最短路径的问题，我们求出K点到每一个点到最短路径，然后取其中最大的一个就是需要的时间了。可以想成从结点K开始有水流向周围扩散，当水流到达最远的一个结点时，那么其他所有的结点一定已经流过水了。最短路径的常用解法有迪杰克斯特拉算法Dijkstra Algorithm, 弗洛伊德算法Floyd-Warshall Algorithm, 和贝尔曼福特算法Bellman-Ford Algorithm，其中，Floyd算法是多源最短路径，即求任意点到任意点到最短路径，而Dijkstra算法和Bellman-Ford算法是单源最短路径，即单个点到任意点到最短路径。这里因为起点只有一个K，所以使用单源最短路径就行了。这三种算法还有一点不同，就是Dijkstra算法处理有向权重图时，权重必须为正，而另外两种可以处理负权重有向图，但是不能出现负环，所谓负环，就是权重均为负的环。为啥呢，这里要先引入松弛操作Relaxtion，这是这三个算法的核心思想，当有对边 (u, v) 是结点u到结点v，如果 dist(v) > dist(u) + w(u, v)，那么 dist(v) 就可以被更新，这是所有这些的算法的核心操作。Dijkstra算法是以起点为中心，向外层层扩展，直到扩展到终点为止。根据这特性，用BFS来实现时再好不过了，注意while循环里的第一层for循环，这保证了每一层的结点先被处理完，才会进入进入下一层，这种特性在用BFS遍历迷宫统计步数的时候很重要。对于每一个结点，我们都跟其周围的结点进行Relaxtion操作，从而更新周围结点的距离值。为了防止重复比较，我们需要使用visited数组来记录已访问过的结点，最后我们在所有的最小路径中选最大的返回，注意，如果结果res为INT_MAX，说明有些结点是无法到达的，返回-1。普通的实现方法的时间复杂度为O(V2)，基于优先队列的实现方法的时间复杂度为O(E + VlogV)，其中V和E分别为结点和边的个数，这里多说一句，Dijkstra算法这种类贪心算法的机制，使得其无法处理有负权重的最短距离，还好这道题的权重都是正数 */

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        int res = 0;
        vector<vector<int>> edges(101, vector<int>(101, -1));
        queue<int> q{{K}};
        vector<int> dist(N + 1, INT_MAX);
        dist[K] = 0;
        for (auto e : times) edges[e[0]][e[1]] = e[2];
        while (!q.empty()) {
            unordered_set<int> visited;
            for (int i = q.size(); i > 0; --i) {
                int u = q.front(); q.pop();
                for (int v = 1; v <= 100; ++v) {
                    if (edges[u][v] != -1 && dist[u] + edges[u][v] < dist[v]) {
                        if (!visited.count(v)) {
                            visited.insert(v);
                            q.push(v);
                        }
                        dist[v] = dist[u] + edges[u][v];
                    }
                }
            }
        }
        for (int i = 1; i <= N; ++i) {
            res = max(res, dist[i]);
        }
        return res == INT_MAX ? -1 : res;
    }
};

/* 下面来看基于Bellman-Ford算法的解法，时间复杂度是O(VE)，V和E分别是结点和边的个数。这种算法是基于DP来求全局最优解，原理是对图进行V-1次松弛操作，这里的V是所有结点的个数（为啥是V-1次呢，因为最短路径最多只有V-1条边，所以只需循环V-1次），在重复计算中，使得每个结点的距离被不停的更新，直到获得最小的距离，这种设计方法融合了暴力搜索之美，写法简洁又不失优雅。之前提到了，Bellman-Ford算法可以处理负权重的情况，但是不能有负环存在，一般形式的写法中最后一部分是检测负环的，如果存在负环则报错。不能有负环原因是，每转一圈，权重和都在减小，可以无限转，那么最后的最小距离都是负无穷，无意义了。没有负环的话，V-1次循环后各点的最小距离应该已经收敛了，所以在检测负环时，就再循环一次，如果最小距离还能更新的话，就说明存在负环。这道题由于不存在负权重，所以就不检测了，参见代码如下： */

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int N, int K) {
        int res = 0;
        vector<int> dist(N + 1, INT_MAX);
        dist[k] = 0;
        for (int i = 1; i < N; ++i) {
            for (auto e : times) {
                int u = e[0], v = e[1], w = e[2];
                if (dist[u] != INT_MAX && dist[v] > dist[u] + w) {
                    dist[v] = dist[u] + w;
                }
            }
        }
        for (int i = 1; i <= N; ++i) {
            res = max(res, dist[i]);
        }
        return res == INT_MAX ? -1 : res;
    }
};

/* 最后，再来说说这个Floyd算法，这也是一种经典的动态规划算法，目的是要找结点i到结点j的最短路径。而结点i到结点j的走法就两种可能，一种是直接从结点i到结点j，另一种是经过若干个结点k到达结点j。所以对于每个中间结点k，我们检查dist(i, k) + dist(k, j) < dist(i, j) 是否成立，成立的话就松弛它，这样遍历完所有的结点k，dist(i,j)中就是结点i到结点j的最短距离了。时间复杂度是O(V3)，处处透露着暴力美学。除了这三种算法外，还有一些很类似的优化算法，比如Bellman-Ford的优化算法-SPFA算法，还有融合了Bellman-Ford和Dijkstra算法的高效的多源最短路径算法-Johnson算法 */


*/