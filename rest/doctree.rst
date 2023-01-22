.. _rest_doctree:

Documentation Tree
##################


Doc tree extension
==================

Although the structure of the whole documentation and the cross references between documents are part of reST, Sphinx
extended reST by providing the way of creating the tree structure of all documents (doc tree). When working with Sphinx,
you must add every reST document to this tree, otherwise you will get warning during the documentation built process
reminding you about this::

   WARNING: document isn't included in any toctree


The ``toctree`` directive
=========================

The doc tree has its root, which typically is the ``index.rst`` file in the project root folder as declared
in Sphinx configuration (the ``conf.py`` file). Starting from the root and below it, every tree branch is declared
using the ``toctree`` directive.

Suppose, on top of the tree, there are the following directories and files (in alphabetical order)::

   ├── glossary.rst
   ├── index.rst
   ├── rest
   │   ├── blocks.rst
   │   ├── doctree.rst
   │   ├── general.rst
   │   ├── index.rst
   │   └── tables.rst
   └── setup
       └── index.rst

To display the documentation structure in the final HTML documents, you should declare the top-level documentation
branch in the root ``index.rst`` file as follows::

   .. toctree::
      :hidden:

      setup/index
      rest/index
      glossary

This example declaration uses the following elements:

*  The option ``hidden`` means that the table of contents will not be displayed in the main document, but will be
   visible in the side (can be left-hand side or right-hand side) navigation panel.
*  The content of the directive contains a list of documents that will be under the root folder. Every element of the
   list is a path to the respective file. You don't need to enter the file name extension here. That is why you see
   ``setup/index`` instead of ``setup/index.rst`` in this example.

.. note:: In the HTML documentation, the documents will be arranged in the navigation tree in the order you write them
   in the directive content.

Then in the ``rest/index.rst`` file, you should specify all documents that are nested in the ``rest`` folder::

   .. toctree::
      :hidden:

      general
      doctree
      blocks
      tables

This must go down the tree until the doc tree covers all the reST files.
