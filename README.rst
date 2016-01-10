glm_pp
======

`GDB pretty-printers`__ for GLM_.

.. __: https://sourceware.org/gdb/current/onlinedocs/gdb/Pretty-Printing.html
.. _GLM: http://glm.g-truc.net/

Before::

    (gdb) p pos
    $1 = {{x = 5, r = 5, s = 5}, {y = 6, g = 6, t = 6}, {z = 7, b = 7, p = 7}}

After::

    (gdb) p pos
    $1 = ivec3(5, 6, 7)

User setup:

* install ``glm_pp.py`` to any directory

* add the contents of ``gdbinit`` to ``~/.gdbinit``, replacing ``.../glm_pp``
  with that directory

System setup:

* ``# make install`` (installs to the system GDB Python directory)

* add ``python import glm_pp`` to ``~/.gdbinit``

Run ``make -C test`` for an example.
