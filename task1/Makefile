all: find_hub

find_hub.o: find_hub.cc find_hub.hpp
	g++ -Wall -c find_hub.cc

find_hub: find_hub.o
	g++ -Wall find_hub.o -o find_hub

test_lite: find_hub
	cat simple_in.txt | ./find_hub
