Detailed Sphinx
###############

.. toctree::
   :hidden:

   tutorial/index
   concepts/index
   research/index
   publish/index
   glossary

.. commented:
   :caption: Contents:

There are two software products branded as Sphinx. This book is about the well-known documentation toolset
also called Sphinx-doc to distinguish it. Such toolsets are also known as static site generators (SSG).

The main part of this book aims to provide a deep overview of the documentation build process managed by Sphinx.
Detailed information is useful for those who need to customize their documentation toolset.
This goes beyond general customization accessible through well-known tools, such as CSS,
and is mainly about Sphinx-specific ones, such as customizing extension behavior,
developing your own Sphinx extension, and creating custom event handlers.


Introduction
============

`Sphinx <https://www.sphinx-doc.org/en/master/>`_ is a powerful documentation toolset (framework) used to create
a set of bound documents (documentation tree) in different formats (HTML, PDF, ePub, and many more) taking source
documents marked up with reStructuredText (reST) or Markdown.
Sphinx is shipped as a Python package along with many other packages it depends on. Among the latter,
`Docutils <https://docutils.sourceforge.io/>`_ is the main reST interpreter.
That is why Docutils is often mentioned in this documentation.

The examples are oriented on Unix and Linux notation regarding the file system. In a Windows
environment, please make the proper changes.


Additional resources
====================

This book doesn't cover all aspects about reST, Docutils, and Sphinx. That is why you are welcome to get more information on
the subject from various internet resources, for example:

*  `Awesome Sphinx <https://github.com/yoloseem/awesome-sphinxdoc>`_
   provides the most complete collection of resources related to Sphinx.
*  `reStructuredText Markup Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_
*  `Sphinx documentation <https://www.sphinx-doc.org/en/master/index.html>`_
*  `Using the technical documentation generator <https://chiplicity.readthedocs.io/en/latest/Using_Sphinx/index.html>`_

.. commented:

   *  `Генератор документации Sphinx <https://sphinx-ru.readthedocs.io/ru/latest/>`_ (Russian)

Indices and tables
==================

* :ref:`genindex`

.. commented:

   * :ref:`modindex`
   * :ref:`search`
