all: find_hub

find_hub: find_hub.cc find_hub.hpp
	g++ -Wall -c find_hub.cc
