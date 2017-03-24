#include "find_hub.hpp"

void GraphProcessor::find_hub()
{
    struct Result res = {};

    complete_graph      g(cities_cnt);
    multi_array<int, 2> weights(extents[cities_cnt][cities_cnt]);
    Vertex              roots[] = {0, 1, 2, 3};
    vector<Edge>        branching;

    for (auto it = lines.begin(); it != lines.end(); ++it) {
        weights[it->from][it->to] = it->price;
    }

    edmonds_optimum_branching<false, true, true>
            (g, identity_property_map(), weights.origin(),
             roots, roots, back_inserter(branching));

#ifdef DEBUG
    BOOST_FOREACH (Edge e, branching)
        std::cout << source(e, g) << " -> " << target(e, g) << " : " << weights[source(e, g)][target(e, g)] << std::endl;
#endif

    res.feasibility = branching.empty() ? false : true;
    for (auto& e : branching)
        res.total_cost += weights[source(e, g)][target(e, g)];
    res.depot_id = INT_MAX;

    BOOST_FOREACH (Edge e, branching)
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
