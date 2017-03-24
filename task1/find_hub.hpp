#include <iostream>
#include <vector>
#include <utility>
#include <iterator>
#include <cstdlib>
#include <limits>
#include <cerrno>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/graph_traits.hpp>
#include <boost/graph/graph_concepts.hpp>
#include <boost/concept_check.hpp>
#include <boost/operators.hpp>
#include <boost/iterator.hpp>
#include <boost/multi_array.hpp>
#include <boost/random.hpp>
#include "edmonds_optimum_branching.hpp"

//#define DEBUG

using namespace std;
using namespace boost;

struct Line {
    unsigned int from, to, price;

    Line(unsigned int from, unsigned int to, unsigned int price) : from(from), to(to), price(price) {};
};

struct Result {
    bool feasibility;
    unsigned int total_cost;
    unsigned int depot_id;
    std::vector<Line> rec_offers;
};

class GraphProcessor {
public:
    bool load_input();
    void find_hub();
    void send_result();

private:
    Result last_res;
    int cities_cnt;
    std::vector<Line> lines;
};

// definitions of a complete graph that implements the EdgeListGraph
// concept of Boost's graph library.
namespace boost {
    struct complete_graph {
        complete_graph(int n_vertices) : n_vertices(n_vertices) {}
        int n_vertices;

        struct edge_iterator : public input_iterator_helper<edge_iterator, int, std::ptrdiff_t, int const *, int>
        {
            int edge_idx, n_vertices;

            edge_iterator() : edge_idx(0), n_vertices(-1) {}
            edge_iterator(int n_vertices, int edge_idx) : edge_idx(edge_idx), n_vertices(n_vertices) {}
            edge_iterator &operator++()
            {
                if (edge_idx >= n_vertices * n_vertices)
                    return *this;
                ++edge_idx;
                if (edge_idx / n_vertices == edge_idx % n_vertices)
                    ++edge_idx;
                return *this;
            }
            int operator*() const {return edge_idx;}
            bool operator==(const edge_iterator &iter) const
            {
                return edge_idx == iter.edge_idx;
            }
        };
    };

    template<>
    struct graph_traits<complete_graph> {
        typedef int                             vertex_descriptor;
        typedef int                             edge_descriptor;
        typedef directed_tag                    directed_category;
        typedef disallow_parallel_edge_tag      edge_parallel_category;
        typedef edge_list_graph_tag             traversal_category;
        typedef complete_graph::edge_iterator   edge_iterator;
        typedef unsigned                        edges_size_type;

        static vertex_descriptor null_vertex() {return -1;}
    };

    pair<complete_graph::edge_iterator, complete_graph::edge_iterator>
    edges(const complete_graph &g)
    {
        return make_pair(complete_graph::edge_iterator(g.n_vertices, 1),
                         complete_graph::edge_iterator(g.n_vertices, g.n_vertices*g.n_vertices));
    }

    unsigned
    num_edges(const complete_graph &g)
    {
        return (g.n_vertices - 1) * (g.n_vertices - 1);
    }

    int
    source(int edge, const complete_graph &g)
    {
        return edge / g.n_vertices;
    }

    int
    target(int edge, const complete_graph &g)
    {
        return edge % g.n_vertices;
    }
}

typedef graph_traits<complete_graph>::edge_descriptor Edge;
typedef graph_traits<complete_graph>::vertex_descriptor Vertex;
