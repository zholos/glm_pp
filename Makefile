all:

DIR != gdb -batch -ex 'python print os.path.dirname(os.path.dirname(gdb.__file__))'
install:
	install -m 0644 glm_pp.py '$(DIR)'
