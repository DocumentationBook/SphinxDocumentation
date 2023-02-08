.. _concepts_sphinx_process:

Operations
##########

Let us walk through the documentation build process in the hierarchical order from top to bottom.
Since the total process can contain hundreds of thousands calls, this journey presents
only the most important ones for a better understanding of this process.

.. toctree::
   :hidden:

   top
   app
   phases

As the process highly depends on the set of documents, we will take a simple structure::

   ├── index.rst
   ├── folder1
   │     └── index.rst
   ├── folder2
         └── index.rst


All the documentation files a very simple ones containing only text with a couple of sections.

The process is started with the following command::

   $ rm -rf _build; sphinx-build -b dirhtml "." "_build" -C
