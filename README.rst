glm_pp
======

`GDB pretty-printers`__ for GLM_.

.. __: https://sourceware.org/gdb/current/onlinedocs/gdb/Pretty-Printing.html
.. _GLM: http://glm.g-truc.net/

User setup:

* install ``glm_pp.py`` to an appropriate directory

* add the contents of ``gdbinit`` to ``~/.gdbinit``, replacing ``.../glm_pp``
  with that directory

System setup:

* ``# make install`` (installs to the system GDB Python directory)

* add ``python import glm_pp`` to ``~/.gdbinit``

Run ``make -C test`` for an example.
