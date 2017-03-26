#include "find_hub.hpp"

void GraphProcessor::find_hub()
{
    struct Result res = {};

    complete_graph      g(cities_cnt);
    multi_array<int, 2> weights(extents[cities_cnt][cities_cnt]);
    Vertex              roots[cities_cnt];
    vector<Edge>        branching;

    int n = {0};
    std::generate(roots, roots + cities_cnt, [&n] { return n++; } );

    int *end = weights.origin() + cities_cnt * cities_cnt;
    for (int *it = weights.origin(); it != end; ++it)
        *it = INT_MAX;

    for (auto it = lines.begin(); it != lines.end(); ++it) {
        weights[it->from][it->to] = it->price;
    }

    unsigned long min_cost = ULONG_MAX;
    unsigned int best_depot = INT_MAX;
    vector<Edge> best_branching;

    for (int r = 0; r < cities_cnt; r++) {
        branching.clear();

        edmonds_optimum_branching<false, true, true>
            (g, identity_property_map(), weights.origin(),
             roots + r, roots + r + 1, back_inserter(branching));

        unsigned long total_cost = 0;
        for (auto& e : branching)
             total_cost += weights[source(e, g)][target(e, g)];

        #ifdef DEBUG
            std::cout << "root: " << r << std::endl;
            BOOST_FOREACH (Edge e, branching)
                 std::cout << source(e, g) << " -> " << target(e, g) << " : " << weights[source(e, g)][target(e, g)] << std::endl;
            std::cout << total_cost << std::endl;
        #endif

        if (total_cost < min_cost) {
            min_cost = total_cost;
            best_depot = r;
            best_branching = branching;
        }
    }

    res.feasibility = best_branching.empty() ? false : true;
    res.total_cost = min_cost;
    res.depot_id = best_depot;

    BOOST_FOREACH (Edge e, best_branching)
        res.rec_offers.push_back(Line(source(e, g), target(e, g), weights[source(e, g)][target(e, g)]));

    last_res = res;
}

bool GraphProcessor::load_input()
{
    if (!(std::cin >> cities_cnt))
        return false;

    unsigned int from, to, price;

    while (cin >> from >> to >> price)
        lines.push_back(Line(from, to, price));

    return true;
}

void GraphProcessor::send_result()
{
    std::cout << last_res.feasibility << " " << last_res.total_cost << " " << last_res.depot_id << std::endl;

    for (auto it = last_res.rec_offers.begin(); it != last_res.rec_offers.end(); ++it) {
        std::cout << it->from << " " << it->to << " " << it->price << std::endl;
    }
}

int main(int argc, char *argv[])
{
    GraphProcessor gp;

    if (!gp.load_input())
        return 1;
    gp.find_hub();
    gp.send_result();

    return 0;
}
