.. _concepts_sphinx_process:

Operations
##########

Let us walk through the documentation build process in the hierarchical order from top to bottom.

.. toctree::
   :hidden:

   top

As the process highly depends on the set of documents, we will take a simple structure::

   ├── index.rst
   ├── folder1
   │     └── index.rst
   ├── folder2
         └── index.rst


All the documentation files a very simple ones containing only text with a couple of sections.

The process is started with the following command::

   $ rm -rf _build; sphinx-build -b dirhtml "." "_build" -C
