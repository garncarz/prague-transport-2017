all: compute_hub

find_hub.o: find_hub.cc find_hub.hpp
	g++ -Wall -c find_hub.cc

compute_hub: find_hub.o
	g++ -Wall compute_hub.cc find_hub.o -o compute_hub
