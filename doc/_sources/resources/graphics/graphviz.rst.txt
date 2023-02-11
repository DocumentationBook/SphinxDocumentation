.. _resources_graphics_graphviz:

Graphviz
########

`Graphiz <https://www.graphviz.org/>`_  is an open source universal graph visualization tool. Engineers and
developers use it to create graphs manually or programmatically.


Setup
=====

Graphviz is a `C package <https://gitlab.com/graphviz/graphviz/>`_ that must be installed on your computer before you
can use it to build graphs manually, with Sphinx, or with other applications.
There are `building instructions <https://graphviz.org/doc/build.html>`_ specific for different platforms or you
or you can install it from its source using a universal procedure. For example, on Mac, you can install in this way::

   $ brew install graphviz

Graphviz is a built-in Sphinx extension, so you don't need to install its Python package. However, you need to add it
to the list of extensions in the ``conf.py`` file::

   extensions = [
      'sphinx.ext.graphviz',
   ]

To test if it works, try the following simplest example in a reST file::

   .. graphviz::

      digraph foo {
         "bar" -> "baz";
      }

After building the documentation, you will get the following graph:

.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }
