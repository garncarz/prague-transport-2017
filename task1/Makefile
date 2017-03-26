CXX=g++-6

all: find_hub

find_hub.o: find_hub.cc find_hub.hpp
	$(CXX) -Wall -c find_hub.cc

find_hub: find_hub.o
	$(CXX) -Wall find_hub.o -o find_hub

test_lite: find_hub
	$(CXX) simple_in.txt | ./find_hub
