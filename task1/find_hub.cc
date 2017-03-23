#include <iostream>
#include <vector>
#include "find_hub.hpp"

struct Result find_hub(int cities_count, int offers_count, struct Offer *offers)
{
    struct Result res;

    std::cout << offers_count << std::endl;

    return res;
}

int main(int argc, char *argv[])
{
    int cities_cnt = 4;
    struct Offer offers[] = {
                            {0, 1, 6},
                            {1, 2, 10},
                            {2, 1, 10},
                            {1, 3, 12},
                            {3, 2, 8},
                            {3, 0, 1}
                        };
    struct Result res;

    res = find_hub(cities_cnt, sizeof(offers)/sizeof(struct Offer), offers);

    return 0;
}
