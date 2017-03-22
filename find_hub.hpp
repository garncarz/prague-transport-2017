struct Offer {
    unsigned int from, to, price;
};

struct Result {
    bool feasibility;
    unsigned int total_cost;
    unsigned int depot_id;
    unsigned int recommended_offers_num;
    struct Offer *recommended_offers;

    Result() : recommended_offers_num(0), recommended_offers(NULL) {}
    ~Result() {::free(recommended_offers); }
};

typedef struct Offer Conn;

struct Result find_hub(int cities_count, int offers_count, struct Offer *offers);
