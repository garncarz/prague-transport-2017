#include "find_hub.hpp"

void GraphProcessor::find_hub()
{
    struct Result res = {};

    complete_graph      g(cities_cnt);
    multi_array<int, 2> weights(extents[cities_cnt][cities_cnt]);
    Vertex              roots[] = {0, 1, 2, 3};
    vector<Edge>        branching;

    weights[0][1] = 6;
    weights[1][2] = 10;
    weights[2][1] = 10;
    weights[1][3] = 12;
    weights[3][2] = 8;
    weights[3][0] = 1;

    edmonds_optimum_branching<false, true, true>
            (g, identity_property_map(), weights.origin(),
             roots, roots, back_inserter(branching));

    BOOST_FOREACH (Edge e, branching)
    {
        std::cout << source(e, g) << " -> " << target(e, g) << std::endl;
    }

    last_res = res;
}

void GraphProcessor::load_input()
{
    cities_cnt = 4;
    lines.push_back(Line(0, 1, 6));
    lines.push_back(Line(1, 2, 10));
    lines.push_back(Line(2, 1, 10));
    lines.push_back(Line(1, 3, 12));
    lines.push_back(Line(3, 2, 8));
    lines.push_back(Line(3, 0, 1));
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

    gp.load_input();
    gp.find_hub();
    //gp.send_result();

    return 0;
}
