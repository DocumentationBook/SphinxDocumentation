.. _research_sphinx:

Sphinx
######

.. toctree::
   :hidden:

   top
   app_init/index
   build_phases/index
   read/index

This set of documents takes a detailed look at the documentation process in Sphinx.

Let us walk through the documentation build process in the hierarchical order from top to bottom.
Since the total process can contain hundreds of thousands calls, this journey presents
only the most important ones for a better understanding of this process.

As the process highly depends on the set of documents, so we will take a simple structure::

   ├── index.rst
   ├── folder1
   │     └── index.rst
   ├── folder2
         └── index.rst


All the documentation files a very simple ones containing only text with a couple of sections.
The building process must run in this folder.

The process is started with the following command::

   $ rm -rf _build; sphinx-build -b dirhtml "." "_build" -C

.. note:: In the following process description, you will find many diagrams displaying the classes used to create
   objects.
   For simplicity, in case of class inheritance, a diagram shows only the class from which a particular
   object is directly created.
   Therefore, all components and methods, even if they are inherited, are shown inside this class.