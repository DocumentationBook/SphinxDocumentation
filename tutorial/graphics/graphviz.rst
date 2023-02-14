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
can install it from its source using a universal procedure. For example, on Mac, you can install it using this way::

   $ brew install graphviz

The Graphviz Python package is a built-in Sphinx extension, so you don't need to install its Python package.
However, you need to add it to the list of extensions in the ``conf.py`` file::

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


Using hyperlinks
================

When creating several documents bound by the same idea, you will probably need to bind graph images as well.
To make a reference from an image created by Graphviz, follow this way:

#. Make the Graphviz to output images in the CSV format instead of the default PNG.
   To do this, add the following option to the ``conf.py`` file::

      graphviz_output_format = 'svg'

#. In the Graphviz element where you want to add a link, use the ``href`` attribute to add a URL or a local path,
   for example:

   *  Using full URL::

         href="https://google.com"

   *  Using a local path that is usually a relative path from the folder (usually ``_images/``), where Sphinx stores
      all processed images, to the target document::

         href="../research/sphinx/read/"

#. Add the HTML ``target`` attribute set to ``_top`` to open the linked document in the current HTML window
   or ``_blank`` to open it on a new tab in your browser.
   This is a Graphviz node example::

      "read" [label=<<b>READING</b>> fillcolor=cadetblue4 fontcolor=white href="../read/" target=_top]
