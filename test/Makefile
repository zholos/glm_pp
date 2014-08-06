run: test
	gdb -batch -n -x script test

test: test.cc
	g++ -I/usr/local/include -O0 -g -o $@ $<

clean:
	rm -f test
